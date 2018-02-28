from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from . import models
from nomadgram.users import models as user_models

class SmallImageSerializer(serializers.ModelSerializer):
    
    """used for the notifications"""

    class Meta:
        model = models.Image
        fields = (
            'file',
        )

class CountImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comments_count',
            'likes_count'
        )
    
    
class LikeSerializer(serializers.ModelSerializer):

    #nestd Serialize

    class Meta:
        model = models.Like
        fields = '__all__'

class FeedUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image'
        )
        
class CommentSerializer(serializers.ModelSerializer):
    
    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator'
        )

class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'creator',
            'file',
            'caption',
            'location',
            'comments',
            'likes_count',
            'tags',
            'created_at'
        )


class InputImageSerializer(serializers.ModelSerializer):

    #필수항목 지정
    
    class Meta:
            model = models.Image
            fields =(
                'file',
                'location',
                'caption'
            )