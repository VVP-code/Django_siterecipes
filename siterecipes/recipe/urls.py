from django.urls import path, re_path, register_converter

from . import converters
from . import views

register_converter(converters.FourDigitYearConverter, 'year4')
urlpatterns = [
    path('', views.RecipeHome.as_view(), name='home'),
    path('about/', views.AboutRecipe.as_view(), name='about'),
    path('dish/<slug:post_slug>/', views.ShowDish.as_view(), name='dish'),
    path('add_dish/', views.AddDish.as_view(), name='add_dish'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('category/<slug:cat_slug>/', views.RecipeCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.ShowTagList.as_view(), name='tag'),
    path('edit/<slug:post_slug>/', views.UpdateDish.as_view(), name='edit_dish'),

]
