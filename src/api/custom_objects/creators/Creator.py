from __future__ import annotations
from abc import ABC, abstractmethod
from api.custom_objects.structure import Structure

class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def get_concrete_element(self) -> Structure:
        product = self.factory_method()
        return product