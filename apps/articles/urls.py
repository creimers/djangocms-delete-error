from django.conf.urls import url

from apps.articles.views import CategoryListView, CategoryDetailView, ArticleDetailView

urlpatterns = [
    url(
        r'^$',
        CategoryListView.as_view(),
        name="category_list"
    ),
    url(
        r'^(?P<slug>[\w\.@+-]+)/$',
        CategoryDetailView.as_view(),
        name='category_detail'
    ),
    url(
        r'^(?P<category_slug>[\w\.@+-]+)/(?P<article_slug>[\w\.@+-]+)$',
        ArticleDetailView.as_view(),
        name='article_detail'
    ),
]