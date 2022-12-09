from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Article
from django.db.models import Q
from .forms import ArticleForm



class IndexView(View):
        
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', None)
        if query:
            articles = Article.objects.filter(Q(name__icontains=query))
        else:
            articles = Article.objects.all()
        return render(request, 'article/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles_index') 
        return render(request, 'article/create.html', {'form': form})
