from django.urls import path
from . import views
from .views import article_search, admin_page, create_news, create_article

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.article_list, name='article_list'),
    path('news/<int:id>/', views.article_detail, name='article_detail'),
    path('news/search/', article_search, name='article_search'),  # Маршрут для поиска
    path('news/admin/', admin_page, name='admin_page'),  # Административная страница
    path('news/create/', create_news, name='create_news'),  # Создание новости
    path('articles/create/', create_article, name='create_article'),  # Создание статьи
    path('news/<int:pk>/edit/', views.edit_news, name='edit_news'),
    path('articles/<int:pk>/edit/', views.edit_article, name='edit_article'),
    path('news/<int:pk>/delete/', views.delete_news, name='delete_news'),  # Удаление новости
    path('articles/<int:pk>/delete/', views.delete_article, name='delete_article'),  # Удаление статьи
]
