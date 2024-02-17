from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    appname = 'Article'
    return render(
        request, 
        'articles/index.html',
        context={'appname': appname}
        )
