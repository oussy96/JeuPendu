import os
from random import randint

def dessin_pendu(pendu_parts, erreurs):
    if erreurs < len(pendu_parts) - 1:
        return pendu_parts[erreurs+1]
    return None


def lire_fichier_pendu(chemin_fichier):
    try:
        with open(chemin_fichier, 'r') as fichier:
            contenu = fichier.read().split(',')
        return contenu
    except FileNotFoundError:
        print(f"Le fichier {chemin_fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


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
    return choix in dictionnaire


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
        print("Vous devez choisir une (seule) lettre de l'alphabet")
        return choisir_lettre(list_lettre_histo, liste_mot_cache)
    elif choix_lettre in list_lettre_histo: 
        print('Lettre déjà choisie')
        return choisir_lettre(list_lettre_histo, liste_mot_cache)
    return choix_lettre


def chercher_mot(mot_secret, niveau, pendu):
    liste_mot_cache = list(init_mot_cache(mot_secret))
    lettre_historique = []
    gagner = False
    print(len(pendu))
    erreurs = len(pendu) - niveau.get("nb_erreurs")
    while not gagner and erreurs < len(pendu) - 1:
        choix_lettre = choisir_lettre(lettre_historique, liste_mot_cache)
        lettre_historique.append(choix_lettre)
        indices = afficher_lettre_indice(mot_secret, choix_lettre)
        if not indices:
            dessin = dessin_pendu(pendu, erreurs)
            erreurs += 1
            if not dessin:
                break
            print(dessin)
            continue
        for i in indices:
            liste_mot_cache[i] = choix_lettre
        if ''.join(liste_mot_cache) == mot_secret:
            gagner = True
    return gagner


mots = ['football', 'jouer', 'manger', 'france', 'adoption', 'organiser', 'apprendre', 'carotte', 'passion', 'incendie', 'chameaux']

DIFFICULTE = {
    "facile" : {
        "id" : 1, "nb_erreurs" : 10, "pendu" : os.path.join("jeu_de_pendu", "v3", "pendu_facile.txt")
    },
    "normal" : {
        "id" : 2, "nb_erreurs" : 7, "pendu" : os.path.join("jeu_de_pendu", "v3", "pendu_moyen.txt")
    },
    "difficile" : {
        "id" : 3, "nb_erreurs" : 4, "pendu" : os.path.join("jeu_de_pendu", "v3", "pendu_difficile.txt")
    }
}

if __name__ == '__main__':
    mot_secret = choisir_mot_secret(mots)
    niveau = choisir_difficulte(DIFFICULTE)
    pendu_parts = lire_fichier_pendu(niveau.get("pendu"))
    if chercher_mot(mot_secret, niveau, pendu_parts):
        print("Bravo !\nVous avez trouver le mot : {} ! ".format(mot_secret))
    else:
        print("Perdu...\n Le mot secret était : {} ".format(mot_secret))