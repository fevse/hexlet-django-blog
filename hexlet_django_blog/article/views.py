from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article
from django.db.models import Q



class IndexView(View):
        
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', None)
        if query:
            articles = Article.objects.filter(Q(name__icontains=query))
        else:
            articles = Article.objects.all()[:5]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article,
        })
