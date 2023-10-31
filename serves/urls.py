from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import AnnouncementViewSet, PostViewSet

router = SimpleRouter()
router.register(
    'announcement',
    AnnouncementViewSet
)
router.register(
    'posts',
    PostViewSet
)
urlpatterns = [
    path('', include(router.urls)),
]
