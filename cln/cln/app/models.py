from django.db import models
from django.urls import reverse

class Patient(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    area = models.CharField(max_length=50)
    height=models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    bpi = models.IntegerField()

    def __str__(self):
        return str(self.uid)

    def get_absolute_url(self):
        return reverse('done')


class Consult(models.Model):
    problem = models.CharField(max_length=500)
    treatment = models.CharField(max_length=500)
    file = models.FileField(upload_to='documents/',blank=True)
    consult = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)

    def get_absolute_url(self):
        return reverse('add')