from django.contrib import admin
from models import Tweet, TweetInstance, Tweets
# Register your models here.
admin.site.register(Tweet)
admin.site.register(Tweets)
admin.site.register(TweetInstance)