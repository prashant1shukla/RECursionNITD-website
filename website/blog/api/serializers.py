from blog.models import Posts,Tags
from rest_framework import serializers
from user_profile.api.serializers import UserSerializer


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

