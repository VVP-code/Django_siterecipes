from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django import forms
from django.contrib.auth import get_user_model
def translit_to_eng(s: str) -> str:
    d = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya'
    }
    return ''.join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))

# Create your models here.
class RecipeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(time_to_cook__gt=0)

class Recipe(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=30, verbose_name='Название')
    ingredients = models.CharField(max_length=200, verbose_name='Ингредиенты')
    time_to_cook = models.IntegerField(blank=True, default=0, verbose_name='Время готовки')
    content = models.TextField(max_length=1000, verbose_name='Описание блюда')
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name='Ссылка')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='recipes', verbose_name='Категории')
    tags = models.ManyToManyField('TagPosts', blank=True, related_name='tags', verbose_name='Тег')
    folk = models.OneToOneField('Folkcreate', on_delete=models.PROTECT, null=True, blank=True, related_name='folk')
    is_published = models.BooleanField(default=False, verbose_name='Статус')
    objects = models.Manager()
    recipeReady = RecipeManager()
    image = models.ImageField(upload_to='photo/%y/%m/%d', verbose_name='Фото', blank=True, default=None, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, verbose_name='Автор',default=None)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'
        ordering = ['-slug']
        indexes = [
            models.Index(fields=['slug']),
        ]

    def get_absolute_url(self):
        return reverse('dish', kwargs={'post_slug': self.slug})

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(translit_to_eng(self.title))
    #     super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='название')
    slug = models.SlugField(max_length=30)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

class TagPosts(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

class Folkcreate(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.name

class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model', verbose_name='Файл')

class DevelopersInspirers(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='uploads_model', verbose_name='Фото')
    describt = models.TextField(verbose_name='Описание')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Разработчики и вдохновители'