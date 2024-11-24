from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class PageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    #protocol = 'http'

    def items(self):
     return ['/']

    def location(self, item):
        return reverse(item)
