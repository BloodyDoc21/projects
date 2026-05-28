from django.urls import path
#from django.views.decorators.cache import cache_page
from .views import *


urlpatterns = [
    #path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:pk>/',NewsByCategory.as_view(extra_context={'title': 'Какой-то заголовок'}), name='category'),
    path('news/<int:pk>/', View_News.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('contact/', contact, name='contact'),
    path('add-comment/', add_comment, name='add_comment'),
    path('categories/', CategoryList.as_view(), name='categories'),
    
]
