from django.db import models


class Pdf(models.Model):
    pdf_file = models.FileField()
    filename = models.CharField(max_length=200)
    text = models.CharField(max_length=1000000)
    latest_access = models.DateTimeField('Último acesso')
    latest_user = models.CharField(max_length=200)

    def __str__(self):
        return self.filename
