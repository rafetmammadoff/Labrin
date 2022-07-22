from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from student.models import Blog,Videos, Country, Service, News, Review, Event, Exhibitions, EducationCategory, Education


class BaseIndexSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'
    # changefreq = "monthly"

    def items(self):
        return ['index']

    def location(self, obj):
        return reverse(obj)


class AboutPageSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'

    def items(self):
        return ['about-us']

    def location(self, obj):
        return reverse(obj)


class CountryDetailSitemap(Sitemap):
    priority = '0.9'
    protocol = 'https'

    def items(self):
        return Country.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class ServicesListSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'

    def items(self):
        return ['service-list']

    def location(self, obj):
        return reverse(obj)


class ServicesDetailSitemap(Sitemap):
    priority = '0.9'
    protocol = 'https'

    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class NewsListSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'

    def items(self):
        return ['news-list']

    def location(self, obj):
        return reverse(obj)


class NewsDetailSitemap(Sitemap):
    priority = '0.9'
    protocol = 'https'

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class BlogListSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'

    def items(self):
        return ['blog-list']

    def location(self, obj):
        return reverse(obj)


class BlogDetailSitemap(Sitemap):
    priority = '0.9'
    protocol = 'https'

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class VideoListSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'

    def items(self):
        return ['video-list']

    def location(self, obj):
        return reverse(obj)


class VideoDetailSitemap(Sitemap):
    priority = '0.9'
    protocol = 'https'

    def items(self):
        return Videos.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class ReviewListSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'

    def items(self):
        return ['review-list']

    def location(self, obj):
        return reverse(obj)


class ReviewDetailSitemap(Sitemap):
    priority = '0.9'
    protocol = 'https'

    def items(self):
        return Review.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class EventListSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'

    def items(self):
        return ['event-list']

    def location(self, obj):
        return reverse(obj)


class EventDetailSitemap(Sitemap):
    priority = '0.9'
    protocol = 'https'

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class ReserveDateSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'

    def items(self):
        return ['reserve-date']

    def location(self, obj):
        return reverse(obj)


class UniversityDetailSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'

    def items(self):
        return Education.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class ProgramsListSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'

    def items(self):
        return ['program-list']

    def location(self, obj):
        return reverse(obj)


class ExhibitionDetailSitemap(Sitemap):
    priority = '0.9'
    protocol = 'https'

    def items(self):
        return Exhibitions.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class InsuranceSitemap(Sitemap):
    priority = '1.0'
    protocol = 'https'

    def items(self):
        return ['insurance']

    def location(self, obj):
        return reverse(obj)


class EducationCategoryListSitemap(Sitemap):
    priority = '0.9'
    protocol = 'https'

    def items(self):
        return EducationCategory.objects.all()

    def lastmod(self, obj):
        return obj.updated_at