from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Car
# Create your views here.

class HomePageView(ListView):
    model = Car
    template_name = "home.html"
    
class HomeDetailView(DetailView):
    model = Car
    template_name = "home_detail.html"
    
class HomeNewView(CreateView):
    model = Car
    template_name = "home_new.html"
    fields =  ['name', 'year', 'img', 'cost']

class HomeDeleteView(DeleteView):
    model = Car
    template_name = "home_delete.html"
    success_url = reverse_lazy("home")
    
class HomeEditView(UpdateView):
    model = Car
    template_name = "home_edit.html"
    fields =  ['name', 'year', 'img', 'cost']
    