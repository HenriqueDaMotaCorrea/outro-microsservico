from django.db import models


class Pdf(models.Model):
    pdf_file = models.FileField(upload_to='uploads')
    text = models.CharField(max_length=1000000, null=True)
    latest_access = models.DateTimeField('Último acesso', null=True)
    latest_user = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.pdf_file.name
