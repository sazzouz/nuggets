from rest_framework import serializers
from nuggets import models


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description'
        )
        model = models.Quiz


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = (
        #     'quiz',
        #     'name',
        #     'email',
        #     'body',
        #     'created',
        #     'updated'
        # )
        fields = '__all__'
        model = models.Comment
