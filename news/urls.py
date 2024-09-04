from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.article_list, name='article_list'),
    path('news/<int:id>/', views.article_detail, name='article_detail'),
]
