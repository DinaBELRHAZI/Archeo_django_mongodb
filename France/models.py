from django.db import models


# Create your models here.
from django.db import models

from pathlib import Path



class France(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id', blank=True, null=False)
    lambert_x = models.CharField(db_column='Lambert_X', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lambert_y = models.CharField(db_column='Lambert_Y', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    departement = models.CharField(db_column='Departement', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commune = models.CharField(db_column='Commune', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_du_site = models.CharField(db_column='Nom_du_site', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_debut = models.CharField(db_column='Date_debut', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_fin = models.CharField(db_column='Date_fin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    periodes = models.CharField(db_column='Periodes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    themes = models.CharField(db_column='Themes', max_length=278, blank=True, null=True)  # Field name made lowercase.
    type_intervention = models.CharField(db_column='Type_intervention', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'france'
