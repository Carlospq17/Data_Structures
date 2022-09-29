from django.urls import path
from api.views import sorting_methods

urlpatterns = [
    path('v1/sorting_methods', sorting_methods.as_view(), name='sorting_methods')
]