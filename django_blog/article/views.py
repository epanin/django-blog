from django.shortcuts import render

from django.http import HttpResponse

from typing import Any, Dict

from django.views import View


class ArticleView(View):
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.context = {'appname': 'Articles!'}
        self.template_name = 'articles/index.html'
    
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)
