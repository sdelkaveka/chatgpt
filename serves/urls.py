from django.urls import path  # include
from .views import vk_ad, ok_ad

urlpatterns = [
    path('vk', vk_ad,),
    path('ok', ok_ad,),
]
