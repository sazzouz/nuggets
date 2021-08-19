from django.utils.safestring import mark_safe
import markdown
from django.db.models import Count
from django import template
from ..models import Quiz
register = template.Library()


@register.simple_tag
def total_quizzes():
    return Quiz.published_mng.count()


@register.inclusion_tag('latest_quizzes.html')
def show_latest_quizzes(count=5):
    latest_quizzes = Quiz.published_mng.order_by('-published')[:count]
    return {'latest_quizzes': latest_quizzes}


@register.simple_tag
def get_most_commented_quizzes(count=5):
    return Quiz.published_mng.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
