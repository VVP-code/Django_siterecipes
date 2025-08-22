from django import template
from django.db.models import Count

from recipe.models import Category, TagPosts
from recipe.utils import menu
register = template.Library()

@register.simple_tag
def get_menu():
    return menu
@register.inclusion_tag('recipe/list_categories.html')
def show_category(cat_selected_id=0):
    cats = Category.objects.annotate(total=Count('recipes')).filter(total__gt=0)
    return {"cats": cats, "cat_selected": cat_selected_id}


@register.inclusion_tag('recipe/list_tags.html')
def show_all_tags():
    tags = TagPosts.objects.annotate(total=Count('tags')).filter(total__gt=0)
    return {"tags": tags}
