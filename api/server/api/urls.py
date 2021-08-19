from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

router = DefaultRouter()
router.register('quizzes', views.QuizViewSet, basename='quiz')
router.register('questions', views.QuestionViewSet, basename='question')
router.register('comments', views.CommentViewSet, basename='comment')
# router.register('search/', views.QuizSearch.as_view(), basename='search')
urlpatterns = router.urls

urlpatterns += [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
