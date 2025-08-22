from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Recipe, Category, DevelopersInspirers


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'time_to_cook', 'content', 'is_published', 'cat', 'tags', 'folk', 'image',
              'post_image']
    readonly_fields = ['folk', 'post_image']
    filter_horizontal = ('tags',)
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'cat', 'is_published', 'post_image']
    list_display_links = ['title']
    ordering = ['title']
    list_editable = ['cat', 'is_published', ]
    list_per_page = 15
    search_fields = ['title', 'cat__name']
    list_filter = ['cat__name']
    save_on_top = True

    @admin.display(description='Изображение')
    def post_image(self, recipe: Recipe):
        if recipe.image:
            return mark_safe(f'<img src={recipe.image.url} width=200 />')
        return 'Без фото'

    @admin.action(description='опубликовать')
    def set_published(self, request, queryset):
        queryset.update(is_published=True)

    @admin.display(description='О слаге')
    def info_slug(self, post: Recipe):
        return f'Слаг содержит {len(post.slug)} символов'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    list_display_links = ['id', 'name']

@admin.register(DevelopersInspirers)
class DevelopersInspirersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'post_photo']
    ordering = ['name']
    list_display_links = ['name']

    @admin.display(description='Изображение')
    def post_photo(self, developer: DevelopersInspirers):
        if developer.photo:
            return mark_safe(f'<img src={developer.photo.url} width=200 />')
        return 'Без фото'