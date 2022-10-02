from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime

class Export(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def toFormat(self, data):
        format = self.factory_method()
        file_metadata = {}
        file_metadata['file_name'] = f"Report_{datetime.now()}"
        file_metadata['file_extension'] = format.get_extension()
        report = format.construct_report(data)
        file_metadata['file'] = format.print_to_format(report, file_metadata['file_name'])
        return file_metadata



