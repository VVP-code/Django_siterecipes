from django.urls import path, re_path, register_converter

from . import converters
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', )
]