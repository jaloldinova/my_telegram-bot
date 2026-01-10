from django.db import models

class Profil(models.Model):
    ism=models.CharField(max_length=100)
    yosh=models.PositiveIntegerField(null=True,blank=True)
    sana=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.ism

class Kurs(models.Model):
    nom=models.CharField(max_length=100)
    daraja=models.CharField(max_length=100)
    ustoz=models.CharField(max_length=100)
    narx=models.PositiveIntegerField(null=True,blank=True)
    chegirma=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.nom

class Izoh(models.Model):
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    kurs=models.ForeignKey(Kurs,on_delete=models.CASCADE)
    matn=models.CharField(max_length=100)
    sana=models.DateField()
    baho=models.PositiveIntegerField(null=True,blank=True)
    def __str__(self):
        return self.profil.ism

class Tanlangan(models.Model):
    kurs=models.ForeignKey(Kurs,on_delete=models.CASCADE)
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    def __str__(self):
        return self.profil.ism

class Xarid(models.Model):
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    kurs=models.ForeignKey(Kurs,on_delete=models.CASCADE)
    sana=models.DateField()
    holat=models.CharField(max_length=100)
    def __str__(self):
        return self.profil.ism


