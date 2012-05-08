from django.contrib.localflavor.us.models import PhoneNumberField
from django.db import models

#from general.models import DefaultModel
from general.models.privacy import Privacy

PHONE_TYPES = (
    ('mobile', 'Mobile'),
    ('home', 'Home'),
    ('office', 'Office'),
    ('voip', 'VOIP'),
)


class Contact(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
            abstract = True

class Phone(models.Model):
    number = PhoneNumberField(null=True, blank=True)
    type = models.CharField(max_length=10, choices=PHONE_TYPES, default='home', null=True, blank=True)

    class Meta:
        abstract = True

class Email(models.Model):
    email = models.EmailField(max_length=250, null=True, blank=True)

    class Meta:
        abstract = True

class WebSite(models.Model):
    website = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        abstract = True