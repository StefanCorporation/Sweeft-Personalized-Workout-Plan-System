from django.shortcuts import render
from django.views.generic.base import TemplateView
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'workout/index.html'
    title = 'Sweeft-Sport'


