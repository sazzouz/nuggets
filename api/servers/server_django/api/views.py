from rest_framework import generics, viewsets, filters

from nuggets import models
from .serializers import QuizSerializer, CommentSerializer

# class ListQuiz(generics.ListCreateAPIView):
#     queryset = models.Quiz.objects.all()
#     serializer_class = QuizSerializer


# class DetailQuiz(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Quiz.objects.all()
#     serializer_class = QuizSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'description')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer


# class QuizSearch(generics.ListAPIView):
#     search_fields = ['title']
#     serializer_class = QuizSerializer

#     queryset = models.Quiz.objects.all()
