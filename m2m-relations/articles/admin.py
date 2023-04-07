from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_count = 0
        for form in self.forms:
            if not len(form.cleaned_data):
                continue
            if form.cleaned_data['is_main'] and not form.cleaned_data['DELETE']:
                is_main_count += 1

        if not is_main_count:
            raise ValidationError('Не выбран основной раздел')
        elif is_main_count > 1:
            raise ValidationError('Оновной раздел может быть только один')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
