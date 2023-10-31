from rest_framework import serializers

from .models import Announcement, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Announcement
