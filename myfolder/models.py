from tkinter import CASCADE

from django.db import models

# Create your models here.


class Users(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30,null=True,blank=True)
    tg_id = models.IntegerField(unique=True)

class Turlar(models.Model):
    nomi = models.CharField(max_length=30)

    def __str__(self):
        return self.nomi

class Maxsulot(models.Model):
    nomi = models.CharField(max_length=30)
    narxi = models.FloatField()
    turi = models.ForeignKey(Turlar, on_delete=models.CASCADE)
    rasm_url = models.CharField(max_length=500)

class Savdo(models.Model):
    maxsulot_id = models.ForeignKey(Maxsulot,on_delete=models.CASCADE)
    tg_id = models.IntegerField()
    number = models.IntegerField()
    status  = models.BooleanField(default=False)
    last_date = models.DateTimeField()


