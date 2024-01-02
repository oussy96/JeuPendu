from random import randint

def dessin_pendu(pendu_parts, erreurs):
    if erreurs < len(pendu_parts) - 1:
        return pendu_parts[erreurs+1]
    return None


def choisir_mot_secret(liste_mots):
    return liste_mots[randint(0, len(liste_mots) - 1)]


def init_mot_cache(mot):
    return '_'*len(mot)


def afficher_lettre_indice(mot, lettre):
    return [i for i, char in enumerate(mot) if char == lettre]


def choix_id(dictionnaire, choix):
    for valeur in dictionnaire.values():
        if valeur.get("id") == choix:
            return True
    print(f"Le numéro doit être compris entre 1 et {len(dictionnaire)} !")
    return False


def choix_niveau(dictionnaire, choix):
    for cle in dictionnaire.keys():
        if cle == choix:
            return True
    print(f"Niveau inconnu !")
    return False


def choisir_difficulte(dictionnaire):
    choix = ''
    print("Veuillez choisir le niveau de difficulté (Ecrivez le numéro ou le nom du niveau) :")
    for index in range(len(dictionnaire)):
        print(f"{index + 1} - {list(dictionnaire.keys())[index]}")
    choix = input("Votre choix : ")
    if choix.isdigit() and choix_id(dictionnaire, int(choix)):
        return list(dictionnaire.values())[int(choix) - 1]
    elif choix.isalpha() and choix_niveau(dictionnaire, choix):
        return dictionnaire.get(choix)
    return choisir_difficulte(dictionnaire)


def choisir_lettre(list_lettre_histo, liste_mot_cache):
    print(f"\n{''.join(liste_mot_cache)}\n")
    choix_lettre = input("Veuillez choisir une lettre :").lower()
    if not choix_lettre.isalpha() or len(choix_lettre) != 1:
        print("Vous devez choisir une lettre de l'alphabet")
        return choisir_lettre(list_lettre_histo, liste_mot_cache)
    elif choix_lettre in list_lettre_histo: 
        print('Lettre déjà choisie')
        return choisir_lettre(list_lettre_histo, liste_mot_cache)
    return choix_lettre


def chercher_mot(mot_secret, niveau, pendu):
    liste_mot_cache = list(init_mot_cache(mot_secret))
    lettre_historique = []
    gagner = False
    erreurs = len(pendu) - niveau.get("nb_erreurs")
    while not gagner and erreurs < len(pendu) - 1:
        choix_lettre = choisir_lettre(lettre_historique, liste_mot_cache)
        lettre_historique.append(choix_lettre)
        indices = afficher_lettre_indice(mot_secret, choix_lettre)
        if not indices:
            erreurs += 1
            dessin = dessin_pendu(pendu, erreurs)
            if not dessin:
                break
            print(dessin)
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

DIFFICULTE = {
    "facile" : {
        "id" : 1, "nb_erreurs" : 10
    },
    "normal" : {
        "id" : 2, "nb_erreurs" : 7
    },
    "difficile" : {
        "id" : 3, "nb_erreurs" : 5
    }
}

if __name__ == '__main__':
    mot_secret = choisir_mot_secret(mots)
    niveau = choisir_difficulte(DIFFICULTE)
    if chercher_mot(mot_secret, niveau, pendu_parts):
        print("Bravo !\nVous avez trouver le mot : {} ! ".format(mot_secret))
    else:
        print("Dommage... \n Le mot secret était : {} ".format(mot_secret))