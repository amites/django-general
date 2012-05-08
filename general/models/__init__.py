from django.db import models

class DefaultModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    class Meta:
        abstract=True

class ZipCode(models.Model):
    zip = models.CharField(unique=True, max_length=15)
    state = models.CharField(max_length=6)
    state_name = models.CharField(max_length=50, blank=True)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    city = models.CharField(max_length=150, blank=True)

    class Meta:
        db_table = u'zip_codes'
