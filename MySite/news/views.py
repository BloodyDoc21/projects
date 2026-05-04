from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import *


def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    
    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id).order_by('-created_at')
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'category': category,
        'news': news
    }
    return render(request, 'news/category.html', context)

def test(request):
    return HttpResponse('<h1>Тестовая страница<h1>')

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
           # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            return render(request, 'news/comment_success.html', {'data': data})
    else:
        form = CommentForm()

    return render(request, 'news/add_comment.html', {'form': form})