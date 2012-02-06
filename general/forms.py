from django.forms import CharField
from django.forms.models import BaseInlineFormSet

class RequiredInlineFormSet(BaseInlineFormSet):
    """
    Generates an inline formset that is required
    """

    def _construct_form(self, i, **kwargs):
        """
        Override the method to change the form attribute empty_permitted
        """
        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form

class CityStateZipField(CharField):
    def validate(self, value):
        super(CityStateZipField, self).validate(value)
        match = re.search(r"\d{5}|\w+, [\.\w]+(?:\w+)?", value)
        if not match:
            raise exceptions.ValidationError(_('Please enter a 5 digit Zip Code or City, State'))
