from django.urls import path

from django_tlp.views import TLPStatusView

urlpatterns = [
    path(
        "tlp/<int:content_type_id>/<int:object_id>",
        TLPStatusView.as_view(),
        name="tlpstatus",
    )
]
