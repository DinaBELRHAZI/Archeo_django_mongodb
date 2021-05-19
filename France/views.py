import re

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django import forms
# Create your views here.
from France.models import France
from pyproj import Proj, transform, CRS




# AFFICHAGE DE LA LISTE DES SITES ***********************************


def index(request):
    list_site = France.objects.all()

    return render(request, 'France/listeFranceAll.html', {'list_site': list_site})  # appem du rep template


# AFFICHAGE DE LA CARTE ***********************************

def maps(request):
    list_site = France.objects.all()

    for site in list_site:

        inProj = CRS('EPSG:2154')
        outProj = CRS('EPSG:4326')
        list_site.lambert_x = re.sub("[,]", ".", site.lambert_x)
        list_site.lambert_y = re.sub("[,]", ".", site.lambert_y)
        x, y = transform(inProj, outProj, list_site.lambert_x, list_site.lambert_y)
        print(x)
        list_site.lambert_x = x
        list_site.lambert_y = y

    return render(request, 'France/maps.html', {'list_site': list})  # appem du rep template


# AFFICHAGE D'UN SITE ***********************************

def oneSite(request, id):
    # print(id)
    list_site = France.objects.get(id=id)
    print(list_site.lambert_x)
    print(list_site.lambert_y)

    inProj = CRS('EPSG:2154')
    outProj = CRS('EPSG:4326')
    list_site.lambert_x = re.sub("[,]", ".", list_site.lambert_x)
    list_site.lambert_y = re.sub("[,]", ".", list_site.lambert_y)
    x, y = transform(inProj, outProj, list_site.lambert_x, list_site.lambert_y)

    list_site.lambert_x = x
    list_site.lambert_y = y

    return render(request, 'France/listeFranceOneSite.html', {'list_site': list_site})  # appem du rep template


# CREATION ET MODIFICATION D'UN SITE ***********************************



def Site(request, id=0):

    if request.method == "GET":
        # S'il s'agit d'un formulaire d'insertion, le formulaire sera vide sinon il sera prérempli
        # Si id == 0, c'est une insertion sinon une mise à jour
        if id == 0:
            return render(request, 'France/creerSite_1.html')
        else:

            # Récupère les données selon l'id du site
            site = France.objects.get(pk=id)
            print(site)

            return render(request, 'France/modifSite.html',  {'site': site})
    else:

        print("Je crée un nouveau monument !")
        print(request.POST)
        print(request.POST["Lambert_X"])

        # Récupère les données de chaque champs
        lambert_x = request.POST['Lambert_X']
        lambert_y = request.POST['Lambert_Y']
        region = request.POST['Region']
        departement = request.POST['Departement']
        commune = request.POST['Commune']
        nom_du_site = request.POST['Nom_du_site']
        date_debut = request.POST['Date_debut']
        date_fin = request.POST['Date_fin']
        periodes = request.POST['Periodes']
        themes = request.POST['Themes']
        type_intervention = request.POST['Type_intervention']
        print("Instantiation, création ou modif ")


        if id == 0:
            # Insertion

            # Récupère le dernier id de la table
            idNew = France.objects.last().id
            # Incrémentation de l'id
            idNew =  idNew+1
            print(idNew)

            # Insertion des données en bdd
            franceRecup = France.objects.create(id = idNew, lambert_x = lambert_x, lambert_y = lambert_y, region = region, departement = departement\
                                                , commune = commune, nom_du_site = nom_du_site\
                                                , date_debut = date_debut, date_fin = date_fin, periodes = periodes, themes = themes, type_intervention = type_intervention)


        else:
            # Modification

            # Récupère les données d'un site selon son id
            franceRecup = France.objects.get(pk=id)

            # Ecrasement des données des champs éxistant
            franceRecup.lambert_x = lambert_x
            franceRecup.lambert_y = lambert_y
            franceRecup.region = region
            franceRecup.departement = departement
            franceRecup.commune = commune
            franceRecup.nom_du_site = nom_du_site
            franceRecup.date_debut = date_debut
            franceRecup.date_fin = date_fin
            franceRecup.periodes = periodes
            franceRecup.themes = themes
            franceRecup.type_intervention = type_intervention

        franceRecup.save()
        return redirect("France:index")

