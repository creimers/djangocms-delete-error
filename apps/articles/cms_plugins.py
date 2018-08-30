from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from apps.articles.models import Category, CategoryPluginModel


class CategoriesPlugin(CMSPluginBase):
    name = "Kategorien-Liste"
    render_template = "articles/plugin.html"
    model = CategoryPluginModel

    def render(self, context, instance, placeholder):
        context = super(CategoriesPlugin, self).render(context, instance, placeholder)
        all_categories = Category.objects.all()
        context["categories"] = all_categories[:instance.number_to_show]
        context["show_more"] = len(all_categories) > instance.number_to_show
        print(context)
        return context


plugin_pool.register_plugin(CategoriesPlugin)
