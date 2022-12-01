from django.shortcuts import render
from django.views import View



class IndexView(View):

        
    def get(self, request, tags=None, article_id=None):
        return render(request, 'article/index.html', context={
            'title': "Статьи", 'tags': tags, 'article_id': article_id,
        })
        
