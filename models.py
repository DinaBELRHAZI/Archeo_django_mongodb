# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DoctrineMigrationVersions(models.Model):
    version = models.CharField(primary_key=True, max_length=191)
    executed_at = models.DateTimeField(blank=True, null=True)
    execution_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctrine_migration_versions'


class France(models.Model):
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


class Images(models.Model):
    id_img = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    id_france = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'
