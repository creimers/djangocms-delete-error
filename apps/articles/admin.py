from django.contrib import admin
from adminsortable.admin import SortableAdmin
# from django.utils.translation import ugettext_lazy as _

from apps.articles.models import Article, Category


class ArticleAdmin(SortableAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "category"]


admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(SortableAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def get_sort_view_queryset(self, request, sortable_by_expression):
        return self.get_queryset(request)


admin.site.register(Category, CategoryAdmin)