from django.forms import ModelForm
from . import models


class UploadPdfForm(ModelForm):
    class Meta:
        model = models.Pdf
        fields = ['pdf_file']
