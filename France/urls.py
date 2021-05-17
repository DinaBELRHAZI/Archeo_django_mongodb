from django.urls import path

from . import views

app_name = 'France'

urlpatterns = [
    # ex: /pizzas/
    path('', views.index, name='index'),
    # path('creerSite/', views.creerSite, name='creerSite'),
    path('creerSite/', views.Site, name='creerSite'), # get et post request pour la création
    path('modifSite/<int:id>/', views.Site, name='modifSite'), # get et post request pour la maj
    path('maps/', views.maps, name='maps'),
    path('oneSite/<int:id>/', views.oneSite, name='oneSite'),
    # path('oneSite/update/<int:id>/', views.oneSiteUpdate, name='oneSiteUpdate'),
    # path('oneSite/updateSend/<int:id>/', views.oneSiteUpdateSend, name='oneSiteUpdateSend'),



    # # ex: /pizzas/5/
    # path('<int:pizza_id>/', views.detail, name='detail'),
    #
    # # ex: /loadimage/
    # path('loadimage/', views.loadimage, name='loadimage'),
    #
    #
    # # ex: /pizzas/xml/
    # path('xml/', views.index_xml, name='index_xml'),
    #
    # # ex: /pizzas/5/update
    # path('<int:pizza_id>/update/', views.detail_update, name='detail_update'),
    #
    # # ex: /pizzas/new
    # path('new/', views.pizza_new, name='pizza_new'),
    #
    # # ex: /pizzas/5/delete
    # path('<int:pizza_id>/delete/', views.pizza_delete, name='pizza_delete'),

]
