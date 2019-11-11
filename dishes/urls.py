from django.conf.urls import url, include
from dishes import views

urlpatterns = [
    url(r'menu', views.DishesView.as_view()),
    url(r'about', views.MyView.as_view()),
    url(r'drink_list', views.DrinksListView.as_view()),
    url(r'make_order/', views.MakeOrder.as_view()),
    url(r'dish_form', views.DishCreate.as_view()),
    url(r'make_drink_order/', views.MakeDrinkOrder.as_view()),
    url(r'dish_form/int:pk>/edit/', views.DishUpdate.as_view()),
]