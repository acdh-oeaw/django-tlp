from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class TLPStatus(models.Model):
    status = models.CharField(max_length=300, null=False)
    note = models.TextField(blank=True, null=True)

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, db_index=True
    )
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("content_type", "object_id"), name="tlp_unique_content_object"
            )
        ]

    def __str__(self):
        return f"{self.content_object} -> {self.status}"
