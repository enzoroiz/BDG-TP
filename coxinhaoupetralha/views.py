# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import tweepy
import keys, api_key
from models import Tweet, Tweets
from django.db import IntegrityError

def get_tweets(request):
    consumer_key = keys.CONSUMER_KEY
    consumer_secret = keys.CONSUMER_SECRET
    access_token = keys.ACCESS_TOKEN
    access_token_secret = keys.ACCESS_TOKEN_SECRET
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    coxinha_words = ['AvanteTemer', 'ForaDilma', 'petralha', 'ForaLula', 'TchauQuerida', 'Petista', 'Esquerdista']
    petralha_words = ['NãoVaiTerGolpe', 'ForaTemer', 'GloboGolpista', 'DilmaFica', 'FicaDilma', 'TemerJamais', 'VoltaDilma', 'VaiTerLuta', 'Golpista']
    #potential_words = ['Dilma', 'Lula', 'Temer', 'Cunha', 'Aécio', 'Moro', 'Golpe', 'Oposição', 'Impeachment', 'governo', 'democracia', 'político', 'política', 'operação', 'Corrupção', 'Corrupto', 'Jucá', 'cpiminc', 'Esquerda', 'Sarney']
    #potential_words = ['Comunista', 'Comuna', 'esquerdopata', 'Jucá', 'Direita', 'Ministro']
    #potential_words = ['Petralhas', 'PassaDilma', 'Protesto', 'Protestos', 'Ministros']

    # is_Petralha = False
    # for query in coxinha_words:
    #     for status in tweepy.Cursor(api.search, q=query + '&place:d9d978b087a92583').items():
    #
    #         if status.geo != None:
    #             print "Tweet:", status.text.encode('utf8')
    #             print "Geo:", status.geo['coordinates']
    #             print "//////////////////"
    #             try:
    #                 tweet = Tweet()
    #                 tweet.is_Petralha = is_Petralha
    #                 tweet.text = status.text.encode('utf-8')
    #                 tweet.lat = status.geo['coordinates'][0]
    #                 tweet.lng = status.geo['coordinates'][1]
    #                 tweet.save()
    #                 print "ADDED"
    #             except IntegrityError as e:
    #                 print e.message
    #
    is_Petralha = True
    for query in petralha_words:
        for status in tweepy.Cursor(api.search, q=query + '&place:d9d978b087a92583').items():

            if status.geo != None:
                print "Tweet:", status.text.encode('utf8')
                print "Geo:", status.geo['coordinates']
                print "//////////////////"
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
    #
    # for query in potential_words:
    #     for status in tweepy.Cursor(api.search, q=query + '&place:d9d978b087a92583').items():
    #
    #         if status.geo != None:
    #             print "Tweet:", status.text.encode('utf8')
    #             print "Geo:", status.geo['coordinates']
    #             print "//////////////////"
    #             try:
    #                 tweet = Tweets();
    #                 tweet.text = status.text.encode('utf-8')
    #                 tweet.lat = status.geo['coordinates'][0]
    #                 tweet.lng = status.geo['coordinates'][1]
    #                 tweet.save()
    #                 print "ADDED POTENTIAL"
    #             except IntegrityError as e:
    #                 print e.message

    print "That's end"

    return render(request, 'coxinhaoupetralha/index.html', {})

def index(request):
    context_dict = {}
    context_dict['API_KEY'] = api_key.API_KEY
    context_dict['petralhas'] = Tweet.objects.filter(is_Petralha=True)
    context_dict['coxinhas'] = Tweet.objects.filter(is_Petralha=False)
    print context_dict['petralhas'].count()
    print context_dict['coxinhas'].count()
    return render(request, 'coxinhaoupetralha/index.html', context_dict)