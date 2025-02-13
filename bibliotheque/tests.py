from django.test import TestCase
from django.utils.timezone import now
from datetime import timedelta
from bibliotheque.models import Membre, Media, Emprunt
from django.contrib.auth.models import User


class EmpruntTestCase(TestCase):
    def setUp(self):
        """Configuration des données initiales"""
        self.user = User.objects.create_user(username="testuser", password="password")
        self.membre = Membre.objects.create(nom="Test Membre", email="test@example.com")
        self.media = Media.objects.create(titre="Test Media", type="livre", quantite_disponible=5)

    def test_ajout_emprunt_reduit_stock(self):
        """Tester que l'ajout d'un emprunt diminue le stock de 1"""
        emprunt = Emprunt.objects.create(membre=self.membre, media=self.media, date_emprunt=now().date())
        
        # Vérifier que le stock est bien mis à jour
        self.media.refresh_from_db()
        self.assertEqual(self.media.quantite_disponible, 4)  # Le stock doit être réduit de 1

    def test_rendre_emprunt_ajoute_stock(self):
        """Tester que la restitution d'un emprunt augmente le stock de 1"""
        self.client.force_login(self.user)  # 🔥 S'assurer que l'utilisateur est connecté
        
        # Créer un emprunt
        emprunt = Emprunt.objects.create(membre=self.membre, media=self.media, date_emprunt=now().date())

        # Vérifier que le stock a diminué
        self.media.refresh_from_db()
        self.assertEqual(self.media.quantite_disponible, 4)

        # Rendre l'emprunt via l'URL de la vue `rendre_emprunt`
        response = self.client.post(f"/bibliotheque/emprunts/{emprunt.id}/rendre/")

        # Rafraîchir les données du média
        self.media.refresh_from_db()
        self.assertEqual(self.media.quantite_disponible, 5)  # 🔥 Le stock doit être revenu à 5

    def test_membre_bloque_ne_peut_pas_emprunter(self):
        """Tester qu'un membre avec un emprunt en retard ne peut pas emprunter"""
        # Créer un emprunt en retard
        Emprunt.objects.create(
            membre=self.membre, media=self.media,
            date_emprunt=now().date() - timedelta(days=15)
        )

        self.assertTrue(self.membre.est_bloque())  # 🔥 Doit retourner True car en retard

        # Vérifier que le membre bloqué ne peut pas emprunter
        nouvel_emprunt = Emprunt(membre=self.membre, media=self.media, date_emprunt=now().date())
        with self.assertRaises(ValueError):  # 🔥 L'erreur doit être levée
            nouvel_emprunt.save()
