from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext as _


class CategoriesAppHook(CMSApp):
    name = _("Categories")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["apps.articles.urls"]


apphook_pool.register(CategoriesAppHook)
