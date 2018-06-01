from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    article = models.Article.objects.get(id=2)
    return render(request, 'blog/index.html', {'article': article})


