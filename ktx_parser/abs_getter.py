from abc import ABC, abstractmethod


class AbsGetter(ABC):
    @abstractmethod
    def get_dict(self):
        pass

    @abstractmethod
    def get(self):
        pass
