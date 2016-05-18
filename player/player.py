from time import sleep
from time import time
from files.addresses import FilesModel
from player.sound import Sound
from random import choice


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
        self.sounds = [Sound(choice(self.hits), self.metre) for _ in range(self.rounds)]

    def main(self):
        beat = self.beats()
        for s in self.sounds:
            self.baseline(s)
        beat.terminate()
        sleep(1)

    def baseline(self, filename):
        start = time()
        bass = filename #Sound(filename, self.metre)
        bass.setup()
        for _ in range(16):
            bass.play()
            sleep(self.metre/2)
        bass.terminate()
        print(time()-start)

    def beats(self):
        beat = Sound(choice(self.beat), self.metre)
        beat.setup()
        beat.loop_sound()
        return beat

    def melody(self):
        pass

    def play_sound(self, filename):
        pass

    def sync(self):
        pass
