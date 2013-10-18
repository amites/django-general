import urllib2

from django.contrib.localflavor.us.us_states import US_STATES
from django.db import models

from general.geo_helpers import get_lat_lng
#from general.models import DefaultModel
from general.models.choices_location import COUNTRY_CHOICES


try:
    from geopy import geocoders
except ImportError:
    geocoders = False


class AddressStreet(models.Model):
    street = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True,
                        choices=US_STATES)
    #    province = models.CharField(max_length=120, null=True, blank=True,
    #               help_text='For non-US State, please select other above.')
    postal_code = models.IntegerField(help_text="5 digits US only",
                        max_length=5, null=True, blank=True)
    county = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True,
                        choices=COUNTRY_CHOICES, default='US')

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s\n%s, %s %s" % (self.street, self.city, self.state,
                                    self.postal_code)


class AddressGeoLocation(AddressStreet):
    latitude = models.CharField(max_length=50, null=True, blank=True,
                        verbose_name='Latitude')
    longitude = models.CharField(max_length=50, null=True, blank=True,
                        verbose_name='Longitude')
    geolocation = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True

    ## Geocode using full address
    def _get_full_address(self):
        return u'%s, %s, %s, %s %s' % (self.street, self.city, self.state,
                                       self.country, self.postal_code)
    full_address = property(_get_full_address)

    ## Geocode by just using zipcode and country name
    #    (faster and more reliable)
    def _get_geo_address(self):
        return u'%s %s' % (self.country.name, self.zipcode)
    geo_address = property(_get_geo_address)

    def get_geocode(self):
        if not self.latitude or not self.longitude:
            address = []
            if self.street:
                address.append(self.street)
            if self.city:
                address.append(self.city)
            if self.state:
                address.append(self.state)
            if self.postal_code:
                address.append(str(self.postal_code))
#            print address
            if len(address) > 1 and geocoders:
                g = geocoders.GoogleV3()
#                print ', '.join(address)
                place, (lat, lng) = g.geocode(', '.join(address), False)
    #            print location
                try:
                    self.latitude = lat
                    self.longitude = lng
                except IndexError:
#                    self.latitude = latlon[0]
#                    self.longitude = latlon[1]
                    raise Exception('Unable to pull geocode')
    #            print latlon
#                print self.latitude
#                print self.longitude
                self.geolocation = '%s,%s' % (self.latitude, self.longitude)
                self.save()
                return self.geolocation
        return self.geolocation

    def save(self, *args, **kwargs):
        if not self.geolocation:
#            if self.zipcode and self.country:
#                location = self.geo_address
#                self.latlng = get_lat_lng(location)
#            else:
            location = '+'.join(filter(None, \
                (self.street, self.city, self.state, self.country)))
            self.latlng = get_lat_lng(location)
        super(AddressGeoLocation, self).save(*args, **kwargs)
