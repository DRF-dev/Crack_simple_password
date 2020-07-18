#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
import string


mdp = input("Insérer ici un mot de passe à cracker : ")


def alea():
    # On prend toutes les lettres disponible minucule et majuscule
    letters = string.ascii_letters
    caract_suivant = ""
    result = ""
    for i in range(len(mdp)):
        while mdp[i] != caract_suivant:
            print(result+caract_suivant)
            caract_suivant = random.choice(letters)
        result += caract_suivant
    return result

debut_crack = time.time()
res = alea()
print("Mot de passe trouvé : ", res, " trouvé en ", time.time()-debut_crack," secondes")

