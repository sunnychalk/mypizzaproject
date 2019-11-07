from django.contrib import admin
from dishes.models import Dish, Ingridient, Drink

# Register your models here.
class DishAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']
	filter_horizontal = ['ingridients']


admin.site.register(Dish, DishAdmin)
admin.site.register(Ingridient)
admin.site.register(Drink)
