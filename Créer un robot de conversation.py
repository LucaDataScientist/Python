#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:23:17 2020

@author: simplon
"""

import random

liste_depart = ['Comment allez-vous ?', 'Pourquoi venez-vous me voir ?', 
                'Comment s’est passée votre journée ?']

keywords = ["travail", "data", "développeur", "graphique", "cluster", "RGBD", "CNIL", "sécurité"]
keyword = []

relance = ['Je sais pas', 'Peut etre', 'Devine']

liste_interrogation = ['Pourquoi me posez-vous cette question ?',
                       'Oseriez-vous poser cette question à un humain ?', 
                       'Je ne peux malheureusement pas répondre à cette question.']                   

liste_vague = ["J'entends bien.", 'Je sens une pointe de regret.', 
               'Est-ce une bonne nouvelle ?', 'Oui, c’est ça le problème.', 
               'Pensez-vous ce que vous dites ?', 'Hum... Il se peut.']


liste_fin=['marre', 'au revoir' , 'à bientôt']
salutations=["au revoir, merci pour votre utilisation", "hasta luego"]

interrupteur = True           
reponse = input(random.choice(liste_depart))

while interrupteur == True:
    keyword=[m for m in reponse.split(' ') if (m.lower() in keywords) or (m=='?') or ( m.lower() in liste_interrogation) or (m.lower() in liste_vague) or (m.lower() in liste_fin) or (m.lower() in keywords )]
    print(keyword)
    if not keyword:
        reponse = input(random.choice(relance))
        
    elif keyword[0] in keywords:
        liste_reponse = ['Sur quoi travaillez-vous dernièrement votre {0} ?'.format(keyword[0]), 'Que pensez-vous des {0} ?'.format(keyword[0]), 'Avez-vous rassemblez les {0} ?'.format(keyword[0])]
        reponse = input(random.choice(liste_reponse))
        
    elif keyword[0] in keywords:
         liste_réponses=['le {keyword} avance bien?', 'la relation avec les {keyword} vous pose t"elle problème ?', 'pourquoi penser vous en ce moment à votre {keyword}?']

    elif keyword[0]=='?':
        reponse = input(random.choice(liste_interrogation))

    elif keyword[0] in liste_vague:
         reponse=input(random.choice(liste_vague))

    elif  keyword[0] in liste_fin:
        interrupteur=False

print(random.choice(salutations))