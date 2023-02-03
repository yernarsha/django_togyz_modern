# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Games(models.Model):
    field_whitename = models.CharField(max_length=50, db_column='_WhiteName', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_blackname = models.CharField(max_length=50, db_column='_BlackName', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_result = models.CharField(max_length=7, db_column='_Result', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_event = models.CharField(max_length=50, db_column='_Event', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_date = models.CharField(max_length=10, db_column='_Date', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_round = models.IntegerField(db_column='_Round', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_site = models.CharField(max_length=50, db_column='_Site', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_notation = models.TextField(db_column='_Notation', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_whiteid = models.CharField(max_length=10, db_column='_WhiteID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_blackid = models.CharField(max_length=10, db_column='_BlackID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_res = models.IntegerField(db_column='_Res', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_eventid = models.IntegerField(db_column='_EventID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_dateint = models.IntegerField(db_column='_DateInt', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_siteid = models.IntegerField(db_column='_SiteID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_reserved1 = models.IntegerField(db_column='_reserved1', blank=True, null=True)  # Field renamed because it started with '_'.
    field_reserved2 = models.IntegerField(db_column='_reserved2', blank=True, null=True)  # Field renamed because it started with '_'.
    field_reserved3 = models.CharField(max_length=50, db_column='_reserved3', blank=True, null=True)  # Field renamed because it started with '_'.
    field_reserved4 = models.BooleanField(db_column='_reserved4', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'games'
