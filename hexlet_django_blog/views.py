from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):

    template_name = 'index.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Stranger'
        return context


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )


def python_42(request):
    return redirect('article', tags='python', article_id=42)
