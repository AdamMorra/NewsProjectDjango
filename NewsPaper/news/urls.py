from django.urls import path
# Импортируем созданные нами представления
from .views import (
    NewsList, NewDetail, PostSearch, NewsCreate, ArticlesCreate,
    NewsUpdate, ArticlesUpdate, NewsDelete, ArticlesDelete
)

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', NewsList.as_view(), name='news_list'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', NewDetail.as_view(), name='news_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='articles_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
]
