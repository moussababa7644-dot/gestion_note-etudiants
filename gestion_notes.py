# gestion_notes.py
# Gestion de notes d'étudiants avec sauvegarde JSON

import json
import os

FICHIER_DONNEES = "data.json"


def charger_donnees():
    """Charge les données depuis data.json si le fichier existe, sinon retourne un dict vide."""
    if not os.path.exists(FICHIER_DONNEES):
        return {}

    try:
        with open(FICHIER_DONNEES, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Sécurisation : s'assurer qu'on a bien dict[str, list[float]]
        etudiants = {}
        if isinstance(data, dict):
            for nom, notes in data.items():
                if isinstance(nom, str) and isinstance(notes, list):
                    cleaned_notes = []
                    for n in notes:
                        try:
                            cleaned_notes.append(float(n))
                        except (ValueError, TypeError):
                            pass
                    etudiants[nom.strip().upper()] = cleaned_notes
        return etudiants

    except (json.JSONDecodeError, OSError):
        print("⚠️ Attention : impossible de lire data.json (fichier vide ou corrompu).")
        return {}


def sauvegarder_donnees(etudiants):
    """Sauvegarde les données dans data.json."""
    try:
        with open(FICHIER_DONNEES, "w", encoding="utf-8") as f:
            json.dump(etudiants, f, ensure_ascii=False, indent=2)
    except OSError:
        print("⚠️ Erreur : impossible d'enregistrer les données.")


def normaliser_nom(nom):
    return nom.strip().upper()


def ajouter_etudiant(etudiants, nom):
    if nom in etudiants:
        print("L'étudiant existe déjà.")
        return

    etudiants[nom] = []
    sauvegarder_donnees(etudiants)
    print(f"{nom} ajouté avec succès.")


def ajouter_note(etudiants, nom, note):
    if nom not in etudiants:
        print("Étudiant introuvable.")
        return

    etudiants[nom].append(note)
    sauvegarder_donnees(etudiants)
    print("Note ajoutée.")


def afficher_moyenne(etudiants, nom):
    if nom not in etudiants:
        print("Étudiant introuvable.")
        return

    notes = etudiants[nom]
    if len(notes) == 0:
        print("Aucune note.")
        return

    moyenne = sum(notes) / len(notes)
    print(f"Moyenne de {nom} : {moyenne:.2f}")


def afficher_etudiants(etudiants):
    if not etudiants:
        print("Aucun étudiant pour le moment.")
        return

    print("\n--- Liste des étudiants ---")
    for nom, notes in etudiants.items():
        if notes:
            notes_str = ", ".join(str(n) for n in notes)
            moyenne = sum(notes) / len(notes)
            print(f"- {nom} | Notes: [{notes_str}] | Moyenne: {moyenne:.2f}")
        else:
            print(f"- {nom} | Notes: [] | Moyenne: N/A")


def supprimer_etudiant(etudiants, nom):
    if nom not in etudiants:
        print("Étudiant introuvable.")
        return

    del etudiants[nom]
    sauvegarder_donnees(etudiants)
    print(f"{nom} supprimé.")


# -------- Programme principal --------
etudiants = charger_donnees()
print("✅ Données chargées depuis data.json (si disponible).")

while True:
    print("\n1. Ajouter étudiant")
    print("2. Ajouter note")
    print("3. Afficher moyenne")
    print("4. Afficher tous les étudiants")
    print("5. Supprimer un étudiant")
    print("6. Quitter")

    choix = input("Choix : ").strip()

    if choix == "1":
        nom = normaliser_nom(input("Nom de l'étudiant : "))
        if nom:
            ajouter_etudiant(etudiants, nom)
        else:
            print("Nom invalide.")

    elif choix == "2":
        nom = normaliser_nom(input("Nom de l'étudiant : "))
        if not nom:
            print("Nom invalide.")
            continue

        try:
            note = float(input("Note (nombre) : "))
            ajouter_note(etudiants, nom, note)
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide pour la note.")

    elif choix == "3":
        nom = normaliser_nom(input("Nom de l'étudiant : "))
        if nom:
            afficher_moyenne(etudiants, nom)
        else:
            print("Nom invalide.")

    elif choix == "4":
        afficher_etudiants(etudiants)

    elif choix == "5":
        nom = normaliser_nom(input("Nom de l'étudiant à supprimer : "))
        if nom:
            supprimer_etudiant(etudiants, nom)
        else:
            print("Nom invalide.")

    elif choix == "6":
        print("Au revoir 👋")
        break

    else:
        print("Choix invalide.")
