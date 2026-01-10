from django.db import models

class Mahsulotlar(models.Model):
    nom=models.CharField(max_length=100)
    narx=models.PositiveIntegerField()
    miqdor=models.IntegerField()
    def __str__(self):
        return self.nom

class Mijoz(models.Model):
    ism=models.CharField(max_length=100)
    telefon=models.IntegerField()
    manzil=models.CharField(max_length=100)
    def __str__(self):
        return self.ism

class Buyurtma(models.Model):
    mijoz=models.ForeignKey(Mahsulotlar,on_delete=models.CASCADE)
    sana=models.DateField(auto_now_add=True)
    umumiy_summa=models.PositiveIntegerField()
    def __str__(self):
        return self.sana

class Buyurtma_Tovar(models.Model):
    buyurtma=models.ForeignKey(Buyurtma,on_delete=models.CASCADE)
    mahsulotlar=models.ForeignKey(Mahsulotlar,on_delete=models.CASCADE)
    miqdor=models.IntegerField()
    def __str__(self):
        return self.mahsulotlar.manzil



