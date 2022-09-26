from api.notify_system.subject.SubjectInterface import SubjectInterface
from api.notify_system.observer.ObserverInterface import ObserverInterface

from random import randrange
from typing import List

class ExportToFormat(SubjectInterface):

    _state: int = None

    _observers: List[ObserverInterface] = []

    def attach(self, observer: ObserverInterface) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: ObserverInterface) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def export(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()