from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView , CreateView, UpdateView
from .forms import AddPostForm, UploadFileForm
from .models import Recipe, Category, TagPosts, UploadFiles, DevelopersInspirers
from .utils import DataMixin
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class RecipeHome(DataMixin, ListView):
    template_name = 'recipe/index.html'
    context_object_name = 'posts'
    title_page = 'Главная страница'

    def get_queryset(self):
        return Recipe.recipeReady.filter(is_published=True).select_related('cat')

class AboutRecipe(DataMixin, TemplateView):
    template_name = 'recipe/about.html'
    extra_context = {'title': 'О сайте'}

class ShowDish(DataMixin, DetailView):
    model = Recipe
    template_name = 'recipe/show_dish.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)

class AddDish(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'recipe/add_dish.html'
    success_url = reverse_lazy('home')
    title_page = 'Добавить блюдо'
    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)

class UpdateDish(DataMixin, UpdateView):
    model = Recipe
    template_name = 'recipe/add_dish.html'
    success_url = reverse_lazy('home')
    fields = ['title','ingredients','time_to_cook','content','cat','tags','image']
    title_page = 'Изменение блюда'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)

class RecipeCategory(DataMixin, ListView):
    template_name = 'recipe/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Recipe.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context,title='Категория - ' + cat.name)

class ShowTagList(DataMixin, ListView):
    template_name = 'recipe/index.html'
    context_object_name = 'posts'
    allow_empty = False
    def get_queryset(self):
        return Recipe.objects.filter(tags__slug=self.kwargs['tag_slug'],is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPosts.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context,title='Тег - ' + tag.title)

class Contact(DataMixin, ListView):
    template_name = 'recipe/contact.html'
    model = DevelopersInspirers
    context_object_name = 'items'
    paginate_by = 1
    def get_queryset(self):
        return DevelopersInspirers.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Кто это сделал!?',)

def page_not_found(request, exception):
    return render(request, 'recipe/404.html', status=404)


