#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tweepy
import time
from datetime import datetime

# añade las credenciales de tu aplicación de twitter
# como cadenas de texto
CONSUMER_KEY =  ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# autentica las credenciales
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# crea un cliente de twiter
t = tweepy.API(auth)

# vamos a buscar mensajes de la Superbowl
query = "superbowl"
# creamos una pequeña batera de mensajes recogidos, para evitar duplicados
messages = {}

# el proceso termina a las 8:00 del 6/02/2017
stop = datetime(2017, 2, 6, 8, 0, 0)

# abrimos un fichero de escritura para ir guardando los tweets
with open('twitter-messages.txt', 'w') as outfile:
    i = 1
    while datetime.now() < stop:
        print('.', end='', flush=True) # cutre-barra de progreso
        results = t.search(q=query, result_type="recent", include_entities=True, lang="en")
        for r in results:
            if r.id_str not in messages:
                messages[r.id_str] = r.text
                outfile.write('%s\t%s\t%s\t%s\n' % (r.id_str, r.created_at, r.user.screen_name, r.text))
                outfile.flush()
        
        if i % 100 == 0:
            print(' ', len(messages.keys()), 'mensajes', flush=True)
        i += 1
        time.sleep(60) # descansa 1 minuto
        
