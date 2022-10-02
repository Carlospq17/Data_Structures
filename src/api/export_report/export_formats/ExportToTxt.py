from api.export_report.Export import Export
from api.export_report.Formats import Formats
from api.export_report.formats.toTxt import toTxt

class ExportToTxt(Export):

    def factory_method(self) -> Formats:
        return toTxt()