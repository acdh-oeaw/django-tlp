import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from django_tlp.forms import TLPStatusForm
from django_tlp.models import TLPStatus
from django_tlp.settings import TLP_DEFAULT

logger = logging.getLogger(__name__)


class TLPStatusView(LoginRequiredMixin, UpdateView):
    template_name = "django_tlp/templatetags/tlpstatus.html"
    model = TLPStatus
    form_class = TLPStatusForm

    def get_object(self, *args, **kwargs):
        content_type = self.kwargs.get("content_type_id")
        pk = self.kwargs.get("object_id")
        tlps, _ = TLPStatus.objects.update_or_create(
            content_type_id=content_type,
            object_id=pk,
            create_defaults={"status": TLP_DEFAULT},
        )
        return tlps

    def get_success_url(self):
        return self.request.path

    def form_invalid(self, form):
        logger.info("Form invalid %s", form)
        return super().form_invalid(form)
