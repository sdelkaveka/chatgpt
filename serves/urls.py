from django.urls import path  # , include
from .views import (corrector, enhance, fairy_tale, inst_ad, inst_post, ok_ad,
                    ok_post, rewrite, shorten, site_keywords,
                    site_seo_optimization, structure_page, structure_site,
                    text_page, tg_ad, tg_post, url_generator, vk_ad, vk_post)

urlpatterns = [
    path('fairy_tale', fairy_tale),
    path('corrector', corrector),
    path('enhance', enhance),
    path('inst_ad', inst_ad),
    path('inst_post', inst_post),
    path('ok_ad', ok_ad),
    path('ok_post', ok_post),
    path('rewrite', rewrite),
    path('shorten', shorten),
    path('site_seo_optimization', site_seo_optimization),
    path('site_keywords', site_keywords),
    path('structure_site', structure_site),
    path('structure_page', structure_page),
    path('url_generator', url_generator),
    path('text_page', text_page),
    path('tg_ad', tg_ad),
    path('tg_post', tg_post),
    path('vk_ad', vk_ad),
    path('vk_post', vk_post),
]
