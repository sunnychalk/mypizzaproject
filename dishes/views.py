from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from dishes.models import Dish, Drink
from django.http import HttpResponse

# Create your views here.
class MyView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse('Hello, it is my pizza_project!')


class DrinksListView(ListView):
	model = Drink
	template_name = 'drink_list.html'


class DishesView(TemplateView):
	template_name = 'menu.html'

	def get_context_data(self, **kwargs):
		context = super(DishesView,self).get_context_data(**kwargs)
		context['dishes'] = Dish.objects.all().order_by('name')
		return context
