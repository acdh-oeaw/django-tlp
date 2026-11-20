from django import template
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django_tlp.models import TLPStatus
from django_tlp.settings import TLP_CHOICES, TLP_DEFAULT
from django_tlp.forms import TLPStatusForm

register = template.Library()


@register.inclusion_tag("django_tlp/templatetags/tlpstatus.html")
def get_tlpchoices_for_object(obj: models.Model):
    content_type = ContentType.objects.get_for_model(obj)
    tlps, _ = TLPStatus.objects.get_or_create(
        content_type=content_type,
        object_id=obj.pk,
        defaults={"status": TLP_DEFAULT},
    )
    return {"object": tlps, "form": TLPStatusForm(instance=tlps)}


@register.inclusion_tag("django_tlp/single_circle.html")
def get_tlpstatus_for_object(obj: models.Model):
    content_type = ContentType.objects.get_for_model(obj)
    tlps, _ = TLPStatus.objects.get_or_create(
        content_type=content_type,
        object_id=obj.pk,
        defaults={"status": TLP_DEFAULT},
    )
    return {"object": tlps}
