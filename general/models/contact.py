from django.contrib.localflavor.us.models import PhoneNumberField
from django.db import models

#from general.models import DefaultModel
from general.models.choices_privacy import PRIVACY_LEVEL

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
    privacy = models.IntegerField(max_length=5, choices=PRIVACY_LEVEL, default=20, blank=True, null=True)

    class Meta:
        abstract = True

class Email(models.Model):
    address = models.EmailField(max_length=250, null=True, blank=True)
    privacy = models.IntegerField(max_length=5, choices=PRIVACY_LEVEL, default=30, blank=True, null=True)

    class Meta:
        abstract = True