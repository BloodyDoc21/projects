from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:pk>/',NewsByCategory.as_view(extra_context={'title': 'Какой-то заголовок'}), name='category'),
    path('news/<int:pk>/', View_News.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('test/', test),
    path('add-comment/', add_comment, name='add_comment'),
    path('categories/', CategoryList.as_view(), name='categories'),
]
