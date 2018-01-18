# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import xx_tab1
# Register your models here.
class XX_TAB1Admin(admin.ModelAdmin):
    list_display = ['id','xx_name']
admin.site.register(xx_tab1,XX_TAB1Admin)
