from ..models import xx_tab1
from django.shortcuts import render
from django import template

register = template.Library()

@register.simple_tag
def get_xx_tab_list():
    return xx_tab1.objects.all()
