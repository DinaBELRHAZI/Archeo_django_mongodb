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

    inProj = CRS('EPSG:2154')
    outProj = CRS('EPSG:4326')

    for site in list_site:
        list_site.lambert_x = re.sub("[,]", ".", site.lambert_x)
        list_site.lambert_y = re.sub("[,]", ".", site.lambert_y)
        x, y = transform(inProj, outProj, list_site.lambert_x, list_site.lambert_y)
        site.lambert_x = x
        site.lambert_y = y
        print(site.lambert_x)
        print(site.lambert_y)

    list_site.lambert_x = site.lambert_x
    list_site.lambert_y = site.lambert_y


    return render(request, 'France/maps.html', {'list': list_site})  # appem du rep template


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
        # S'il s'agit d'un formulaire d'insertion, le formulaire sera vide sinon il sera pr??rempli
        # Si id == 0, c'est une insertion sinon une mise ?? jour
        if id == 0:
            return render(request, 'France/creerSite_1.html')
        else:

            # R??cup??re les donn??es selon l'id du site
            site = France.objects.get(pk=id)
            print(site)

            return render(request, 'France/modifSite.html', {'site': site})
    else:

        print("Je cr??e un nouveau monument !")
        print(request.POST)
        print(request.POST["Lambert_X"])

        # R??cup??re les donn??es de chaque champs
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
        print("Instantiation, cr??ation ou modif ")

        if id == 0:
            # Insertion

            # R??cup??re le dernier id de la table
            idNew = France.objects.last().id
            # Incr??mentation de l'id
            idNew = idNew + 1
            print(idNew)

            # Insertion des donn??es en bdd
            franceRecup = France.objects.create(id=idNew, lambert_x=lambert_x, lambert_y=lambert_y, region=region,
                                                departement=departement \
                                                , commune=commune, nom_du_site=nom_du_site \
                                                , date_debut=date_debut, date_fin=date_fin, periodes=periodes,
                                                themes=themes, type_intervention=type_intervention)


        else:
            # Modification

            # R??cup??re les donn??es d'un site selon son id
            franceRecup = France.objects.get(pk=id)

            # Ecrasement des donn??es des champs ??xistant
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
