from django.views import View
from django.http import HttpResponse

import json
import importlib

from api.sorting_algorithms.Proxy import Proxy
from api.sorting_algorithms.SortInterface import SortInterface

# Create your views here.

class sorting_methods(View):
    
    def get(self, request):
        json_data = json.loads(request.body)
        size = json_data['size']
        sorting_methods = json_data['sorting_methods']
        data = {}

        for element in sorting_methods:
            try:
                method = getattr(importlib.import_module('api.sorting_algorithms.'+element), element)
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
        pass
