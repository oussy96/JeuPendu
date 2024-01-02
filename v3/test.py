import os

DIFFICULTE = {
    "facile" : {
        "id" : 1, "nb_erreurs" : 10, "pendu" : "pendu_facile.txt"
    },
    "normal" : {
        "id" : 2, "nb_erreurs" : 7, "pendu" : "pendu_moyen.txt"
    },
    "difficile" : {
        "id" : 3, "nb_erreurs" : 5, "pendu" : "pendu_difficile.txt"
    }
}

def lire_fichier_pendu(chemin_fichier):
    try:
        # Ouvrir le fichier en mode lecture
        with open(chemin_fichier, 'r') as fichier:
            # Lire le contenu du fichier
            contenu = fichier.read().split(',')

        # Afficher le contenu
        print("Contenu du fichier:")
        print(contenu[0])

    except FileNotFoundError:
        print(f"Le fichier {chemin_fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

lire_fichier_pendu("jeu_de_pendu/v3/pendu_facile.txt")


"""for index in range(len(DIFFICULTE)):
    print(f"{index + 1} - {list(DIFFICULTE.keys())[index]}")

# choix = input("Votre choix : ")

print(list(DIFFICULTE.values())[0].get("id"))"""