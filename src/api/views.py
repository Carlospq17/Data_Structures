from django.views import View
from django.http import JsonResponse

import json

from api.custom_objects.creators.ArrayCreator import ArrayCreator
from api.custom_objects.creators.LinkedListCreator import LinkedListCreator
from api.custom_objects.creators.QueueCreator import QueueCreator
from api.custom_objects.creators.StackedCreator import StackedCreator

# Create your views here.

class product_call(View):
    
    def get(self, request):
        a = LinkedListCreator()
        b = a.get_concrete_element()
        c = b()
        return JsonResponse(f"This is a test {c.operation()}",safe = False)

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