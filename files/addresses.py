from os import walk
from os.path import join


class FilesModel:
    """ This class orders sounds according to need. """

    def __init__(self, base_dir, *args):
        self.base_dir = base_dir
        self._filenames = []
        self._hits = []
        self._beats = []

    @property
    def filenames(self) -> dict:
        """ Getter """

        if self._filenames:
            return self._filenames

        for path, _, files in walk(self.base_dir):
            self._filenames += [join(path, file) for file in files if ".wav" in file]

        return self._filenames

    @property
    def hits(self):
        """ Getter """

        if self._hits:
            return self._hits

        self._hits = [x for x in self.filenames if "hits" in x.lower()
                      and "fx" not in x.lower()]
        return self._hits

    @property
    def beats(self):
        """ Getter """

        if self._beats:
            return self._beats

        self._beats = [x for x in self.filenames if "beats" in x.lower()]
        return self._beats