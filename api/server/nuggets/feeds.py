from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Quiz


class LatestQuizzesFeed(Feed):
    title = 'My blog'
    # Not going to work without typical list viewu unlike our use of home and search.
    # link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'

    def items(self):
        return Quiz.published_mng.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
