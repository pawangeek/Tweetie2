from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    handleid = models.BigIntegerField(null=False)
    name = models.CharField(max_length=200, null=False)


class Tweets(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=1000, null=False)

    tweetid = models.BigIntegerField(null=False)
    author = models.CharField(max_length=100, null=False)
    link = models.CharField(max_length=300, null=False)
    website = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(null=False)
    handle = models.BigIntegerField(null=False)
