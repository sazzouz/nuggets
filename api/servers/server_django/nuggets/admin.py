from django.contrib import admin
from .models import Quiz

admin.site.register(Quiz)


class QuizAdmin(admin.ModelAdmin):
    ordering = ['pub_date']
    exclude = ('pub_date')
