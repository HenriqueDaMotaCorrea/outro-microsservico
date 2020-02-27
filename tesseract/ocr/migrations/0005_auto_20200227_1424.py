# Generated by Django 3.0.3 on 2020-02-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0004_pdf_pdf_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdf',
            name='filename',
        ),
        migrations.AlterField(
            model_name='pdf',
            name='latest_access',
            field=models.DateTimeField(null=True, verbose_name='Último acesso'),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='latest_user',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='text',
            field=models.CharField(max_length=1000000, null=True),
        ),
    ]
