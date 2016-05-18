from pyaudio import PyAudio
from wave import open as open_wav
from pyaudio import get_format_from_width
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Manager
from time import sleep


class Sound:
    def __init__(self, filename: str, metre: float, q: Manager().Queue,
                 *, loop: bool=False):
        self.filename = filename
        self.q = q
        self.wf = open_wav(self.filename, "rb")
        self.formatting = get_format_from_width(self.wf.getsampwidth())
        self.channels = self.wf.getnchannels()
        self.no_frames = self.wf.getnframes()
        self.rate = self.wf.getframerate()
        self.data = self.wf.readframes(self.no_frames)
        self.duration = self.no_frames/self.rate
        self.wf.close()

        self.qs = []
        self.processes_pointers = []
        if not loop:
            self.no_p = int(self.duration*metre*10)+2
            self.qs = [Queue() for _ in range(self.no_p)]
            self.ps = [Process(
                target=self.throw_process,
                args=(q,))
                       for q in self.qs]
            self.setup()
            self.i = 0


    def play(self):
        """ Plays a sound by lifting process queue block. """

        self.qs[self.i].put(True)
        self.i = (self.i+1) % self.no_p

    def loop_sound(self):
        """ Initiate a sound loop. """

        q = Queue()
        p = Process(target=self.throw_process_loop, args=(q,))
        p.daemon = True
        p.start()
        self.processes_pointers += [p]
        self.qs += [q]

    def throw_process_loop(self, q: Queue):
        """ A sound loop. """

        import sounddevice
        p = PyAudio()
        stream = p.open(
            format=self.formatting,
            channels=self.channels,
            rate=self.rate,
            output=True
        )
        while q.empty():
            stream.write(self.data)
        p.terminate()
        stream.close()

    def throw_process(self, q):
        """ Plays a sound. """

        import sounddevice
        p = PyAudio()
        stream = p.open(
            format=self.formatting,
            channels=self.channels,
            rate=self.rate,
            output=True
        )
        while True:
            if not q.get():
                break
            stream.write(self.data)
        p.terminate()
        stream.close()

    def setup(self):
        """ Sets up processes. """

        for p in self.ps:
            p.daemon = True
            p.start()
            self.processes_pointers += [p]

    def terminate_capture(self):
        for q in self.qs:
            q.put(False)

    def terminate_join(self):
        for p in self.processes_pointers:
            p.is_alive()
            p.terminate()
            p.join()
