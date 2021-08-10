import uuid
from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

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


class Quiz(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(
        max_length=250, unique_for_date="published", null=True)
    published = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    # UUID Overflow bug using tags https://github.com/jazzband/django-taggit/issues/679

    objects = models.Manager()  # The default manager.
    published_mng = PublishedManager()  # Our custom manager.
    tags = TaggableManager(through=UUIDTaggedItem)  # Tagging

    class Meta:
        default_manager_name = 'published_mng'
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quiz', args=[str(self.id)])


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
