
""""from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore"""
from django.views.generic import TemplateView  # type: ignore


class HomeView(TemplateView):
    template_name = 'index.html'



""""class Homeview(View):
    def get( self, request):
        return HttpResponse('holaa')"""