from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import QuizViewSet

# urlpatterns = [
#     path('', ListQuiz.as_view()),
#     path('<int:pk>/', DetailQuiz.as_view()),
# ]

router = DefaultRouter()
router.register('', QuizViewSet, basename='quiz')
urlpatterns = router.urls