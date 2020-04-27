from rest_framework import serializers
from pins.models import pin, categoryType, upVoteStory, flagStory, commentStory, aboutUs, Faq, photo, FlagComment
from django_restql.mixins import DynamicFieldsMixin
from django.contrib.auth.models import User
import datetime
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from rest_framework.fields import ListField


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categoryType
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = aboutUs
        fields = '__all__'


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'


class upVoteStorySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = upVoteStory
        fields = '__all__'


class FlagStorySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = flagStory
        fields = '__all__'


class FlagCommentSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = FlagComment
        fields = '__all__'


class CommentStorySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    username = serializers.CharField(
        source="commenter.username", read_only=True)
    flaggingComment = FlagCommentSerializer(many=True, read_only=True)
    flagscore = serializers.IntegerField(read_only=True)

    class Meta:
        model = commentStory
        fields = '__all__'

class StringListField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        return ' '.join(data.values_list('name', flat=True))

# class TagSerializer(serializers.ModelSerializer):
#     tags = serializers.SlugRelatedField(
#         many=True,
#         read_only=True,
#         slug_field='name'
#     )




#     class Meta:
#         model = Tag
#         fields = '__all__'

# class StringArrayField(ListField):
#     """
#     String representation of an array field.
#     """
#     def to_representation(self, obj):
#         obj = super().to_representation(self, obj)
#         # convert list to string
#         return ",".join([str(element) for element in obj])

#     def to_internal_value(self, data):
#         data = data.split(",")  # convert string to list
#         return super().to_internal_value(self, data)

# class StringArrayField(ListField):
#     """
#     String representation of an array field.
#     """
#     def to_representation(self, obj):
#         obj = super().to_representation(obj)
#         # convert list to string
#         return ",".join([str(element) for element in obj])
        
#     def to_internal_value(self, data):
#         data = data.split(",") 
#         # convert string to list
# #         return super().to_internal_value(self, data)
# class StringArrayField(ListField):
#     def to_representation(self, obj):
#         obj = super().to_representation(obj)
#         return ",".join([str(element) for element in obj])
    # def to_internal_value(self, data):
    #     data = data.split(",")
    #     return super().to_internal_value(self, data)

class PinSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
  #  updoot = serializers.IntegerField()

    username = serializers.CharField(
        source="owner.username", read_only=True)
    categoryName = serializers.CharField(
        source="category.categoryName", read_only=True)
    categoryImage = serializers.ImageField(
        source="category.image_url",
        read_only=True)
    # pinsUpvote = serializers.StringRelatedField(many=True)
    # pinsUpvote = upVoteStorySerializer(many=True, read_only=True)
    # pinsUpvoted = upVoteStorySerializer(many=True, read_only=True)
    updooots = serializers.IntegerField(read_only=True)
    flagscore = serializers.IntegerField(read_only=True)
    flaggerstory = FlagStorySerializer(many=True, read_only=True)
    updotes = upVoteStorySerializer(many=True, read_only=True)
    commentstory = CommentStorySerializer(many=True, read_only=True)
    tags = serializers.ListField(child=serializers.CharField())
    # tags = serializers.SlugRelatedField(
    #     many=True,
    #     queryset=Tag.objects.all(),
    #     slug_field='text'
    # )
    
    # def create(self, validated_data):
    #     tags = validated_data.pop('tags')
    #     instance = super(TagSerializer, self).create(validated_data)
    #     instance.tags.set(*tags)
    #     return instance

    class Meta:
        model = pin
        fields = '__all__'
    
    # def create(self, validated_data):
    #     tags = validated_data.pop('tags')
    #     instance = super(PinSerializer, self).create(validated_data)
    #     instance.tags.set(*tags)
    #     return instance

    # def update(self,instance, validated_data):
    #     tags = validated_data.pop('tags')
    #     pinInfo = pin.objects.update(**validated_data)
    #     for tag in tags:
    #         Tag.objects.update(pinInfo=pinInfo, **tags)
    #     return pinInfo

        


class PinFlaggedSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    username = serializers.CharField(
        source="owner.username", read_only=True)
    flagscore = serializers.IntegerField(read_only=True)
    flaggerstory = FlagStorySerializer(many=True, read_only=True)

    class Meta:
        model = pin
        fields = ['id', 'owner', 'title',
                  'username', 'flagscore', 'flaggerstory']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = '__all__'
