from django.urls import path  # include

from .views import vk_ad

urlpatterns = [
    path('vk', vk_ad,)
    # path('', include()),
]
