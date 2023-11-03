from django.urls import path  # , include

from .views import ok_ad, tg_ad, vk_ad

urlpatterns = [
    path('vk', vk_ad,),
    path('ok', ok_ad,),
    path('tg', tg_ad,),
]
