from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleFormCreateView, ArticleFormUpdateView, ArticleFormDestroyView


urlpatterns = [
    path('', IndexView.as_view(), name='articles_index'),
    path('<int:id>/edit/', ArticleFormUpdateView.as_view(), name='article_update'),
    path('<int:id>/delete/', ArticleFormDestroyView.as_view(), name='article_destroy'),
    path('<int:id>/', ArticleView.as_view(), name='article_show'),
    path('create/', ArticleFormCreateView.as_view(), name='article_create'),
]