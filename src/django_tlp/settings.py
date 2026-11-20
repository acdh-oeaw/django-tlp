from django.conf import settings

DEFAULT_TLP_CHOICES = [
    ("red", "red"),
    ("yellow", "yellow"),
    ("green", "green"),
]
DEFAULT_TLP_DEFAULT = "red"

TLP_CHOICES = getattr(settings, "DJANGO_TLP_CHOICES", DEFAULT_TLP_CHOICES)
TLP_DEFAULT = getattr(settings, "DJANGO_TLP_DEFAULT", DEFAULT_TLP_DEFAULT)
