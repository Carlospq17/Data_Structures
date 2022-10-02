from __future__ import annotations
from abc import ABC, abstractmethod

class Formats(ABC):

    @abstractmethod
    def print_to_format(self, data, filename):
        pass