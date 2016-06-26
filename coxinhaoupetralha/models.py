from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tweet(models.Model):
    is_Petralha = models.BooleanField(blank=False)
    text = models.CharField(max_length=350, blank=False, unique=True)
    lat = models.DecimalField(max_digits=17, decimal_places=14, blank=False)
    lng = models.DecimalField(max_digits=17, decimal_places=14, blank=False)

    def __unicode__(self):
        return str(self.is_Petralha) + " " + self.text

# Create your models here.
class Tweets(models.Model):
    text = models.CharField(max_length=350, blank=False, unique=True)
    lat = models.DecimalField(max_digits=17, decimal_places=14, blank=False)
    lng = models.DecimalField(max_digits=17, decimal_places=14, blank=False)

    def __unicode__(self):
        return self.text


# Create your models here.
class TweetInstance(models.Model):
    total = models.IntegerField()
    geo = models.IntegerField()
    potential = models.IntegerField()

    def __unicode__(self):
        return str(self.total) + " - " + str(self.geo) + " - " + str(self.potential)