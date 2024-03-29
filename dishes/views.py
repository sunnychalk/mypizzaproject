from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from dishes.models import Dish, Drink
from django.http import HttpResponse 
from dishes.forms import ContactForm, DrinkForm, DishForm

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


class MakeOrder(FormView):
	template_name = 'make_order.html'
	form_class = ContactForm
	success_url = '/'

	def get_initial(self):
		initial = super().get_initial()
		initial['name'] = 'TEST'
		return initial 

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

	def form_invalid(self, form):
		print('So sad!')
		return super().form_invalid(form)


class MakeDrinkOrder(FormView):
	template_name = 'make_drink_order.html'
	form_class = DrinkForm
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class DishCreate(CreateView):
	template_name = 'dish_form.html'
	model = Dish
	fields = ['name', 'ingridients', 'is_meat', 'is_vegan', 'price']
	success_url = 'menu.html'


class DishUpdate(UpdateView):
	form_class = DishForm
	model = Dish
	template_name = 'dish_form.html'
	success_url = '/'