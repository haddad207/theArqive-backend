from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class pin(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    category = models.ForeignKey(
        "categoryType", on_delete=models.CASCADE, null=True, related_name='selected_category')
    # 1 is community, 2: historical, 3: personal


class categoryType(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        """String for representing the Model object."""
        return self.categoryName


class upVoteStory(models.Model):
    pinId = models.ForeignKey(
        "pin", on_delete=models.CASCADE, null=True)
    upVoter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    upvote = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['pinId', 'upVoter'], name="upvoter-pin")
        ]


class flagStory(models.Model):
    pinId = models.ForeignKey(
        "pin", on_delete=models.CASCADE, null=True)
    flagger = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    flagged = models.BooleanField(default=False)


class countUpvoteFlag(models.Model):
    pinId = models.ForeignKey(
        "pin", on_delete=models.CASCADE, null=True)
    upVotes = models.PositiveSmallIntegerField(default=0)
    flags = models.PositiveSmallIntegerField(default=0)
