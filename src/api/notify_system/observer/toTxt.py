from api.notify_system.observer.ObserverInterface import ObserverInterface
from api.notify_system.subject.SubjectInterface import SubjectInterface

class toTxt(ObserverInterface):
    def update(self, subject: SubjectInterface) -> None:
        print("toTxt: Reacted to the event",{subject._state})
