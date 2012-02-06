from django.contrib.localflavor.us.us_states import US_STATES
from django.db import models

from general.models import DefaultModel
from general.models.choices_location import COUNTRY_CHOICES

class AddressStreet(models.Model):
    #DefaultModel
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    street = models.CharField(max_length=250, null=True, blank=True)
    city =  models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True, choices=US_STATES)
    #    province = models.CharField(max_length=120, null=True, blank=True, help_text='For non-US State, please select other above.')
    postal_code = models.IntegerField(help_text="5 digits US only", max_length=5, null=True, blank=True)
    county = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True, choices=COUNTRY_CHOICES, default='US')

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s\n%s, %s %s" % (self.street, self.city, self.state, self.postal_code)

class AddressExtended(AddressStreet):
    latitude = models.CharField(max_length=50, null=True, blank=True, verbose_name='Latitude')
    longitude = models.CharField(max_length=50, null=True, blank=True, verbose_name='Longitude')

    class Meta:
        abstract = True
