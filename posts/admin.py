from django.contrib import admin

from .models import SportCars, Category


class AdminSportCar:
	list_display = ['model_car', 'manufacturer']
	list_display_links = ['model_car', 'manufacturer']
	search_fields = ['model_car', 'manufacturer', 'color_car']
	list_filter = ['model_car', 'manufacturer']


admin.site.register(SportCars)
admin.site.register(Category)
