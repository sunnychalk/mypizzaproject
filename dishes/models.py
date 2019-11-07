from django.db import models

# Create your models here.
class BaseItem(models.Model):
	name = models.CharField(max_length=254)
	price = models.DecimalField(max_digits=9, decimal_places=2, default=0)

	class Meta:
		abstract = True

	def __str__(self):
		return self.name


class Ingridient(BaseItem):
	
	class Meta:
		verbose_name = 'Ингридиент'
		verbose_name_plural = 'Ингридиенты'


class Dish(BaseItem):
	ingridients = models.ManyToManyField(Ingridient, blank=True, null=True)
	is_vegan = models.BooleanField(default=False)
	is_meat = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Блюдо'
		verbose_name_plural = 'Блюда'


class Drink(BaseItem):

	class Meta:
		verbose_name = 'Напиток'
		verbose_name_plural = 'Напитки'
