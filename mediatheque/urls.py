from django.contrib import admin
from django.urls import path, include
from bibliotheque import views  # Importe la vue d'accueil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bibliotheque/', include('bibliotheque.urls')),
    path('', views.accueil, name='accueil'),  # Ajoute une URL pour l'accueil
]
