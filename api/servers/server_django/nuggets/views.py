from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
from .models import Quiz, Comment
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailQuizForm, CommentForm
from django.core.mail import send_mail
from django.db.models import Count
import requests


class Dev(TemplateView):
    template_name = 'dev.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['message'] = 'Dev area'
        return context


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        context['qs'] = Quiz.published_mng.all()[:8]
        latest_quiz_list = Quiz.published_mng.order_by('-published')[:5]
        context['output'] = ', '.join([q.title for q in latest_quiz_list])
        return context


def leaderboard(request):
    context = {}
    return render(request, 'leaderboard.html', context)


class Stats(TemplateView):
    template_name = 'stats.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


def search(request, tag_slug=None):
    tag = None
    context = {}
    # if request.method.GET:
    #     Quiz.objects.all().filter(content__contains=results)
    if request.method == "GET":
        print('\n\nfrom tags\n\n')
        if 'q' in request.GET:
            q = request.GET['q']
            quiz_list = Quiz.objects.all().filter(title__icontains=q)
            context['results'] = quiz_list
            context['count'] = quiz_list.count()
            return render(request, 'search.html', context)
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            quiz_list = Quiz.objects.all()
            quiz_list = quiz_list.filter(tags__in=[tag])
            print(quiz_list)
            context['results'] = quiz_list
            context['count'] = quiz_list.count()
            context['tag'] = tag
            # Issue with paginator
            # paginator = Paginator(quiz_list, 3)  # 3 posts in each page
            # page = request.GET.get('page')
            # # print(page)
            # try:
            #     posts = paginator.page(page)
            #     context['posts'] = posts
            # except PageNotAnInteger:
            #     # If page is not an integer deliver the first page
            #     posts = paginator.page(1)
            #     context['posts'] = posts
            # except EmptyPage:
            #     # If page is out of range deliver last page of results
            #     posts = paginator.page(paginator.num_pages)
            #     context['posts'] = posts
            return render(request, 'search.html', context)
    else:
        return JsonResponse('Must be a GET request.')


def quiz(request, id):
    context = {}
    context['id'] = id
    # Issue with get_object_or_404, having to use list instead
    quiz = get_list_or_404(Quiz, id=id)
    # quiz = Quiz.objects.filter(id=id)
    context['quiz'] = quiz
    print(quiz)
    # List of active comments for this post
    comments = quiz[0].comments.filter(active=True)
    new_comment = None
    # List of similar posts
    post_tags_ids = quiz[0].tags.values_list('id', flat=True)
    similar_quizzes = Quiz.published_mng.filter(
        tags__in=post_tags_ids).exclude(id=quiz[0].id)
    similar_quizzes = similar_quizzes.annotate(
        same_tags=Count('tags')).order_by('-same_tags', '-published')[:4]
    context['similar'] = similar_quizzes

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.quiz = quiz[0]
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()
    context['comments'] = comments
    context['comment_form'] = comment_form
    context['new_comment'] = new_comment

    return render(request, 'quiz.html', context)


def quiz_share(request, id):
 # Retrieve post by id
    quiz = get_object_or_404(Quiz, id=id, status='published')
    if request.method == 'POST':
        # Form was submitted
        form = EmailQuizForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
            quiz_url = request.build_absolute_uri(quiz.get_absolute_url())
            print(quiz_url)
            subject = f"{cd['name']} recommends you read " f"{quiz.title}"
            message = f"Read {quiz.title} at {quiz_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        sent = False
        form = EmailQuizForm()
    return render(request, 'share.html', {'quiz': quiz, 'form': form, 'sent': sent})


def json_page(request):
    context = {}
    res = requests.get('https://swapi.dev/api/people')
    context['1'] = 'First message'
    return JsonResponse(res.json())
