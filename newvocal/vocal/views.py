from django.shortcuts import render
from django.views.generic.list import ListView

class HomeView(ListView):
    template_name = "recipe/home.html"


# Create your views here.
