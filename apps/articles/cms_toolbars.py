from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool


@toolbar_pool.register
class CategoryToolbar(CMSToolbar):

    def populate(self):
        category_menu = self.toolbar.get_or_create_menu(
            'categories',
            _('Categories')
        )

        url = reverse('admin:articles_category_changelist')
        category_menu.add_modal_item(_('Categories'), url=url)

        url = reverse('admin:articles_category_add')
        category_menu.add_modal_item(_('Add Category'), url=url)


@toolbar_pool.register
class ArticleToolbar(CMSToolbar):

    def populate(self):
        article_menu = self.toolbar.get_or_create_menu(
            'articles',
            _('Articles')
        )

        url = reverse('admin:articles_article_changelist')
        article_menu.add_modal_item(_('Articles'), url=url)

        url = reverse('admin:articles_article_add')
        article_menu.add_modal_item(_('Add Article'), url=url)