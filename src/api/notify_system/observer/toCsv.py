from api.notify_system.observer.ObserverInterface import ObserverInterface
from api.notify_system.subject.SubjectInterface import SubjectInterface

class toCsv(ObserverInterface):
    def update(self, subject: SubjectInterface) -> None:
        print("toCSV: Reacted to the event ",{subject._state})

