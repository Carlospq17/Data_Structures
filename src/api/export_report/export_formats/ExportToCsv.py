from api.export_report.Export import Export
from api.export_report.Formats import Formats
from api.export_report.formats.toCsv import toCsv

class ExportToCsv(Export):

    def factory_method(self) -> Formats:
        return toCsv()