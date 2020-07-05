from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import random


def index(request):
    while True:
        num = random.randint(0, 72)
        return HttpResponse(num)


def taiseiyo(request):  # 新しくnew関数を追記
    template_name = "daily/new.html"
    return render(request, template_name)
