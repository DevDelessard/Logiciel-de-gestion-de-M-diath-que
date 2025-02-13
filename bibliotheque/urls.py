from django.urls import path
from . import views
from .views import get_medias_disponibles, rendre_emprunt, voir_emprunts

urlpatterns = [
    path('', views.accueil, name='accueil'),  # Page d'accueil avec connexion et consultation
    path('membres/', views.liste_membres, name='liste_membres'),
    path('medias/', views.liste_medias, name='liste_medias'),
    path('membres/creer/', views.creer_membre, name='creer_membre'),  # Ajouter un membre
    path('membres/<int:membre_id>/modifier/', views.mettre_a_jour_membre, name='mettre_a_jour_membre'),  # Modifier un membre
    path('membres/<int:membre_id>/emprunts/', views.voir_emprunts, name='emprunts_membre'),  # Voir les emprunts d'un membre
    path('membres/<int:membre_id>/emprunter/', views.enregistrer_emprunt, name='enregistrer_emprunt'),  # Nouvel emprunt
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('get_medias_disponibles/', get_medias_disponibles, name='get_medias_disponibles'),
    path('emprunts/<int:emprunt_id>/rendre/', rendre_emprunt, name='rendre_emprunt'),
]

