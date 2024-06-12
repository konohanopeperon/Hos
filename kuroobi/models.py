from django.db import models


class Employee(models.Model):
    empid = models.CharField(max_length=8, primary_key=True)
    empfname = models.CharField(max_length=64)
    emplname = models.CharField(max_length=64)
    emppasswd = models.CharField(max_length=256)
    emprole = models.IntegerField()

    def __str__(self):
        return f'{self.empfname} {self.emplname}'


class Tabyouin(models.Model):
    tabyouinid = models.CharField(max_length=8, primary_key=True)
    tabyouinmei = models.CharField(max_length=64)
    abyouinaddres = models.CharField(max_length=64)
    tabyouintel = models.CharField(max_length=13)
    abyouinshihonkin = models.IntegerField()
    kyukyu = models.IntegerField()


class Patient(models.Model):
    patid = models.CharField(max_length=8, primary_key=True)
    patfname = models.CharField(max_length=64)
    patlname = models.CharField(max_length=64)
    hokenmei = models.CharField(max_length=64)
    hokenexp = models.DateField()


class Medicine(models.Model):
    medicineid = models.CharField(max_length=8, primary_key=True)
    medicinename = models.CharField(max_length=64)
    unit = models.CharField(max_length=8)
