# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TP.settings')

import django
django.setup()

from coxinhaoupetralha.models import Tweets, Tweet
from django.db import IntegrityError

tweets = Tweets.objects.all()

for tweet in tweets:
    print tweet.text
    input = raw_input("Coxinha, Petralha ou Nenhum: ")
    while input != 'c' and input != 'p' and input != 'n' and input != 'd':
        print tweet.text
        input = raw_input("Coxinha, Petralha, Nenhum ou Decidir Depois: ")

    if input == 'c':
        try:
            status = Tweet()
            status.text = tweet.text
            status.lat = tweet.lat
            status.lng = tweet.lng
            status.is_Petralha = False
            status.save()
            print 'ADDED COXINHA'
        except IntegrityError as e:
            print e.message

        tweet.delete()

    if input == 'p':
        try:
            status = Tweet()
            status.text = tweet.text
            status.lat = tweet.lat
            status.lng = tweet.lng
            status.is_Petralha = True
            status.save()
            print 'ADDED PETRALHA'
        except IntegrityError as e:
            print e.message

        tweet.delete()

    if input == 'n':
        tweet.delete()

print 'End'