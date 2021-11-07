from django.shortcuts import render
from django.views.generic import TemplateView


# TemplateViewをもとにclass作成
class IndexView(TemplateView):
    template_name = 'index.html'