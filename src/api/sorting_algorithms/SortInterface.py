from __future__ import annotations
from abc import ABC, abstractmethod
from array import array

class SortInterface(ABC):

    @abstractmethod
    def sort(self, arr):
        pass

    @abstractmethod
    def generateExampleArray(self, size):
        pass