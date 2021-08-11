from rest_framework import generics, viewsets, filters
from django.contrib.auth import get_user_model
from nuggets.models import Quiz, Comment
from .serializers import QuizSerializer, CommentSerializer, UserSerializer

# class ListQuiz(generics.ListCreateAPIView):
#     queryset = models.Quiz.objects.all()
#     serializer_class = QuizSerializer


# class DetailQuiz(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Quiz.objects.all()
#     serializer_class = QuizSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'description')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# class QuizSearch(generics.ListAPIView):
#     search_fields = ['title']
#     serializer_class = QuizSerializer

#     queryset = models.Quiz.objects.all()

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
