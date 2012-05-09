#from django.contrib.auth.models import User
from django.forms import ModelChoiceField


class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()
