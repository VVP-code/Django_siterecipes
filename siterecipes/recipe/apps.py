from django.apps import AppConfig


class RecipeConfig(AppConfig):
    verbose_name = 'Рецепты для Сони'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipe'
