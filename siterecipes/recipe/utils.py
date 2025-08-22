menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить рецепт', 'url_name': 'add_dish'},
        {'title': 'Контакты', 'url_name': 'contact'},

        ]

class DataMixin:
    title_page = None
    paginate_by = 3
    extra_context = {}
    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page



    def get_mixin_context(self,context,**kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context
