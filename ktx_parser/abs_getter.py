from abc import ABC, abstractmethod


class AbsGetter(ABC):
    @abstractmethod
    def get_initializer(self) -> str:
        """ Initializer for interactive formats."""
        pass

    @abstractmethod
    def get_dict(self) -> dict:
        pass

    @abstractmethod
    def get(self):
        pass
