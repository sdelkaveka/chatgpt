from django.urls import path  # , include

from .views import (fairy_tales, fix, improve, inst, inst_post, ok_ad, ok_post,
                    rewrite, short, site_ceo, site_keywords, site_struct,
                    site_struct_page, site_url, text_struct, tg, tg_post,
                    translate, vk_ad, vk_post)

urlpatterns = [
    path('fairy_tales', fairy_tales),
    path('fix', fix),
    path('improve', improve),
    path('inst', inst),
    path('inst_post', inst_post),
    path('ok_ad', ok_ad),
    path('ok_post', ok_post),
    path('rewrite', rewrite),
    path('short', short),
    path('site_ceo', site_ceo),
    path('site_keywords', site_keywords),
    path('site_struct', site_struct),
    path('site_struct_page', site_struct_page),
    path('site_url', site_url),
    path('text_struct', text_struct),
    path('tg', tg),
    path('tg_post', tg_post),
    path('translate', translate),
    path('vk_ad', vk_ad),
    path('vk_post', vk_post),
]
