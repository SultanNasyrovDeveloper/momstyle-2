from django.shortcuts import render
from django.views import generic

from seo.models import SitePageSeo

from . import  models


class AboutUsView(generic.TemplateView):

    page_name = 'О нас'
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo, _ = SitePageSeo.objects.get_or_create(page_name=self.page_name)
        context['page_seo'] = seo
        context['blocks'] = models.AboutUsBlock.objects.all()
        return context
