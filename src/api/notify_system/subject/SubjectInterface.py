from __future__ import annotations
from abc import ABC, abstractmethod

from api.notify_system.observer.ObserverInterface import ObserverInterface

class SubjectInterface(ABC):

    @abstractmethod
    def attach(self, observer: ObserverInterface) -> None:
        pass

    @abstractmethod
    def detach(self, observer: ObserverInterface) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass
