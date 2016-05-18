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
        self.sounds = []

    def main(self):
        beat = self.beats()
        for _ in range(self.rounds):
            self.baseline(choice(self.hits))
        beat.terminate()
        sleep(1)

    def baseline(self, filename):
        bass = Sound(filename, self.metre)
        bass.setup()
        start = time()
        for _ in range(16):
            bass.play()
            sleep(self.metre/2)
        print(time()-start, self.metre*8)
        bass.terminate()

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
