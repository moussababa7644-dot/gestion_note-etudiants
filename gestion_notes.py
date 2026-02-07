# gestion_notes.py
# Projet Gestion de notes d'étudiants

etudiants = {}

def ajouter_etudiant(nom):
    if nom in etudiants:
        print("L'étudiant existe déjà.")
    else:
        etudiants[nom] = []
        print(f"{nom} ajouté avec succès.")

def ajouter_note(nom, note):
    if nom in etudiants:
        etudiants[nom].append(note)
        print("Note ajoutée.")
    else:
        print("Étudiant introuvable.")

def afficher_moyenne(nom):
    if nom in etudiants:
        if len(etudiants[nom]) > 0:
            moyenne = sum(etudiants[nom]) / len(etudiants[nom])
            print(f"Moyenne de {nom} : {moyenne:.2f}")
        else:
            print("Aucune note.")
    else:
        print("Étudiant introuvable.")

# Menu principal
while True:
    print("\n1. Ajouter étudiant")
    print("2. Ajouter note")
    print("3. Afficher moyenne")
    print("4. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        nom = input("Nom de l'étudiant : ").strip().upper()
        ajouter_etudiant(nom)

    elif choix == "2":
        nom = input("Nom de l'étudiant : ").strip().upper()
        try:
            note = float(input("Note (nombre) : "))
            ajouter_note(nom, note)
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")

    elif choix == "3":
        nom = input("Nom de l'étudiant : ").strip().upper()
        afficher_moyenne(nom)

    elif choix == "4":
        print("Au revoir 👋")
        break

    else:
        print("Choix invalide.")
