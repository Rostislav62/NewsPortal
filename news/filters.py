import django_filters
from .models import Article
from django import forms

class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    author = django_filters.CharFilter(lookup_expr='icontains', label='Автор')
    publication_date = django_filters.DateFilter(
        field_name='publication_date',
        lookup_expr='gt',
        label='Позже даты',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    # Поля для фильтрации по типу статьи или новости
    type_article = django_filters.BooleanFilter(
        method='filter_type_article',
        label='Статья',
        widget=forms.CheckboxInput
    )
    type_news = django_filters.BooleanFilter(
        method='filter_type_news',
        label='Новость',
        widget=forms.CheckboxInput
    )

    class Meta:
        model = Article
        fields = ['title', 'author', 'publication_date']

    # Метод для фильтрации статей
    def filter_type_article(self, queryset, name, value):
        if value:  # Фильтруем, если выбран флажок "Статья"
            return queryset.filter(type=False)
        return queryset

    # Метод для фильтрации новостей
    def filter_type_news(self, queryset, name, value):
        if value:  # Фильтруем, если выбран флажок "Новость"
            return queryset.filter(type=True)
        return queryset
