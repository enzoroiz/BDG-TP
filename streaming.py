# -*- coding: utf-8 -*-
import sys
import os

import tweepy

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TP.settings')

import django
django.setup()

from coxinhaoupetralha.models import Tweet, TweetInstance, Tweets
from django.db import IntegrityError

consumer_key = 'PNQMmk6tDho0GE3zB24xmm5xh'
consumer_secret = '4eUbqYAzW0KYcnHhNKkKWDRpFlu7UXJXXFdwZZkEg1HxaXQ2o8'
access_token = '88196587-65q0xUVRMeL3xFXjvZzRLiJ3bLOk8aTXFXJWeZtDE'
access_token_secret = '14XD2DqWFcnvSq2smnXKdaWQGhqfRQt24eUmRVtvKMUBI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        def save_tweet(status, is_Petralha, is_Potential):
            if is_Potential:
                tweet = Tweets()
                tweet.text = status.text.encode('utf-8')
                tweet.lat = status.geo['coordinates'][0]
                tweet.lng = status.geo['coordinates'][1]
                tweet.save()
                print "ADDED POTENTIAL"
            else:
                try:
                    tweet = Tweet()
                    tweet.is_Petralha = is_Petralha
                    tweet.text = status.text.encode('utf-8')
                    tweet.lat = status.geo['coordinates'][0]
                    tweet.lng = status.geo['coordinates'][1]
                    tweet.save()
                    print "ADDED"
                except IntegrityError as e:
                    print e.message

        def getTweetInstance():
            if TweetInstance.objects.all().count() > 0:
                tweet_instance = TweetInstance.objects.last()
            else:
                try:
                    tweet_instance = TweetInstance()
                    tweet_instance.geo = 0
                    tweet_instance.potential = 0
                    tweet_instance.total = 0
                    tweet_instance.save()
                except IntegrityError as e:
                    print e.message

            return tweet_instance

        coxinha_words = ['AvanteTemer', 'ForaDilma', 'petralha', 'ForaLula', 'TchauQuerida', 'Petista', 'Esquerdista']
        petralha_words = ['NãoVaiTerGolpe', 'ForaTemer', 'GloboGolpista', 'DilmaFica', 'FicaDilma', 'TemerJamais', 'VoltaDilma', 'VaiTerLuta', 'Golpista']
        potential_words = ['stf', 'governo', 'democracia', 'político', 'política', 'Petrobras', 'Petrobrás', 'operação','Corrupção', 'Corrupto', 'Jucá', 'cpiminc', 'Esquerda', 'Sarney', 'Dilma', 'Lula', 'Temer', 'Cunha', 'Aécio', 'Moro', 'Coxinha', 'PT', 'PMDB', 'Lava-Jato', 'Golpe', 'Oposição', 'Impeachment', 'Ministério da Cultura', 'minc']
        tweet_instance = getTweetInstance()

        tweet_instance.total= tweet_instance.total + 1

        if status.geo != None:
            tweet_instance.geo = tweet_instance.geo + 1
            print "Tweet:", status.text.encode('utf8')
            print "Geo:", status.geo['coordinates']

            if any(word in status.text.encode('utf-8') for word in coxinha_words):
                save_tweet(status, False, False)
                print "Coxinha"
                print "//////////////////"

            elif any(word in status.text.encode('utf-8') for word in petralha_words):
                save_tweet(status, True, False)
                print "Petralha"
                print "//////////////////"
            elif any(word in status.text.encode('utf-8') for word in potential_words):
                save_tweet(status, True, True)
                tweet_instance.potential = tweet_instance.potential + 1
                print "Potencial"
                print "//////////////////"
            else:
                print "Not about Brazil."

        tweet_instance.save()

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener())
streaming_api.filter(locations=[-44.052429, -19.986255, -43.867035, -19.791257])

print 'Ending'