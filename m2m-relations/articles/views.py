from django.shortcuts import render

from .models import Article, Scope
from django.forms import BaseInlineFormSet

def articles_list(request):
    template = 'articles/news.html'
    from django.db.models import Prefetch
    article = Article.objects.prefetch_related(
        Prefetch('scopes', queryset=Scope.objects.select_related('tag')))
    #article = Article.objects.prefetch_related('scopes.tag').all()#.prefetch_related('tags') select_related
    x: Article
    #for x in article:
        #print(x.scopes.all(), x.id)
        #y: Scope
        #for y in x.scopes.all():
            #print(y.id, y.is_main)
    context = {'object_list': article}
    ordering = '-published_at'
    return render(request, template, context)
