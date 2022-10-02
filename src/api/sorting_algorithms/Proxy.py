from api.sorting_algorithms.SortInterface import SortInterface
import time
class Proxy(SortInterface):
    _time = 0

    def __init__(self, real_subject: SortInterface) -> None:
        self._real_subject = real_subject

    def sort(self, arr):
        start = time.perf_counter()
        self._real_subject.sort(arr)
        end = time.perf_counter()
        self._time = end - start
        return arr

    def generateExampleArray(self, size):
        return self._real_subject.generateExampleArray(size)
    
    def getTime(self):
        return self._time

