# coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import myboke1.models as models

# 首页
def index(request):
    return render(request,'index.html')