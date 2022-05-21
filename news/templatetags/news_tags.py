import re
from unicodedata import category
from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()


# simple_tag для него нужен страница: _sidebar.html, index.html
@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


# inclusion_tag для него нужен страница: list_categories.html, _sidebar.html \, inde.html
@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello', arg2='world'):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {"categories": categories, "arg1": arg1, "arg2": arg2}
