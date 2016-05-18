from time import sleep
from time import time
from files.addresses import FilesModel
from player.sound import Sound
from random import choice
from multiprocessing import Manager


class Player:
    def __init__(self, base_dir):
        self.fm = FilesModel(base_dir)
        self.files = self.fm.filenames
        self.bpm = 125
        self.metre = 60 / self.bpm
        self.start = time()
        self.hits = self.fm.hits
        self.beat = self.fm.beats
        self.rounds = 5
        self.m = Manager()
        self.q = self.m.Queue()
        self.sounds = [Sound(choice(self.hits), self.metre, self.q) for _ in range(self.rounds)]

    def main(self):
        """ Main. """

        beat = self.beats()
        for s in self.sounds:
            self.baseline(s)
        self.terminate(beat)


    def master(self):
        #TODO play a loop as relative speed mesurement.
        pass

    def baseline(self, filename):
        """ Plays single sounds. """

        start = time()
        bass = filename
        for _ in range(8):
            bass.play()
            sleep(self.metre)
        bass.terminate_capture()
        print(time()-start)

    def beats(self):
        """ Sets up a loop. """
        beat = Sound(choice(self.beat), self.metre, self.q, loop=True)
        beat.loop_sound()
        return beat

    def melody(self):
        #TODO make a melody.
        pass

    def sync(self):
        pass

    def terminate(self, beat):
        #TODO terminate everythong nicely.
        for s in self.sounds:
            s.terminate_join()
        beat.terminate_capture()
        sleep(1)
        beat.terminate_join()