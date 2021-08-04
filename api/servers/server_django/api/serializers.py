from rest_framework import serializers
from nuggets import models


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Quiz