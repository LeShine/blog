from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharFiled(max_length=32, default='title')
    content = models.TextFiled(null=True)

