from django.shortcuts import render, get_object_or_404
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


class CategoryDetailView(ListView):
    model = SportCars
    template_name = 'categories/category_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return SportCars.objects.filter(category=self.category).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        context['category'] = self.category
        return context
