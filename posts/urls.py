from django.urls import path
from .views import *

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('details/<int:pk>/<slug:slug>', PostDetailView.as_view(), name='details'),
]
