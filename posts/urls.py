from django.urls import path
from .views import *

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('details/<int:pk>/<slug:slug>', PostDetailView.as_view(), name='details'),
	path('category/<int:pk>/<slug:slug>', CategoryDetailView.as_view(), name='category_details'),
	path('tags/<slug:slug>', TagDetailView.as_view(), name='tag_details'),
]
