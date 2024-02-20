from django.urls import path

from django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<str:tag>/<int:article_id>', views.ArticleView.as_view(), name='article'),
]
