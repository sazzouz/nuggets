from . import views
from django.urls import path, include
# from .feeds import LatestPostsFeed

urlpatterns = [
    path('dev/', views.Dev.as_view(),
         kwargs={'sample': 'sample value'}, name='dev'),
    path('', views.Home.as_view(), name='home'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('stats/', views.Stats.as_view(), name='stats'),
    path('search/', views.search, name='search'),
    path('tag/<slug:tag_slug>/', views.search, name='search_by_tag'),
    path('quiz/<uuid:id>/', views.quiz, name='quiz'),
    path('quiz/<uuid:id>/share/', views.quiz_share, name='quiz_share'),
    # path('feed/', LatestPostsFeed(), name='post_feed'),
    path('json_page', views.json_page, name='json_page')
]
