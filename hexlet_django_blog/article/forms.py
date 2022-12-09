from django.forms import ModelForm, CharField
from .models import Article

class ArticleForm(ModelForm):

    name = CharField(max_length=49, required=True)

    class Meta:
        model = Article
        fields = ['name', 'body']
