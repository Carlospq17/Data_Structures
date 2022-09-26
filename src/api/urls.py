from django.urls import path
from api.views import product_call

urlpatterns = [
    path('structure/', product_call.as_view(), name='figure_list')
]