from django.db import models

class Lavozim(models.Model):
    nom= models.CharField(max_length=100)
    maosh=models.IntegerField()
    def __str__(self):
        return self.nom

class Xodim(models.Model):
    ism=models.CharField(max_length=100)
    lavozim=models.ForeignKey(Lavozim,on_delete=models.CASCADE)
    ishga_kirgan_sana=models.DateField()
    def __str__(self):
        return self.ism