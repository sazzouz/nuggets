from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from nuggets import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description'
        )
        model = models.Quiz


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Question


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
