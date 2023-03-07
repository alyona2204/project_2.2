from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, forms

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            return

        tags = []
        for form in self.forms:
            if form.cleaned_data:
                tag = form.cleaned_data['tag']
                if tag in tags:
                    raise forms.ValidationError("Duplicate name %s." % tag)
                tags.append(tag)


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
