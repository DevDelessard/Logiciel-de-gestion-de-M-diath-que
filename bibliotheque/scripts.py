from bibliotheque.models import Livre, Dvd, Cd, JeuDePlateau, Emprunteur

def creer_donnees_test():
    # Membres
    membre1 = Emprunteur.objects.create(name="Alice")
    membre2 = Emprunteur.objects.create(name="Bob", bloque=True)

    # Médias
    Livre.objects.create(name="1984", auteur="George Orwell", disponible=True)
    Dvd.objects.create(name="Inception", realisateur="Christopher Nolan", disponible=True)
    Cd.objects.create(name="Thriller", artiste="Michael Jackson", disponible=True)
    JeuDePlateau.objects.create(name="Catan", createur="Klaus Teuber")

    print("Données de test créées.")
