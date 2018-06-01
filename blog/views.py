from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    # article = models.Article.objects.get(id=2)
    article = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': article})


def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{"article":article})


