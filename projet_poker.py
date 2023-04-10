import random

# Initialisation du paquet de cartes
cartes = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Cartes correspondant à des numéros
paquet = cartes * 3  # 3 exemplaires de chaque carte
random.shuffle(paquet)  # Mélange du paquet

# Initialisation des fonds des joueurs
fonds_joueur = 100
fonds_ia = 100

# Fonction pour afficher les cartes d'un joueur
def afficher_cartes(nom, cartes):
    print(nom, ":", cartes)

# Fonction pour calculer la meilleure combinaison de cartes
def calculer_combinaison(cartes):
    # Tri des cartes pour faciliter la vérification des combinaisons
    cartes.sort()
    # Vérification de la combinaison "deux fois le même chiffre"
    for i in range(2):
        if cartes[i] == cartes[i+1]:
            return "Deux fois le même chiffre", cartes[i]
    # Vérification de la combinaison "trois fois le même chiffre"
    if cartes[0] == cartes[2]:
        return "Trois fois le même chiffre", cartes[0]
    # Vérification de la combinaison "trois chiffres qui se suivent"
    if cartes[2] - cartes[0] == 2:
        return "Trois chiffres qui se suivent", cartes[1]
    # Si aucune combinaison n'est trouvée, on renvoie "Aucune combinaison"
    return "Aucune combinaison", None

# Début du jeu
while True:
    # Distribution des cartes
    cartes_joueur = paquet[:3]
    cartes_ia = paquet[3:6]

    # Affichage des cartes du joueur et de l'IA
    afficher_cartes("Vos cartes", cartes_joueur)
    afficher_cartes("Cartes de l'IA", cartes_ia)

    # Phase de mise du joueur
    mise_joueur = 0
    while True:
        mise_joueur = int(input("Entrez votre mise (0 pour passer) : "))
        if mise_joueur <= fonds_joueur:
            fonds_joueur -= mise_joueur
            break
        else:
            print("Mise invalide. Fond insuffisant.")

    # Phase de mise de l'IA (aléatoire)
    mise_ia = random.randint(0, fonds_ia)
    fonds_ia -= mise_ia

    # Affichage des mises
    print("Votre mise :", mise_joueur)
    print("Mise de l'IA :", mise_ia)

    # Phase de révélation des cartes
    combinaison_joueur, valeur_joueur = calculer_combinaison(cartes_joueur)
    combinaison_ia, valeur_ia = calculer_combinaison(cartes_ia)

    # Affichage des combinaisons
    print("Votre combinaison :", combinaison_joueur, valeur_joueur)
    print("Combinaison de l'IA :", combinaison_ia, valeur_ia)

        # Comparaison des combinaisons pour déterminer le gagnant
    if combinaison_joueur == combinaison_ia:
        if valeur_joueur == valeur_ia:
            print("Égalité ! Les mises sont remboursées.")
            fonds_joueur += mise_joueur
            fonds_ia += mise_ia
        elif valeur_joueur > valeur_ia:
            print("Vous avez gagné ! Vous remportez les mises.")
            fonds_joueur += mise_joueur + mise_ia
        else:
            print("L'IA a gagné ! Vous perdez les mises.")
            fonds_ia += mise_joueur + mise_ia
    elif combinaison_joueur == "Aucune combinaison":
        print("Vous avez perdu ! Vous perdez les mises.")
        fonds_ia += mise_joueur + mise_ia
    elif combinaison_ia == "Aucune combinaison":
        print("L'IA a perdu ! Vous remportez les mises.")
        fonds_joueur += mise_joueur + mise_ia
    else:
        print("Erreur de comparaison de combinaisons.")

    # Affichage des fonds des joueurs
    print("Vos fonds :", fonds_joueur)
    print("Fonds de l'IA :", fonds_ia)

    # Vérification de la fin du jeu
    if fonds_joueur <= 0:
        print("Vous êtes à court de jetons. Fin du jeu.")
        break
    elif fonds_ia <= 0:
        print("L'IA est à court de jetons. Vous avez gagné ! Fin du jeu.")
        break

    # Demande si le joueur souhaite continuer à jouer
    continuer = input("Voulez-vous continuer à jouer ? (Oui/Non) : ")
    if continuer.lower() != "oui":
        print("Fin du jeu.")
        break

