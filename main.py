from config.config import base_dir
from player.player import Player


def main():
    f = Player(base_dir)
    f.main()


if __name__ == '__main__':
    main()

