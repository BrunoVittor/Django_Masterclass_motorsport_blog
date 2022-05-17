from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import SportCars, Category


class IndexView(ListView):
	template_name = 'posts/index.html'
	model = SportCars
	context_object_name = 'posts'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context


class PostDetailView(DetailView):
	template_name = 'posts/detail.html'
	model = SportCars
	context_object_name = 'detail_view'

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		return context
