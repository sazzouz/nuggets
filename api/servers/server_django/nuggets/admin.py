from django.contrib import admin
from .models import Quiz, Comment


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published', 'status')
    list_filter = ('status', 'created', 'published', 'status')
    search_fields = ('title', 'description')
    date_hierarchy = 'published'
    readonly_fields = ('id',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', '-published')

    # https://stackoverflow.com/questions/14562943/make-the-prepopulated-slug-field-as-readonly-in-django-admin
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.is_superuser:
            return readonly_fields
        return list(readonly_fields) + ['slug', ]

    def get_prepopulated_fields(self, request, obj=None):
        prepopulated_fields = super().get_prepopulated_fields(request, obj)
        if request.user.is_superuser:
            return prepopulated_fields
        else:
            return {}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'quiz', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
