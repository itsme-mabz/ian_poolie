# myapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('pb-data/', process_and_forward_data, name='process_and_forward_data'),
]
