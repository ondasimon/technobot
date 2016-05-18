from time import sleep
from time import time
import sounddevice as sound_dev
import soundfile as sf
import struct
from wave import open as wave_open
#import numpy
import pyglet


class Sound:
    def __init__(self, filename):
        self.filename = filename

    def setup(self):
        pass

    def play(self):
        start = time()
        player = pyglet.media.Player()
        sound = pyglet.media.load(filename=self.filename)
        player.queue(sound)
        player.play()
        print(time()-start)

        return
        wav = wave_open(self.filename, "rb")
        params = (nchannels, sampwidth, rate, nframes, comp, compname) = wav.getparams()
        frames = wav.readframes(nframes*nchannels)
        wav.close()
        out = struct.unpack_from("%dh" % nframes*nchannels, frames)

        #data, fs = sf.read(self.filename)
        #sound = sf.SoundFile(file=self.filename)
        #data = sound.read()
        #with sf.SoundFile("test.wav", "w", samplerate=fs, channels=2, subtype="FLOAT") as f:
        #    f.write(data)
        #print(fs)
        sound_dev.play(out, samplerate=44100, blocking=True)
