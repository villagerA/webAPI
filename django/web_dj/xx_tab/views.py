# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from xx_tab import models
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def hello(request):
#     return render
def hello(request):
    return HttpResponse("hello,Stanger.")

def index(request):
    return HttpResponse("this is the index.")

def get_xxtabs(request):
    # return HttpResponse("this is the xx_tabs.")
    tab_list_obj = models.xx_tab1.objects.all()
    return render(request,'list.html',{'li':tab_list_obj})

def add_xxtabs_form(request):
    return render(request,'add.html',{'li':models.xx_tab1.objects.all()})

def add_xxtabs(request):
    name = request.POST['name']
    models.xx_tab1.objects.create(xx_name=name)
    return render(request,'list.html',{'li':models.xx_tab1.objects.all()})

def del_xxtabs_form(request):
    return render(request,'del.html',{'li':models.xx_tab1.objects.all()})

def del_xxtabs(request):
    post_id = int(request.POST['post_id'])
    models.xx_tab1.objects.filter(id=post_id).delete()
    return render(request,'list.html',{'li':models.xx_tab1.objects.all()})

def update_xxtabs_form(request):
    return render(request,'update.html',{'li':models.xx_tab1.objects.all()})

def update_xxtabs(request):
    post_id = int(request.POST['post_id'])
    post_name = request.POST['post_name']
    models.xx_tab1.objects.filter(id=post_id).update(xx_name=post_name)
    # user.name=post_name
    # user.save()
    return render(request,'list.html',{'li':models.xx_tab1.objects.all()})
