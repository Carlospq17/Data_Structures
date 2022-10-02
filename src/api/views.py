from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse

import json
import importlib

from api.sorting_algorithms.Proxy import Proxy
from api.sorting_algorithms.SortInterface import SortInterface

from api.export_report.Export import Export
from api.export_report.export_formats.ExportToCsv import ExportToCsv
from api.export_report.export_formats.ExportToTxt import ExportToTxt

# Create your views here.

class sorting_methods(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        json_data = json.loads(request.body)
        size = json_data['size']
        sorting_methods = json_data['sorting_methods']
        data = {}

        for element in sorting_methods:
            try:
                method = getattr(importlib.import_module(f"api.sorting_algorithms.{element}"), element)
                proxy = Proxy(method())
                original_array = proxy.generateExampleArray(size)
                sorted_array = original_array.copy()
                proxy.sort(sorted_array)
            except:
                raise NameError("%s doesn't exist." % element)
            finally:
                if isinstance(proxy, (SortInterface)):
                    data[element] = {
                        'time' : proxy.getTime(),
                        'original_array' : original_array,
                        'sorted_array' : sorted_array
                    }
                else:
                    raise TypeError("%s is not a class." % element)
        resp = {}
        resp['data'] = data
        return HttpResponse(json.dumps(resp), content_type="application/json")

    def post(self, request):
        json_data = json.loads(request.body)
        file_metadata = self.generateReport(ExportToCsv(), json_data)
        return HttpResponse(file_metadata['file'], headers={
            'Content-Type': 'application/pdf text/csv text/plain',
            'Content-Disposition': 'attachment; filename='+file_metadata['file_name']+'.'+file_metadata['file_extension'],
            }) 

    def generateReport(self, export: Export, data):
        return export.toFormat(data)
        
