from django.shortcuts import render, get_object_or_404, redirect
from .models import Membre, Emprunt, Media
from .forms import EmpruntForm, MembreForm
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib import messages

def accueil(request):
    medias = Media.objects.filter(disponible=True)
    return render(request, "accueil.html", {"medias": medias})

def liste_medias(request):
    medias = Media.objects.all()
    return render(request, "liste_medias.html", {"medias": medias})

@login_required
def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, "liste_membres.html", {"membres": membres})

MAX_EMPRUNTS = 3  # Limite d'emprunts par membre

@login_required
def enregistrer_emprunt(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    medias_disponibles = Media.objects.filter(disponible=True, empruntable=True)

    # Vérifier le nombre d'emprunts actifs
    emprunts_actifs = Emprunt.objects.filter(membre=membre)
    if emprunts_actifs.filter(date_retour_prevu__lt=now().date()).exists():
        messages.error(request, "Vous avez des emprunts en retard. Vous ne pouvez pas emprunter.")
        return redirect('emprunts_membre', membre_id=membre.id)

    if emprunts_actifs.count() >= MAX_EMPRUNTS:
        messages.error(request, "Vous avez atteint la limite d'emprunts autorisés.")
        return redirect('emprunts_membre', membre_id=membre.id)

    if request.method == "POST":
        form = EmpruntForm(request.POST)
        if form.is_valid():
            emprunt = form.save(commit=False)
            emprunt.membre = membre

            # Vérification du stock (maintenant géré dans models.py)
            if emprunt.media.est_disponible():
                emprunt.save()  # `save()` va réduire le stock dans `models.py`
                messages.success(request, "Emprunt enregistré avec succès.")
                return redirect('emprunts_membre', membre_id=membre.id)
            else:
                messages.error(request, "Ce média n'est plus disponible en stock.")

    else:
        form = EmpruntForm()

    return render(request, "enregistrer_emprunt.html", {"form": form, "membre": membre, "medias": medias_disponibles})

def get_medias_disponibles(request):
    media_type = request.GET.get("media_type")
    medias = Media.objects.filter(type=media_type, disponible=True).values("id", "titre")
    return JsonResponse({"medias": list(medias)})

@login_required
def creer_membre(request):
    if request.method == "POST":
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm()
    return render(request, 'creer_membre.html', {'form': form})

@login_required
def mettre_a_jour_membre(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    if request.method == "POST":
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm(instance=membre)
    return render(request, 'modifier_membre.html', {'form': form, 'membre': membre})

@login_required
def voir_emprunts(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    emprunts = Emprunt.objects.filter(membre=membre)
    medias_disponibles = Media.objects.filter(disponible=True, empruntable=True, quantite_disponible__gt=0)
    return render(request, "liste_emprunts.html", {"membre": membre, "emprunts": emprunts, "medias_disponibles": medias_disponibles})

def connexion(request):
    if request.user.is_authenticated:
        return redirect('liste_membres')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('liste_membres')
    else:
        form = AuthenticationForm()

    return render(request, "connexion.html", {"form": form})

@login_required
def deconnexion(request):
    logout(request)
    return redirect('accueil')

@login_required
def rendre_emprunt(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, id=emprunt_id)

    emprunt.delete()  # Géré via delete() dans models.py

    messages.success(request, f"Le média '{emprunt.media.titre}' a été rendu avec succès.")
    return redirect('emprunts_membre', membre_id=emprunt.membre.id)

