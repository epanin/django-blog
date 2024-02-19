from django.shortcuts import render

from typing import Any

from django.views import View

from django.shortcuts import redirect

from django.urls import reverse


class ArticleView(View):
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.context = {
            'appname': 'Articles!',
        }
        self.template_name = 'articles/index.html'
    
    
    
    def get(self, *args, **kwargs):
        
        tag = kwargs.get('tag', None)
        article_id = kwargs.get('article_id', None)
        if tag and article_id:
            self.context['tag'] = tag
            self.context['article_id'] = article_id
            return render(self.request, self.template_name, self.context)

        return redirect(reverse('article', kwargs={'tag': 'python', 'article_id': 42}))            
         
