import os
from random import randint

def menu_principal_choix_niveau(niveaux):
    print("***********************************")
    print("********** JEU DU PENDU ***********")
    print("***********************************")
    print()
    return choisir_difficulte(niveaux)


def rejouer_partie():
    choix_possible = ("o", "oui", "n", "non")
    rejouer = input("Voulez-vous rejouer ? ([o]ui ou [n]on) ").lower()
    print()
    if rejouer not in choix_possible:
        print(f"Veuillez choisir entre les options : {', '.join(choix_possible)}")
        return rejouer_partie()
    elif rejouer in choix_possible[:2]:
        return True
    return False


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


def choix_id(niveaux, choix):
    for valeur in niveaux.values():
        if valeur.get("id") == choix:
            return True
    print(f"Le numéro doit être compris entre 1 et {len(niveaux)} !")
    return False


def choix_niveau(niveaux, choix):
    if not choix in niveaux:
        print("Niveau inconnu !!!")
        return False
    return True


def choisir_difficulte(niveaux):
    choix = ''
    print("Veuillez choisir le niveau de difficulté\n(Ecrivez le NUMERO ou le NOM du niveau) :\n")
    for index in range(len(niveaux)):
        print(f"{index + 1} - {list(niveaux.keys())[index]}")
    choix = input("Votre choix : ").lower()
    if choix.isdigit() and choix_id(niveaux, int(choix)):
        print(f"\nVous avez choisi le mode {list(niveaux.keys())[int(choix) - 1].upper()}")
        print(f"Nombre de vies restantes : {list(niveaux.values())[int(choix) - 1].get("nb_erreurs")}")
        return list(niveaux.values())[int(choix) - 1]
    elif choix.isalpha() and choix_niveau(niveaux, choix):
        print(f"\nVous avez choisi le mode {choix.upper()}")
        print(f"Nombre de vies restantes : {niveaux.get(choix).get("nb_erreurs")}")
        return niveaux.get(choix)
    print()
    return choisir_difficulte(niveaux)


def choisir_lettre(list_lettre_histo, liste_mot_cache):
    print(f"\n{''.join(liste_mot_cache)}\n")
    choix_lettre = input("Veuillez choisir une lettre :").lower()
    print()
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
    erreurs = len(pendu) - niveau.get("nb_erreurs") - 1
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
        "id" : 1, "nb_erreurs" : 10, "pendu" : os.path.join("jeu_de_pendu", "pendu_facile.txt")
    },
    "normal" : {
        "id" : 2, "nb_erreurs" : 7, "pendu" : os.path.join("jeu_de_pendu", "pendu_moyen.txt")
    },
    "difficile" : {
        "id" : 3, "nb_erreurs" : 4, "pendu" : os.path.join("jeu_de_pendu", "pendu_difficile.txt")
    }
}

if __name__ == '__main__':
    while True:
        mot_secret = choisir_mot_secret(mots)
        niveau = menu_principal_choix_niveau(DIFFICULTE) 
        pendu_parts = lire_fichier_pendu(niveau.get("pendu"))
        if chercher_mot(mot_secret, niveau, pendu_parts):
            print("Bravo !\nVous avez trouver le mot : {} !\n".format(mot_secret))
        else:
            print("Perdu...\n Le mot secret était : {}\n".format(mot_secret))
        if not rejouer_partie():
            break
print("\nFIN DU JEU")