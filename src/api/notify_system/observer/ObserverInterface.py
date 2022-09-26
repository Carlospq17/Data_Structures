from __future__ import annotations
from abc import ABC, abstractmethod

from api.notify_system.subject import SubjectInterface

class ObserverInterface(ABC):

    @abstractmethod
    def update(self, subject: SubjectInterface) -> None:
        pass
