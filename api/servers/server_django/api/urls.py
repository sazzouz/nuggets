from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

# urlpatterns = [
#     path('', ListQuiz.as_view()),
#     path('<int:pk>/', DetailQuiz.as_view()),
# ]

router = DefaultRouter()
router.register('quizzes', views.QuizViewSet, basename='quiz')
router.register('comments', views.CommentViewSet, basename='comment')
# router.register('search/', views.QuizSearch.as_view(), basename='search')
urlpatterns = router.urls
