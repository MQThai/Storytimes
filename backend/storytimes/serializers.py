from rest_framework import serializers
from .models import Prompt, Post, Chapter, Comment

class PromptSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post-detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Prompt
        fields = ('id', 'author', 'body', 'post_date', 'posts',)

class PostSerializer(serializers.HyperlinkedModelSerializer):
    prompt = serializers.HyperlinkedRelatedField(
        view_name='prompt-detail',
        read_only=True
    )
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'body', 'post_date', 'prompt',)

class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post-detail',
        read_only=True
    )
    class Meta:
        model = Chapter
        fields = ('id', 'body', 'chapter', 'post_date', 'post',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post-detail',
        read_only=True
    )