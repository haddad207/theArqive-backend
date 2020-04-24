from django.urls import path
from rest_framework import routers
from .api import PinViewSet, CategoryViewSet, upVoteStoryViewSet, FlagStoryViewSet, CommentStoryViewSet, \
    PinSearchViewSet, FlagCommentViewSet, FaqViewSet, PhotoViewSet, PinFlaggedViewSet, PinCoordViewSet, MinPinDate, \
    MaxPinDate, TagViewSet
from . import views
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register('api/pins', PinViewSet, 'pin')
router.register('api/tags', TagViewSet, 'tags')
# router.register('api/category', CategoryViewSet, 'category')
router.register('api/category', CategoryViewSet, 'category')
router.register('api/upVoteStory', upVoteStoryViewSet, 'upvotestory')
router.register('api/flagStory', FlagStoryViewSet, 'flagstory')
router.register('api/commentStory', CommentStoryViewSet, 'commentstory')
router.register('api/pinSearch', PinSearchViewSet, 'pin')
router.register('api/minPinDate', MinPinDate, 'pin')
router.register('api/maxPinDate', MaxPinDate, 'pin')
router.register('api/pinCoordFilter', PinCoordViewSet, 'pin')
router.register('api/pinFlagged', PinFlaggedViewSet, 'pinFlag')
router.register('api/faq', FaqViewSet, 'faqModel')
router.register('api/flagcomment', FlagCommentViewSet, 'flagcomment')
router.register('api/photo', PhotoViewSet, 'photo')
# router.register('api/tags', views.setTags, 'tags')
# router.register('api/tags/get', views.getTags, 'get-tags')

# urlpatterns = [
#     url(r'^api/tags', views.setTags, name='set-tags'),
#     url(r'^api/tags/get', views.getTags, name='get-tags')
# ]

urlpatterns = router.urls
# urlpatterns = [
#     path('api/tags', views.setTags, name='tags')
# ]