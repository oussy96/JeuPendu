from random import randint

def dessin_pendu(pendu_parts, erreurs):
    return ''.join(pendu_parts[:erreurs+1])


def choisir_mot_secret(liste_mots):
    return liste_mots[randint(0, len(liste_mots) - 1)]


def init_mot_cache(mot):
    return '_'*len(mot)


def afficher_lettre_indice(mot, lettre):
    indices = []
    liste_mot = list(mot)
    for i in range(len(liste_mot)):
        if liste_mot[i] == lettre:
            indices.append(i)
    return indices if indices else None


def choisir_lettre(list_lettre_histo, liste_mot_cache):
    print(f"\n{''.join(liste_mot_cache)}\n")
    choix_lettre = input("Veuillez choisir une lettre :")
    if choix_lettre.isdigit():
        print("Vous devez choisir une lettre de l'alphabet")
        return choisir_lettre(list_lettre_histo, liste_mot_cache)
    if choix_lettre == '' or len(choix_lettre) > 1:
        print("Vous devez choisir une seule lettre")
        return choisir_lettre(list_lettre_histo, liste_mot_cache)
    if choix_lettre in list_lettre_histo:
        print('Lettre déjà choisie')
        return choisir_lettre(list_lettre_histo, liste_mot_cache)
    return choix_lettre


def chercher_mot(mot_secret, pendu):
    liste_mot_cache = list(init_mot_cache(mot_secret))
    lettre_historique = []
    gagner = False
    erreurs = 0
    while not gagner and erreurs < len(pendu) - 1 :
        choix_lettre = choisir_lettre(lettre_historique, liste_mot_cache)
        lettre_historique.append(choix_lettre)
        indices = afficher_lettre_indice(mot_secret, choix_lettre)
        if indices == None:
            erreurs += 1
            print(dessin_pendu(pendu, erreurs))
            continue
        for i in indices:
            liste_mot_cache[i] = choix_lettre
        if ''.join(liste_mot_cache) == mot_secret:
            gagner = True
    return gagner


pendu_parts = [
        '''
        -
        '''
        ,
        '''
        |    
        |
        |
        |
        -
        '''
        ,
        '''
        ------
        |    
        |
        |
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |
        |
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |    |
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |   /|
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |   /|\\
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |   /|\\
        |   /
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        -
        '''
    ]
mots = ['football', 'jouer', 'manger', 'france', 'adoption', 'organiser', 'apprendre', 'carotte', 'passion', 'incendie', 'chameaux']

if __name__ == '__main__':
    mot_secret = choisir_mot_secret(mots)
    if chercher_mot(mot_secret, pendu_parts):
        print("Bravo, vous avez trouver le mot : {} ! ".format(mot_secret))
    else:
        print("Dommage... \n Le mot secret était : {} ".format(mot_secret))