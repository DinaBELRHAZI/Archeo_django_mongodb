import re

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django import forms
# Create your views here.
from France.models import France
from forms import FranceForm
from pyproj import Proj, transform, CRS


# context = {
#         'Sites_list': "toto"
#     }

# AFFICHAGE DE LA LISTE DES SITES ***********************************


def index(request):
    list_site = France.objects.all()

    for site in list_site:
        # print(site.nom_du_site + site.lambert_x + site.lambert_y)

        list = {
            'id': site.id,
            'lambert_x': site.lambert_x,
            'lambert_y': site.lambert_y,
            'region': site.region,
            'departement': site.departement,
            'commune': site.commune,
            'nom_du_site': site.nom_du_site,
            'date_debut': site.date_debut,
            'date_fin': site.date_fin,
            'periodes': site.periodes,
            'themes': site.themes,
            'type_intervention': site.type_intervention,
        }
        # print(list)

    return render(request, 'France/listeFranceAll.html', {'list_site': list_site})  # appem du rep template


# AFFICHAGE DE LA CARTE ***********************************

def maps(request):
    list_site = France.objects.all()

    for site in list_site:
        inProj = CRS('EPSG:2154')
        outProj = CRS('EPSG:4326')
        site.lambert_x = re.sub("[,]", ".", site.lambert_x)
        site.lambert_y = re.sub("[,]", ".", site.lambert_y)
        x2, y2 = transform(inProj, outProj, site.lambert_x, site.lambert_y)

        list = {
            'id': site.id,
            'lambert_x': x2,
            'lambert_y': y2,
            'region': site.region,
            'departement': site.departement,
            'commune': site.commune,
            'nom_du_site': site.nom_du_site,
            'date_debut': site.date_debut,
            'date_fin': site.date_fin,
            'periodes': site.periodes,
            'themes': site.themes,
            'type_intervention': site.type_intervention,
        }
        # print(list)

    return render(request, 'France/maps.html', {'list_site': list})  # appem du rep template


# AFFICHAGE D'UN SITE ***********************************

def oneSite(request, id):
    # print(id)
    list_site = France.objects.filter(id=id)

    print(list_site)
    for site in list_site:
        # print(site.id, site.nom_du_site + site.lambert_x + site.lambert_y)
        # inProj = Proj(init='epsg:2154')
        # outProj = Proj(init='epsg:4326')
        inProj = CRS('EPSG:2154')
        outProj = CRS('EPSG:4326')
        # site.lambert_x = re.sub("[,]", ".", site.lambert_x)
        # site.lambert_y = re.sub("[,]", ".", site.lambert_y)
        x2, y2 = transform(inProj, outProj, site.lambert_x, site.lambert_y)

        print(x2, y2)

        list = {
            'id': site.id,
            'lambert_x': x2,
            'lambert_y': y2,
            'region': site.region,
            'departement': site.departement,
            'commune': site.commune,
            'nom_du_site': site.nom_du_site,
            'date_debut': site.date_debut,
            'date_fin': site.date_fin,
            'periodes': site.periodes,
            'themes': site.themes,
            'type_intervention': site.type_intervention,
        }

        # print(list)
    return render(request, 'France/listeFranceOneSite.html', {'list_site': list})  # appem du rep template


# CREATION ET MODIFICATION D'UN SITE ***********************************

def Site(request, id=0):
    if request.method == "GET":
        # S'il s'agit d'un formulaire d'insertion, le formulaire sera vide sinon il sera prérempli
        # Si id == 0, c'est une insertion sinon une mis à jour
        if id == 0:
            form = FranceForm()
            return render(request, 'France/creerSite.html')
        else:
            # Récupère les données selon l'id du site
            sites = France.objects.filter(pk=id)
            # print(sites)
            # form = FranceForm(instance=sites)

            for site in sites:

                list = {
                    'id': site.id,
                    'lambert_x': site.lambert_x,
                    'lambert_y': site.lambert_y,
                    'region': site.region,
                    'departement': site.departement,
                    'commune': site.commune,
                    'nom_du_site': site.nom_du_site,
                    'date_debut': site.date_debut,
                    'date_fin': site.date_fin,
                    'periodes': site.periodes,
                    'themes': site.themes,
                    'type_intervention': site.type_intervention,
                }
                print(list)
            # return render(request, 'France/modifSite.html', {'list_site': list})
            return render(request, 'France/modifSite.html', {'list_site': list})  # appel du form template
    else:
        if id == 0:
            form = FranceForm(request.POST)
        else:
            site = France.objects.get(pk=id)
            form = FranceForm(request.POST, instance=site)
            print("form")
        if form.is_valid():
            form.save()
            print("Formualaire enregistré !")
        return redirect("France:index")







#
# def creerSiteSend(request):
#     print(request)
#
#     # pass the object as instance in form
#     form = France(request.POST or None)
#     print(form.nom_du_site)
#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         form.save()
#         # return HttpResponseRedirect("/" + id)
#     #
#     #
#     # if request.method == "POST":
#     #     if form.is_valid():
#     #         form.save()
#     #     else:
#     #         form = PostCreateForm()
#
#     return render(request, 'France/listeFranceAll.html', {'form': form})  # appem du rep template


# MODIFICATION D'UN SITE ***********************************

# def oneSiteUpdate(request, id):
#     list_site = France.objects.filter(id=id)
#
#     # print(list_site)
#     for site in list_site:
#         # print(site.id, site.nom_du_site + site.lambert_x + site.lambert_y)
#         list = {
#             'id': site.id,
#             'lambert_x': site.lambert_x,
#             'lambert_y': site.lambert_y,
#             'region': site.region,
#             'departement': site.departement,
#             'commune': site.commune,
#             'nom_du_site': site.nom_du_site,
#             'date_debut': site.date_debut,
#             'date_fin': site.date_fin,
#             'periodes': site.periodes,
#             'themes': site.themes,
#             'type_intervention': site.type_intervention,
#         }
#
#     return render(request, 'France/modifSite.html', {'list_site': list})  # appem du rep template


# def oneSiteUpdateSend(request, id):
#     list_site = France.objects.get(id=id)
#     form = FranceForm(request.POST, instance=list_site)
#     print("DANS oneSiteUpdateSend")
#     if form.is_valid():
#         form.save()
#         print("Modification validée")
#         return redirect("France:index")
#
#         # if request.method == "POST":
#     #     form = PostCreateForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #     else:
#     #         form = PostCreateForm()
#
#     # list_site = France.objects.filter(id=id)
#     #
#     # # print(list_site)
#     # for site in list_site:
#     #
#     #     France.objects.get
#     #     list = {
#     #         'id': site.id,
#     #         'lambert_x': site.lambert_x,
#     #         'lambert_y': site.lambert_y,
#     #         'region': site.region,
#     #         'departement': site.departement,
#     #         'commune': site.commune,
#     #         'nom_du_site': site.nom_du_site,
#     #         'date_debut': site.date_debut,
#     #         'date_fin': site.date_fin,
#     #         'periodes': site.periodes,
#     #         'themes': site.themes,
#     #         'type_intervention': site.type_intervention,
#     #     }
#     #     print(list)
#
#     return render(request, 'France/modifSite.html', {'list_site': list_site})  # appem du rep template


# update view for details
# def update_view(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     # list = {
#     #     'id': site.id,
#     #     'lambert_x': site.lambert_x,
#     #     'lambert_y': site.lambert_y,
#     #     'region': site.region,
#     #     'departement': site.departement,
#     #     'commune': site.commune,
#     #     'nom_du_site': site.nom_du_site,
#     #     'date_debut': site.date_debut,
#     #     'date_fin': site.date_fin,
#     #     'periodes': site.periodes,
#     #     'themes': site.themes,
#     #     'type_intervention': site.type_intervention,
#     # }
#
#     # fetch the object related to passed id
#     obj = get_object_or_404(France, id=id)
#
#     # pass the object as instance in form
#     form = France(request.POST or None, instance=obj)
#
#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/" + id)
#
#     # add form dictionary to context
#     list["form"] = form
#
#     return render(request, "update_view.html", list)
