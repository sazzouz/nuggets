import uuid
from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
from django.contrib.auth import get_user_model
from django.conf import settings
from django.template.defaultfilters import truncatechars

""" Managers """


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


""" Models """


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Topic(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    LEVEL_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.ManyToManyField(
        Topic, help_text="Select a topic for this quiz")
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(
        max_length=250, unique_for_date="published", null=True)
    published = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    level = models.CharField(
        max_length=20, choices=LEVEL_CHOICES, null=True)
    # UUID Overflow bug using tags https://github.com/jazzband/django-taggit/issues/679

    objects = models.Manager()  # The default manager.
    published_mng = PublishedManager()  # Our custom manager.
    tags = TaggableManager(through=UUIDTaggedItem)  # Tagging
    metadata = models.JSONField(blank=True, null=True, default=dict)

    @property
    def topics(self):
        return ", ".join([str(p) for p in self.topic.all()])

    @property
    def short_description(self):
        return truncatechars(self.description, 200)

    class Meta:
        default_manager_name = 'published_mng'
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quiz', args=[str(self.id)])


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=200)
    answers = models.JSONField(null=True)


class QuizAttempt(models.Model):
    STATUS_CHOICES = (
        ('in-progress', 'In Progress'),
        ('complete', 'Complete'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='attempts')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)
    answers = models.JSONField(blank=True, null=True, default=dict)
    started = models.DateTimeField(null=True, auto_now_add=True)
    finished = models.DateTimeField(null=True)

    @property
    def score(self):
        return str(self.answers)

    def __str__(self):
        return f"{self.user}'s attempt of: {self.quiz.title}"


class Comment(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, null=True)
    email = models.EmailField(null=True)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.quiz}'
