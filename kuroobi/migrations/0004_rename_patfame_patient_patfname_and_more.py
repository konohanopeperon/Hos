# Generated by Django 5.0.6 on 2024-06-12 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuroobi', '0003_medicine_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='patfame',
            new_name='patfname',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='patlame',
            new_name='patlname',
        ),
    ]
