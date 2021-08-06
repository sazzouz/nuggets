from django.shortcuts import render, get_object_or_404
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
        latest_quiz_list = Quiz.objects.order_by('-pub_date')[:5]
        context['output'] = ', '.join([q.title for q in latest_quiz_list])
        return context


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'nuggets/quiz-detail.html', {'question': quiz})


def search(request):
    context = {}
    # if request.method.GET:
    #     Quiz.objects.all().filter(content__contains=results)
    if request.method == "GET":
        if 'q' in request.GET:
            q = request.GET['q']
            context['results'] = Quiz.objects.all().filter(title__icontains=q)
            context['count'] = len(list(context['results']))
            return render(request, 'search.html', context)
    else:
        return HttpResponse('Must be a GET request.')
