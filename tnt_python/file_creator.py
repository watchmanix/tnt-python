import os
from tempfile import NamedTemporaryFile

from .utils import get_file_name


class FileCreator:
    def __init__(self, file_name=get_file_name()):
        self.file = NamedTemporaryFile(delete=False)
        self.path = self.file.name
        self.file.name = file_name + ".txt"

    def write(self, text: bytes):
        self.file.write(text)
        self.file.seek(0)

    def close(self):
        self.file.close()
        os.unlink(self.path)



