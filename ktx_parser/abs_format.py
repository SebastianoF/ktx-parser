"""
import ktx_generator
https://goodcode.io/articles/python-dict-object/ 
"""
from abc import ABC, abstractmethod


class AbsFormat(ABC):
    @abstractmethod
    def convert(self):
        pass
