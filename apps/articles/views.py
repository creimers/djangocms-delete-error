
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from apps.articles.models import Category, Article


class CategoryListView(ListView):
    template_name = "articles/category-listview.html"
    model = Category


class CategoryDetailView(DetailView):
    template_name = "articles/category-detailview.html"
    model = Category

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.all().prefetch_related("articles")


class ArticleDetailView(DetailView):
    template_name = "articles/article-detailview.html"
    model = Article

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get("article_slug", None)
        return get_object_or_404(Article, slug=slug)
