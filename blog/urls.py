from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('article/(?p<article_id>[0-9]+)$/', views.article_page),

]
