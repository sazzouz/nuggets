from rest_framework import generics, viewsets

from nuggets import models
from .serializers import QuizSerializer

# class ListQuiz(generics.ListCreateAPIView):
#     queryset = models.Quiz.objects.all()
#     serializer_class = QuizSerializer


# class DetailQuiz(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Quiz.objects.all()
#     serializer_class = QuizSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer