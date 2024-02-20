from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

from typing import Any

from .models import Article


class ArticleView(View):    
    
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={'article': article})           
         

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={'articles': articles})