from abc import ABC, abstractmethod, abstractstaticmethod
from typing import Dict, List, Union


class AbsGetter(ABC):
    @staticmethod
    def get_getter_tag() -> str:
        pass

    @abstractstaticmethod
    def get_headers_keys() -> Union[List, Dict]:
        pass

    @abstractstaticmethod
    def get_numbered_keys() -> Union[List, Dict]:
        pass

    @abstractmethod
    def get_interactive_initializer(self) -> str:
        """ Initializer for interactive formats."""

    @abstractmethod
    def get_dict(self) -> dict:
        pass

    @abstractmethod
    def get_quantity_numbered_keys(self) -> (int, int):
        pass

    def get_entries(self):
        pass