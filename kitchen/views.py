from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dish
from .forms import DishForm


def home(request):
    return render(request, "kitchen/home.html")


class DishListView(LoginRequiredMixin, ListView):
    model = Dish
    context_object_name = "dishes"
    template_name = "kitchen/dish_list.html"


class DishDetailView(LoginRequiredMixin, DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"


class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"

