from django.urls import path
from rest_framework import routers
from .api import PinViewSet, CategoryViewSet, upVoteStoryViewSet, FlagStoryViewSet, CommentStoryViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/pins', PinViewSet, 'pin')
# router.register('api/category', CategoryViewSet, 'category')
router.register('api/category', CategoryViewSet, 'category')
router.register('api/upVoteStory', upVoteStoryViewSet, 'upvotestory')
router.register('api/flagStory', FlagStoryViewSet, 'flagstory')
router.register('api/commentStory', CommentStoryViewSet, 'commentstory')
urlpatterns = router.urls
