from django.contrib.localflavor.us.models import PhoneNumberField
from django.db import models

from general.models import DefaultModel
from general.models.choices_privacy import PRIVACY_LEVEL

PHONE_TYPES = (
    ('mobile', 'Mobile'),
    ('home', 'Home'),
    ('office', 'Office'),
    ('voip', 'VOIP'),
)

class Phone(DefaultModel):
    number = PhoneNumberField()
    type = models.CharField(max_length=10, choices=PHONE_TYPES, default='home')
    privacy = models.IntegerField(max_length=5, choices=PRIVACY_LEVEL, default=20, blank=True, null=True)

    class Meta:
        abstract = True


class Email(DefaultModel):
    address = models.CharField(max_length=250)
    privacy = models.IntegerField(max_length=5, choices=PRIVACY_LEVEL, default=30, blank=True, null=True)

    class Meta:
        abstract = True