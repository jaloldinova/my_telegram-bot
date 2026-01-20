from django.db import models


class Talaba(models.Model):
    ism=models.CharField(max_length=200)
    guruh=models.CharField(max_length=200)
    kurs=models.PositiveIntegerField(default=1)
    kitob_soni=models.PositiveIntegerField(default=1,blank=True,null=True)
    def __str__(self):
        return self.ism

class Muallif(models.Model):
    JINS_CHOICES = (
        ('ERKAK','ERKAK'),
        ('AYOL','AYOL')
    )
    TIRIK_CHOICES = (
        ('TRUE','TRUE'),
        ('FALSE','FALSE')
    )
    ism=models.CharField(max_length=200)
    jins=models.CharField(max_length=200,choices=JINS_CHOICES)
    tugilgan_sana=models.DateField(blank=True,null=True)
    kitob_soni=models.IntegerField(blank=True,null=True)
    tirik=models.CharField(max_length=200,choices=TIRIK_CHOICES)
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    JANR_CHOICES = (
    ('BADIIY','BADIIY'),
    ('FANTASTIK','FANTASTIK'),
    ('DINIY','DINIY'),
    ('ROMANTIK','ROMANTIK')
    )
    nom=models.CharField(max_length=200)
    janr=models.CharField(max_length=200,choices=JANR_CHOICES)
    sahifa=models.IntegerField(blank=True,null=True)
    muallif=models.ForeignKey(Muallif,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Kutubxonachi(models.Model):
    ism=models.CharField(max_length=200)
    ish_vaqti=models.TimeField(blank=True,null=True)
    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba=models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob=models.ForeignKey(Kitob,on_delete=models.CASCADE)
    kutubxonachi=models.ForeignKey(Kutubxonachi,on_delete=models.CASCADE)
    olingan_sana=models.DateTimeField(auto_now_add=True)
    qaytarish_sana=models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.talaba.ism




