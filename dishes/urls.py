from django.conf.urls import url, include
from dishes import views

urlpatterns = [
    url(r'menu', views.DishesView.as_view()),
    url(r'about', views.MyView.as_view()),
    url(r'drink_list', views.DrinksListView.as_view()),
]