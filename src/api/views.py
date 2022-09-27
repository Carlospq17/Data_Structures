from django.views import View
from django.http import JsonResponse

import json

# Create your views here.

class product_call(View):
    
    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

# try:
#     object = getattr(importlib.import_module('api.models'), product)
#     declared_object = object()
#     b = declared_object.op2()
# except AttributeError:
#     raise NameError("%s doesn't exist." % product)
# if isinstance(declared_object, (Creator)):
#     return JsonResponse(b, safe=False)
# raise TypeError("%s is not a class." % product)