from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Announcement, Post
from .serializers import AnnouncementSerializer, PostSerializer


class AnnouncementViewSet(
    GenericViewSet,
    CreateModelMixin
):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()


class PostViewSet(
    GenericViewSet,
    CreateModelMixin
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
