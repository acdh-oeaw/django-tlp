from django import forms

from django_tlp.models import TLPStatus
from django_tlp.settings import TLP_CHOICES, TLP_DEFAULT


class TLPStatusForm(forms.ModelForm):
    status = forms.ChoiceField(choices=TLP_CHOICES, initial=TLP_DEFAULT)
    note = forms.CharField(required=False)

    class Meta:
        model = TLPStatus
        fields = ["status", "note"]

    class Media:
        css = {"all": ["css/django_tlp.css"]}
