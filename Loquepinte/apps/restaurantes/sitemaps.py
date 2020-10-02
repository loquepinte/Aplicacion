from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return['index', 'principal', 'restaurante', 'el_patron', 'el_surtidor', 'la_chimenea', 'nanas', 'san_jose']
    
    def location(self, item):
        return reverse(item)