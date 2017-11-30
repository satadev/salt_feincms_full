from elephantblog.models import Entry
from haystack import indexes
from feincms.module.page.models import Page


class PageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Page

    def index_queryset(self, using=None):
        return self.get_model().objects.active()


class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Entry

    def index_queryset(self, using=None):
        return self.get_model().objects.active()
