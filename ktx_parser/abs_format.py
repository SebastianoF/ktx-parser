"""
import ktx_generator
https://goodcode.io/articles/python-dict-object/ 
"""
from abc import ABC, abstractmethod
from pathlib import PosixPath


class AbsFormat(ABC):
    @abstractmethod
    def convert(self, destination_file: PosixPath):
        pass
