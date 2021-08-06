from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Quiz

# Create your views here.
# def index(request):
#     return HttpResponse('Nuggets')

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        context['qs'] = Quiz.objects.all()
        return context