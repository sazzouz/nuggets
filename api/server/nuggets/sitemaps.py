from django.contrib.sitemaps import Sitemap
from .models import Quiz


class QuizSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Quiz.published_mng.all()

    def lastmod(self, obj):
        return obj.updated
