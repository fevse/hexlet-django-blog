from django.shortcuts import render
from django.views import View
from .models import Article



class IndexView(View):
        
    def get(self, request, tags=None, article_id=None):
        articles = Article.objects.all()
        return render(request, 'article/index.html', context={
            'articles': articles,
            'title': "Статьи", 
            'tags': tags, 
            'article_id': article_id,
        })
        
