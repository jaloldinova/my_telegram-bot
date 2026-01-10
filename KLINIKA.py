from django.db import models

class Bemor(models.Model):
    ism=models.CharField(max_length=100)
    telefon=models.IntegerField()
    tugilgan_sana=models.DateField()
    def __str__(self):
        return self.ism

class Shifokor(models.Model):
    ism=models.CharField(max_length=100)
    mutaxasislik=models.CharField(max_length=100)
    def __str__(self):
        return self.ism

class Qabul(models.Model):
    bemor=models.ForeignKey(Bemor,on_delete=models.CASCADE)
    shifokor=models.ForeignKey(Shifokor,on_delete=models.CASCADE)
    sana=models.DateField()
    tashxis=models.CharField(max_length=255)
    def __str__(self):
        return self.bemor.ism
