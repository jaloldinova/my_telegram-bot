#son=int(input("1-7 gacha son kiriting:"))
#match son:
#    case 1:
#       print("dushanba")
#   case 2:
#       print("seshanba")
#   case 3:
#       print("chorsanba")
#   case 4:
#       print("payshanba")
#    case 5:
#        print("juma")
#    case 6:
#        print("shanba")
#    case 7:
#        print("yakshanba")
#son=int(input("1-5 k son kiriting:"))
#match son:
#   case 1:
#        print("yomon baho:")
#    case 2:
#        print("qoniqarsiz baho:")
#    case 3:
#        print("qoniqarli baho:")
#    case 4:
#        print("yaxshi baho:")
#    case 5:
#        print("alo baho:")
#    case _:
#        print("xato:")
#oy=int(input("oyni raqamini kiriting:"))
#match oy:
#    case 1| 2 | 12:
#        print("qish")
#    case 3| 4 | 5:
#        print("bahor")
#    case 6|7|8:
#        print("yoz")
#    case 9|10|11:
#        print("kuz")
#    case _:
#        print("xato kiritilgan:")
import asyncio
import csv
import json
import random
import sqlite3
from collections import deque
from idlelib.replace import replace
from idlelib.undo import Command
from mailbox import Message
from math import factorial
from multiprocessing import connection
from operator import index
from os import remove

#oy=int(input("1-12gacha raqamini kiriting:"))
#match oy:
#    case 1:
#        print("30-31 kundan iborat")
#    case 2:
#        print("28-29 kundan iborat")
#    case 3:
#         print("30-31 kundan iborat")
#    case 4:
#        print("30-31 kundan iborat")
#    case 5:
#        print("30-31 kundan iborat")
#    case 6:
#        print("30-31 kundan iborat")
#    case 7:
#        print("30-31 kundan iborat")
#    case 8:
#        print("30-31 kundan iborat")
#    case 9:
#        print("30-31 kundan iborat")
#    case 10:
#        print("30-31 kundan iborat")
#    case 11:
#        print("30-31 kundan iborat")
#    case 12:
#        print("30-31 kundan iborat")


#son=int(input("20-69 gacha son kiriting:"))
#match son:
 #   case 1:
 #       print("bir")
 #   case 2:
 #       print("ikki")
 #   case 3:
 #       print("uch")
 #   case 4:
 #       print("tort")
 #   case 5:
 #       print("besh")
 #   case 6:
 #       print("olti")
 #  case 7:
 #       print("yetti")
 #   case 8:
 #       print("sakkiz")
 #   case 9:
 #       print("toqiz")
 #   case 0:
 #       print("nol")
 #   case 10:
 #       print("on")
 #   case 20:
 #       print("yigirma")
 #   case 30:
 #       print("ottiz")
 #   case 40:
 #       print("qirq")
 #   case 50:
 #       print("ellik")
 #   case 60:
 #       print("oltimish")
 #   case _:
 #       print("xato")
#ranglar=['qizil','yashil','kok','siyohrang','olovrang','sariq','toqqizil']
#mashinalar=['gentra','malibu','nexia3']
#ranglar.extend(mashinalar) #biror element qoshish
#print(ranglar)
#print(mashinalar.index('gentra')) #qaysi indeksda turgani
#print(ranglar.count('malibu')) #NECH MARTA QATNASHGANI
#ranglar.sort() #alifbo tartib
#mashinalar.sort(reverse=True) #teskari tartib
#print(ranglar)

#1
#sonlar = [5, 154, 105, 250, 251]
#yigindi = sum(sonlar)
#print("Yig'indisi:", yigindi)
#2
#sonlar=[12,34,56,876,912]
#print(max(sonlar))
#3
#Ismlar=['Jahongir', 'Ali', 'Shahzod', 'Bahodir']
#Ismlar.sort()
#print(Ismlar)
#4
#ismlar=[ 'Jahongir', 'Ali', 'Shahzod', 'Bahodir']
#ismlar.sort(reverse=True)
#print(ismlar)
#5
#mevalar=('olma', 'nok', 'behi', 'olma', 'anjir', 'banan', 'olma', 'anor')
#print(mevalar.count('olma'))
#6
#sozlar=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#sozlar=sozlar[1:-1]
#print(sozlar)
#7
#ranglar=('red', 'green', 'white', 'black', 'pink', 'yellow')
#ranglar=ranglar + ('blue',)
#print(ranglar)
#8
#ismlar = ["Ali", "Anvar", "Dilshod", "Kamola", "Zilola", "Sardor"]
#ism = input("Iltimos, ismingizni kiriting: ")
#if ism in ismlar:
#    print("Ism ro'yxatda  bor.")
#else:
#    ismlar.append(ism)
#    print("Ism ro’yxatga qo’shildi.")
#print("Yangilangan ism ro'yxati:", ismlar)
#9
#sonlar=[123,43,57]
#kattasi=max(sonlar)
#sonlar.remove(kattasi)
#print("ochirilgan son.")
#print("yangi royxat",sonlar)

#10


#11
#sonlar=[234,456,876]
#kattasi=max(sonlar)
#print(kattasi)
#12
#sonlar=[2,3,4,5]
#sonlar.sort(reverse=True) #teskari tartib
#print(sonlar)

#13


#14
# 4-dars vazifalari
#1topshiriq
#1
#first_name = input("ismingizni kiriting: ")
#last_name = input("familiyangizni kiriting: ")
#2
#yashash_joy=input("Namangan viloyati Norin tumani")
#telefon=input("Redmi12")
#2topshiriq
#1
#meva='shaftoli'
#yonalish='Axborot xavfsizligi'
#print(len(meva))
#print(len(yonalish))
#3topshiriq
#1
#name="fotima"
#print(name[3])
#2
#soz='education'
#print(soz[5:8])
#3
#til='Python dasturlash tili'
#print(til[:6])
#4
#soz='String va uning methodlari'
#print(soz[::2])
#5
#til='Algorithm'
#print(til[::-1])
#6
#familiya="jaloldinova.txt"
#print(familiya[-4:][::-1])
#7
#tillar='C++,Java,Python,JS,PHP'
#print(tillar[9:-7])
#String Indexing va Slicing uchun Vazifalar
##1
#name='fotima'
#print(name[0])
#print(name[-1])
#print(name[2],name[-2])
##2
#til='Python dasturlash tili'
#1print(til[6:17])
#2print(til[::2])
#3print(til[::-1])
##3
#soz='programming'
#print(soz[:3])
#print(soz[-4:])
#print(soz[3:7])
#4
#tel_raqam=int(input("tel nomeringizni kiriting:"))
#print(split(tel_raqam))
#print(tel_raqam[1:])
###5
#ism=input('familiya kiriting:')
#print(ism[::-1])
#keyingi topshiriq
#a=int(input("a sonni kiriting:"))
#b=int(input("b sonni kiriting:"))
#print(f"{a} + {b}={a+b}")
#print(f"{a}-{b}={a-b}")
#print(f"{a}*{b}={a*b}")
#print(f"{a}/{b}={a/b}")
###vazifalar
#sonlar='8600 0804 1344 5555'
#print(sonlar.replace(" ",""))
#####
#vazifa
#1
#name='fotima'
#familiya='jaloldinova.txt'
#yosh='19'
#yashash_joyi='namangan'
#yonalish='axborot xavfsizligi'
#2
#matn='String - matn korinishidagi malumot turi'
#print(matn[::])
#print(matn[9::])
#3
#name='fotimaxon'
#print(name[::-1])
#4
#ism=input("  ismingizni kiriting:  ")
#print(f"Salom,{ism} {familiya}")
#print(ism.capitalize())
#print(ism.strip())
#5
#manzil='namangan'
#print(manzil.upper())
#6
#sozlar='jaloldinova.txt fotima egamberdi qizi'
#print(sozlar.title())
#7
#parol='98765432112345678'
#print(parol.isdigit())
#8
#ism='fotima'
#print(ism)
#ism = input("Ismingizni kiriting: ")
#if ism.startswith("A"):
#    print("Ism A harfi bilan boshlanadi.")
#else:
#    print("Ism A harfi bilan boshlanmaydi.")
#10
#11
#matn='Yaponiya chiroyli mamlakat! Yaponiyada hamma baxtli yashaydi'
#yangi=matn.replace('Yaponiya','OZBEKISTON')
#print(yangi)
#10 13 14 chiqmaganlari

##robocontest
#1
#son1 =12
#son2 =34
#yigindi=son1+son2
#print(yigindi)
#3
#A,B=map(int,input().split())
#if A>B:
#    print(">")
#elif A==B:
#    print("=")
#else:
#    print("<")
#ism=input("ismingizni kiriting:")
#print("welcome", ism, "!")
                         ##1-dars vazifalari
    #1
#ism="Fotima"
#familiya="Jaloldinova"
#print(ism,familiya)
   #2
#strga oid.Va ism b/n familiyani ekranga chiqarib beradi. print--ekranga chiqaradi.
   #3
#ism = input("ismingizni kiriting: ")
#familiya = input("familiyangizni kiriting: ")
#print("Assalomu alaykum, " + ism + " " + familiya + "!")
   #4
#yosh=int(input("yoshingizni kiriting:"))
#maktab=int(input("maktab raqamingiz:"))
#mashina="424"
#uy="7"
#barmoqlar="10"
#print("mashina raqamini kiriting:",mashina)
#print("uy raqamani:",uy)
#print("barmoqlar soni",barmoqlar)
   #5
#pi=float(input("pi:"))
#massa=float(input("massa:"))
#boy=1.64
#masofa=123.54
#kitonlar_soni=12.0
#print("boyingizni uzunligi",boy)
#print("ogirligingiz",massa)
#print("kitonlar soni",kitonlar_soni)
   #6
#name=input("ismingizni kiriting:")
#familiya=input("familiya:")
#uy_raqami="8"
#kiyimlar_soni="234"
#razmer="23"
#print("uy_raqami",uy_raqami)
#print("kiyimlar_soni",kiyimlar_soni)
#print("razmer",razmer)
   #7
#tun = True
#dars_qilyapti = True
#pasport = True
#instagram = False
#guruhda_qizlar_kop = False
#print("tun_vaqti", tun)
#print("dars", dars_qilyapti)
#print("pasport", pasport)
#print("instagram_bor", instagram)
#print("guruhda_qizlar_kop", guruhda_qizlar_kop)
                  #Set va dictionary
                ####1
#s1={"Azim","Jahongir","Xoji","Abu"}
#s2={"Xoji","Ali","Akbar","Bahrom"}
#print(s1.intersection(s2))
                ####2
#s1={"Azim","Jahongir","Xoji","Abu"}
#s2={"Xoji","Ali","Akbar","Bahrom"}
#print(s1.union(s2))
#print(s1.intersection(s2))
#print(s1.difference(s2))
#print(s1.symmetric_difference(s2))
                ####3
#sonlar={23,56,98,43,21}
#print(max(sonlar))
              ####4
#nom={"jersey":10,"club":"paxtakor","ege":28}
#for key,value in nom.items():
#    if value=="paxtakor":
#        nom[key]="neftchi"
#print(nom)

            ####5

       ####6
#sonlar = {4, 7, 2, 4, 2, 9}
#print(len(sonlar))
           ####7
#ism=input("ismingizni kiriting:")
#fan=input("fan kiriting:")
#yosh=input("yosh kiriting:")
#ustoz={"ism":ism,"fan":fan,"yosh":yosh}
#print("malumot",ustoz)
          ####8
#ustoz={"ism":"Fotima","fan":"ingliz_tili","yosh":19}
#ustoz.update({"fan":"python"})
#print("yangilangan tartib",ustoz)
            ####9
#ustoz={"ism":"Fotima","fan":"ingliz_tili","yosh":19}
#print(ustoz.values())
     ####10


#son1=int(input("1chi sonni kiriting:"))
#son2=int(input("2chi sonni kiriting:"))
#print(son1+son2)
#a=float(input("a tomonni kiriting:"))
#b=float(input("b tomonni kiriting:"))
#perimetr=2*(a + b)
#print(perimetr)

#daqiqalar=int(input("daqiqalarni kirting:"))
#soat=daqiqalar//60
#daqiqalar=daqiqalar%60
#print(soat,":", daqiqalar)
#n=int(input("sekundni kiriting:"))
#soat=n//3600
#daqiqa=n%3600
#3sekund=n//86400
#print(soat, ":", daqiqa,":", sekund)
            ####2-dasr vazifalari
#topshiriqlar
#1
#a=int(input("2xonlai son kiriting:"))
#onlik=a//10
#birlik=a%10
#print(birlik*10+onlik)
#2
#n=int(input("sekundni kiriting:"))
#soat=n//3600
#qoldiq=n%3600
#daqiqa=qoldiq//60
#sekund=qoldiq%60
#print(soat,":",daqiqa,":",sekund)
#3670=3600+60+10
#3
#yil=int(input("yilni kiriting:"))
#print(yil//100+1)
#4
#sonlar=12,34,54
#print(max(sonlar)-min(sonlar))
            ##VAZIFALAR
  #1
#yil=int(input("yilingizni kiriting:"))
#yosh=2025-yil
#print(yosh)
  #2
#a=int(input("1 sonni kiriting:"))
#b=int(input("2 sonni kiriting:"))
#print((a+b)/2)
  #3
#a=int(input("1tomonni kiriting:"))
#b=int(input("2tomonni kiriting:"))
#c=int(input("3tomonni kiriting:"))
#p=a+b+c
#print(p)
  #4
#dollor=int(input("dollorni kiring: "))
#som=dollor*12950
#print(som)
  #5#
#son=int(input("3 xonali son kiriting:"))
#yuzlik=son//100
#onlik=son//10
#birlik=son%10
#print(max(yuzlik,onlik,birlik))
  #6
#a=int(input("a tomonni kiriting:"))
#b=int(input("b tomonni kiriting:"))
#s=a*b
#p=2*(a+b)
#print(s)
#print(p)
  #7
#son=int(input("son kiriting:"))
#n=son**2
#n1=son**3
#print(n,n1)
  #8
#son1=int(input("1chi sonni kiriting:"))
#son2=int(input("2chi sonni kiriting:"))
#yigindi=son1+son2
#ayirma=son1-son2
#kopaytma=son1*son2
#bolinma=son1//son2
#print(yigindi,ayirma,kopaytma,bolinma)
  #9
#selsiy=int(input("selsiyni kiriting:"))
#F=1.8 * selsiy + 32
#print(F)
  #10
#son=int(input("3 xonali son kiriting:"))
#yuzlik=son//100
#onlik=(son//10)%10
#birlik=son%10
#yigindi=yuzlik+onlik+birlik
#print(yigindi)
  #11
#a=int(input("a sonnni kiriting:"))
#b=int(input("b sonnni kiriting:"))
#a, b = b, a
#print(a, b)

#nom={"jersey":10, "club":"paxtakor","age":28}
#print(nom.items())



#def salomlashish():
#    print("Assalomu alaykum")
#salomlashish()
#def toliq_ism():
#    ism=input("ismingizni kiriting:")
#    familiya=input("familiyangizni kiriting:")
#    print(f"{ism} {familiya}")
#toliq_ism()
#def daraja(son,daraja):
#    print(son**daraja)
#daraja(3,4)
#daraja(6,7)
#daraja(8,9)
#daraja(5,4)
#daraja(2,9)
#daraja(12,6)
                 #40ta masala
#1
# a=int(input("a tomonini kiriting:"))
#p=4*a
#print(p)
#2
#a=int(input("a tomonini kiriting:"))
#s=a**2
#print(s)
#3
#a=int(input("a tomonini kiriting:"))
#b=int(input("b tomonini kiriting:"))
#s=a*b
#p=2*(a+b)
#print(s)
#print(p)
#4
#d=int(input("diametrni kiriting:"))
#l=3.14*d
#print(l)
#5
#a=int(input("a tomonini kiriting:"))
#s=6*a**2
#v=a**3
#print(s)
#print(v)
#6
#a=int(input("a tomonini kiriting:"))
#b=int(input("b tomonini kiriting:"))
#c=int(input("c tomonini kiriting:"))
#v=a+b+c
#s=2*(a*b+c*b+a*c)
#print(v)
#print(s)
#7
#r=int(input("radiusni kiriting:"))
#l=6.28*r
#s=3.14*r**2
#print(l)
#print(s)
#8
#a=int(input("a tomonini kiriting:"))
#b=int(input("b tomonini kiriting:"))
#ortasi=(a+b)/2
#print(ortasi)
#9
#a=int(input("a tomonini kiriting:"))
#b=int(input("b tomonini kiriting:"))
#math.sqrt(a*b)
#print()   # ildiz qana boladi pythonda
#10
#a=int(input("a sonni kiriting:"))
#b=int(input("b sonni kiriting:"))
#print(a+b)
#print(a*b)
#print(a**2+b**2)
#11
#a=int(input("a sonni kiriting:"))
#b=int(input("b sonni kiriting:"))
#rint(a+b)
#print(a*b)


#12
#n1=input("n1 sonni kiriting:")
#n2=input("n2 sonni kiriting:")
#n3=input("n3 sonni kiriting:")
#p=n1+n2+n3
#c=math.sqrt(n1**n2**2)
#print(p)
#print(c)


#13
#R1=int(input("R1 sonni kiriting:"))
#R2=int(input("R2 sonni kiriting:"))
#pi=3.14
#S1=pi*R1
#2=pi*R2
#S3=pi*(R1-R2)
#print(S1)
#print(S2)
#print(S3)
#14
#L=int(input("uzunlikni kiriitng:"))
#R=L/6.28
#S=3.14*R
#print(R)
#print(S)
#15
#import math
#pi=3.14
#S = float(input("Yuzani kiriting: "))
#R = math.sqrt(S / math.pi)
#print("Radius:", R)
#16
#x1=int(input("x1 ni kiriting:"))
#x2=int(input("x2 ni kiriting:"))
#masofa=abs(x2-x1)
#print("uzunlik:",masofa)
#25
#x = int(input("x sonni kiriting: "))
#print(3 * ((x**6) - 6 * (x**2) - 7))
#26
#x = int(input("x sonni kiriting: "))
#print(4*((x-3)**6)-7*((x-3)**3)+2)
#27
#a=int(input("a sonni kiriting:"))
#print((a**2),(a**4),(a**8))
#28
#a=int(input("a sonni kiriting:"))
#print((a**2),(a**3),(a**5),(a**10),(a**15))
#29
#import math
#gradus=float(input("gradusni kiriting: "))
#radian=gradus*math.pi/180
#print("radianda",radian)
#30
#import math
#radian=float(input("radianni kiriting:"))
#gradus=radian*180/math.pi
#print("gradus",gradus)
#31
#t1=float(input("t1 ni kiriting:"))
#t2=(t1-32)*(5/9)
#print(t2)
#32 31 bilan bir xil ekan
#33
#x=int(input(" kg ni kiriitng:"))
#a=int(input("konfet narxini kiriitng;"))
#y=a/x
#print(y)
#38
#a=int(input("a sonni kiriting:"))
#b=int(input("b sonni kiriting:"))
#x=-(b/a)
#print(x)
#39
#import math
#a = int(input("a ni kiriting: "))
#b = int(input("b ni kiriting: "))
#c = int(input("c ni kiriting: "))
#D = b**2 - 4*a*c
#x1 = (-b + math.sqrt(D)) / (2 * a)
#x2 = (-b - math.sqrt(D)) / (2 * a)
#print("x1 =", x1)
#print("x2 =", x2)
#40
#a1=int(input("a1 sonni kiritng:))
#b1=int(input("b1 sonni kiritng:))"))
#a2=int(input("a2 sonni kiritng:"))
# b2=int(input("b2 sonni kiritng:"))
#c2=int(input("c2 sonni kiritng:"))
#x=int(input("x sonni kiritng:"))
#y=int(input("y sonni kiritng:"))
#d=(a1*b2-a2*b1)
#print()
#34
#x=float(input("shokoland miqdori:"))
#a=float(input("summa miqdori:"))
#y=float(input("konfet miqdori:"))
#b=float(input("summa konfet:"))
#print

#print(math.sqrt(121))
#print(math.pow(2,6))
#print(math.factorial(12))
#print(math.fabs(-45))
#print(math.fabs(45))
                  #10-DARS VAZIFALARI FUNKSIYALAR
    #1
#def salomlash():
#    print("salom bolajonlar!")
#salomlash()
    #2
#def max_tanla():
#    ismlar=["fotima","sanamgul","rano","gulmira"]
#    ism=max(ismlar,key=len)
#   print(ism)
#max_tanla()
    #3
#def ortacha_baho():
#    baholar=[12,23,56,83,28]
#    baho=sum(baholar)/len(baholar)
#    print(baho)
#ortacha_baho()
    #4
#def min_tanla():
#    ismlar=["fotima","sanamgul","rano","gulmira"]
#    ism=min(ismlar,key=len)
#    print(ism)
#min_tanla()
    #5
#def teskari_tartib():
#    ism="fotimaxon"
#    teskari_tartib=ism[::-1]
#    print(teskari_tartib)
#teskari_tartib()


    #6

   #7
#def eng_kattasi():
#    sonlar=[456,876,278]
#    print(sonlar, max(sonlar))
#eng_kattasi()
    #8
#def kubni_hisobla():
#    sonlar=int(input("sonni kiriting:"))
#    son=pow(sonlar,3)
#    print("son =",son)
#kubni_hisobla()
    #9
#def juft_toqlik():
#   son = int(input("Son kiriting: "))
#    if son % 2 == 0:
#        print("juft son.")
#    else:
#        print("toq son.")

#juft_toqlik()
    #10
#def katta_harflarda():
#    ism="Fotima"
#    print(ism.upper())
#katta_harflarda()
#                                                   FAKTORYAL
#def factorial(son: int):
#   if son == 1:
#        return 1
#    else:
#        return son * factorial(son - 1)
    #               yigindi


#def yigindi(toplam:list):
#    if len(toplam) == 0:
#        return 0
#    else:
#        return toplam.pop() + yigindi(toplam)
#sonlar=[1,2,3,4,5]
#print(yigindi(sonlar))
                                  #butun sonlar ustida amallarni barajarish
  #1
#l=int(input("l ni kiriting (sm):"))
#metr=l/100
#print(metr)
  #2
#m=int(input("m ni kiriting(kg):"))
#tonna=m/1000
#print(tonna)
  #3
#hajm=int(input("hajmni kiriting:"))
#kilobayt=hajm/1024
#print(kilobayt)
  #4 5 birxil ekan
  #6
#son=int(input("2 xonali son kiriting:"))
#onlik=son//10
#birlik=son%10
#print("onlik", onlik,"birlik",birlik)
  #7
#son=int(input("2 xonali son kiriting:"))
#onlik=son//10
#birlik=son%10
#a=onlik+birlik
#print(a)
  #8
#son=int(input("2 xonali son kiriting:"))
#onlik=son//10
#birlik=son%10
#onlik,birlik=birlik,onlik
#print(onlik,birlik)
  #9
#son=int(input("3 xonalani son kiriting:"))
#yuzlik=son//100
#rint(yuzlik)
  #10
#son=int(input("3 xonalani son kiriting:"))
#onlik=son//10%10
#birlik=son%10
#print(birlik,onlik)
  #11
#son=int(input("3 xonali son kiriting:"))
#yuzlik=son//100
#onlik=son//10%10
#birlik=son%10
#a=yuzlik+onlik+birlik
#print(a)
  #12
#son=int(input("3 xonali son kiriting:"))
#yuzlik=son//100
#onlik=son//10%10
#birlik=son%10
#yuzlik,onlik,birlik=birlik,onlik,yuzlik
#print(yuzlik,onlik,birlik)
  #13
#son = int(input("3 xonali son kiriting: "))
#yuzlik = son // 100
#onlik = (son // 10) % 10
#birlik = son % 10
#yangi_son = (son // 10) + (birlik * 100)
#print(yangi_son)

   #14

  #15
#son = int(input("3 xonali son kiriting: "))
#yuzlik = son // 100
#onlik = (son // 10) % 10
#birlik = son % 10
#yuzlik,onlik,birlik=onlik,yuzlik,birlik
#print(yuzlik,onlik,birlik)
  #16
#son = int(input("3 xonali son kiriting: "))
#yuzlik = son // 100
#onlik = (son // 10) % 10
#birlik = son % 10
#yuzlik,onlik,birlik=yuzlik,birlik,onlik
#print(yuzlik,onlik,birlik)
  #17
#sonlar=int(input(" 4 xonali son kiriting:"))
#yuzlik=(sonlar//100)%10
#print(yuzlik)
  #18
#sonlar=int(input(" 4 xonali son kiriting:"))
#minglik=(sonlar//1000)
#print(minglik)
  #19
      # DARS VAZIFALARI
   #1
#radius=float(input(" doira radiusini kiriting: "))
#s=3.14*(radius**2)
#l=2*3.14*radius
#print(s,l)
   #2
#yosh=int(input("yoshingizni kiriting:"))
#yil=2025-yosh
#print(yil)
   #3
#son=int(input("1-9 son kiriting:"))
#print(factorial(son))
   #4
#import math
#a=int(input("a sonni kiriting:"))
#b=int(input("b sonni kiriting:"))
#c=math.sqrt(a**2+b**2)
#print(c)
                      #  4 dars mashgulot
#manzil="Namangan viloyati Norin tumani Toshqin QFY Shohidon MFY "
#print(len(manzil))
#familiya_ism="Jaloldinova Fotima"
#print(len(familiya_ism))
#name="fotimaxon"
#print(name[0])
#print(name[-3:])
#print(name[0:6])
#1
#name="fotima"
#print(name[3])
#2
#soz="education"
#print(soz[5:9])
#3
#matn="python dasturlash tili"
#print(matn[0:7])
#4
#satr="string va methodlari"
#print(satr[1::2])
#5
#soz="algorithm"
#print(soz[::-1])
#6
#familiya="Jaloldinova"
#print(familiya[-4:])
#7
#sozlar="C++,Java,Python,JS,PHP"
#print(sozlar[9:15])
                #rekuvsiv funksiya
  #1
#def salomlashish():
#    print("salom bolajonlar!")
#salomlashish()
  #2
#def max_tanla():
#    ismlar = ["fotima", "rano", "gulmira", "sanamgul"]
#    ism=max(ismlar,key=len)
#    print(ism)
#max_tanla()
  #3
#def baho():
#    baholar=[12,34,67,89,123,456,789]
#    ortacha=sum(baholar)//len(baholar)
#    print(ortacha)
#baho()
  #4
#def ism_kichigi():
#    ismlar=["fotima","guli","mohira","gulzira"]
#    ism=min(ismlar,key=len)
#    print(ism)
#ism_kichigi()
  #5
#def teskari_tartib():
#    ism="fotimaxon"
#    print(ism[::-1])
#teskari_tartib()
   #6  for nima vazifani bajaradi: nega faqat 1tadan chiqqaryapti
#def musbat_manfiy(a, b, c,d):
#    musbat = 0
#    manfiy = 0
#    for son in [a, b, c,d]:
#        if son > 0:
#            musbat = son
#        elif son < 0:
#            manfiy = son
#    print(f"Musbat : {musbat}")
#    print(f"Manfiy : {manfiy}")
#musbat_manfiy(12,-5,8,-4)
   #7
#def qosh_dictga(dictionary, key, value):
#    dictionary[key] = value
#    return dictionary
#my_dict = {'ism': 'fotima', 'yosh': 19}
#yangilangan_dict = qosh_dictga(my_dict, 'kasb', 'dasturchi')
#print(yangilangan_dict)
   #8
#def aniqla(son, boshi, oxiri):
#    return boshi <= son <= oxiri
#print(aniqla(15,89,78))
#print(aniqla(15,56,71))
#print(aniqla(19,56,71))
#print(aniqla(19,56,11))
   #1 rekursif funksiyada ishlolmayapman
#ism="fotimaxon"
#print(ism[::-1])
   #2
#son=[12,56,98742]
#print(max(son))
   #3
#son=int(input("sonni kiriting:"))
#print(son**1,son**2,son**3)
   #4
#son=int(input("son kiriting:"))
#if son%2==0:
#    print("juft son")
#else:
#    print("toq son")
   #5
#def katta_harfda(ism):
#    return ism.upper()
#print(katta_harfda("fotima"))
#print(katta_harfda("jaloldinova.txt"))
  #6
#sonlar=[12,36,45,98]
#print(sum(sonlar))
   #7
#def bosh_joy(ism):
#     return ism.strip()
#print(bosh_joy("  fotima  "))
                 #leedcode
    #326
#n=27
#if n**3:
#    print("True")
#elif n==0:
#    print("False")
#else:
#    print("False")
   #342
#n=int(input("n ni kiriting:"))
#if n%4==0:
#    print("True")
#else:
#    print("False")
   #344
#ism="fotimaxon"
#print(ism[::-1])
   #509--------------

       #imtihondagilar
#1
#son="5679824"
#natija=son[:5]
#print(natija)
#2
#sonlar=[1,2,2,36,78,54,2]
#x=int(input("x ni kiriting:"))
#natija=sonlar.count(x)
#print(natija)
#3
#son1=int(input("1 chi son kiriting:"))
#son2=int(input("2 chi son kiriting:"))
#son3=int(input("3 chi son kiriting:"))
#if son1%2==0:
#    print("juft son")
#else:
#    print("toq son")
#if son2%2==0:
#    print("juft son")
#else:
#    print("toq son")
#if son3%2==0:
#    print("juft son")
#else:
#    print("toq son")
#4
#matn=input("matn kiriting:")
#print(matn.replace(".", ","))
#5
#a=int(input("a sonni kiriting:"))
#onlik=a//10
#birlik=a%10
#onlik,birlik=birlik,onlik
#print(onlik,birlik)
#6
#ismlar=["fotima","maftuna","gullola","asilbek"]
#natija=sorted(ismlar)
#print(natija)
#7
#son=int(input("3 xonali son kiriting:"))
#yuzlik=son//100
#onlik=son//10%10
#birlik=son%10
#yuzlik,onlik,birlik=birlik,onlik,yuzlik
#print(yuzlik,onlik,birlik)
#8

#9
#son=input("son kiriting:")
#xona=len(son)
#print("raqamlar soni:", xona)
#10
#import random
#import math
#son=random.randint(1,50)
#print(f"{son}!={math.factorial(son)}")
#11
#ismlar=["fotima","gullola","rano","sanamgul"]
#ism=input("ism kiriting:")
#if ism in ismlar:
#    print("allaqachon mavjud")
#else:
#    ismlar.append(ism)
#    print("royxatga qoshildi")
#print(ismlar)
#12
#sonlar=[1,23,56,43,12]
#natija=((sum(sonlar)-max(sonlar)-min(sonlar))/(len(sonlar)-2)
#print(natija)
#13

#21
#son=[12,13,14]
#juft=son%2==0
#print("juft",juft)
#toq=son%2!=0
#print("toq",toq)

                # dars
#topshiriq
#product = "telefon"
#price = 100
#discount = 15
#print(f"{product} asl narxi ${price:.2f},{discount}% chegirmadan song, ${price -(price/100*discount):.3f}")
  #topshiriq
# find bn index bir xil vazifani barajaradi.
                #1
#name="fotima"
#print(name.upper())
#print(name.lower())
#print(name.title())
#print(name.capitalize())
#print(name.find('a'))
#print(name.index('m'))
#print(name.count('t'))
                 #dars
#1
#for i in range(5):
#    ism=input("ismingizni kiriting:")
#    print(ism)
#2
#sonlar=[1,12,15,56,8]
#yigindi=0
#for son in sonlar:
#    yigindi +=son
#print("yigindi",yigindi)
#3
#for i in range(20, 9, -1):
#    print(i, end=" ")
#4

       #4 dars  vazifalari
#String Indexing va Slicing uchun Vazifalar
#1
#ism=input("ismingizni kiriting:")
#print(ism[0])
#print(ism[-1])
#print(ism[2])
#print(ism[4])
#2
#matn="Python dasturlash tili"
#print(matn[7:17])
#print(matn[1::2])
#print(matn[::-1])
#3
#soz= "programming"
#print(soz[0:3])
#print(soz[-4:]) #:-4 boshini chiqaradi,-4: oxiridan chiqari
#print(soz[3:7])#1ta 2ta nuqta bolsa orasida sozni oladi,2ta nuqta bolsa tashab oladi
#4
#raqam = input("Telefon raqamingizni kiriting: ")
#togrilangan=raqam.replace("+","").replace(" ","")
#print(togrilangan)
#print(-4:)
#5
#familiya=input("familayangizni kiriting:")
#print(familiya[::-1])
        #qoshimcha
#1
#ism="fotima"
#famila="jaloldinova.txt"
#manzil="namangan"
#yonalish="axborot xavfsizlifgi"
#shahar="xaqqulabod"
#2
#matn = "String matn korinishidagi malumot turi"
#print(len(matn))
#print(matn[9:])
#3
#ism="fotimaxon"
#print(ism[::-1])
#4
#ism_familiya=input("ism familiyangizni kiriting:")
#print(f"{ism_familiya.capitalize()} ")
#print(ism_familiya.replace(" ",""))
#5
#manzil="namangan"
#print(f"{manzil.upper()}")
#6
#sozlar=("fotima").title()
#sozlar1=("lola").title()
#sozlar2=("guli").title()
#print(sozlar,sozlar1,sozlar2)
#7
#parol=input("parol kiriting:")
#print(parol.isalnum())
#8
#ism=input("ismngizni kiriting:")
#print(ism.startswith("A"))
#9 fikr yurit--------------------------------------------------------------------------------------------------------------------------------------------
#abc = 'abcdefghijklmnopqrstuvxyz'
#start=abc.index("g")
#end=abc.index("t")+1
#print(start,end)
#10
#raqamlar='123456789'
#print(raqamlar[1::2])
#11
#matn = "Yaponiya chiroyli mamlakat! Yaponiyada hamma baxtli yashaydi"
#print(matn.replace('Yaponiya', 'O‘zbekiston').replace('Yaponiyada', 'O‘zbekistonda'))
                     #qoshimcha uchun
#1
#ism="fotimaxon"
#sm1="rano"
#print(ism.capitalize())
#print(ism.casefold())
#print(ism.center(2,"*"))
#print(ism.count("o"))
#print(ism.encode())
#print(ism.endswith("on"))
#print(ism.expandtabs(7))
#print(ism.find("on"))
#print(ism.format("rano"))
#print(ism.isalpha())
#print(ism.isdigit())
#print(ism.isdecimal())
#print(ism.isidentifier())
#print(ism.islower())
#print(ism.isupper())
#print(ism.join(ism1))
#rint(ism.lower())
#print(ism.lstrip())
#print(ism.replace("fotimaxon","rano"))
#print(ism.removeprefix("fotimaxon"))
#print(ism.removesuffix("foti"))
#print(ism.rstrip)
#print(ism.splitelines())
#print(ism.startswith("fotima"))
#print(ism.strip("fotima"))
#print(ism.swapcase())
                     #39 guruhdaghi vazifalar
            #1-tashalgan masalalar
#1
#sonlar=[1,2,3,4]
#for son in sonlar:
#    kvadrar=son**2
#    print(f"{son} ning kvadrati: {kvadrar}")
#2---
#for i in range(2, 10):
#    print(f"\n{i} ning karra jadvali:")
#    for j in range(1, 11):
#        print(f"{i} x {j} = {i * j}")
#3
#son=int(input("son kiriting:"))
#if son%3==0 and son%5==0:
#    print("FizzBuzz")
#elif son%3==0:
#    print("Buzz")
#elif son%5==0:
#    print("Fizz")
#else:
#    print("son")
#4 #5---------
#6
#k=int(input("k sonni kiriting:"))
#n=int(input("n sonni kiriting: (qancha chiqarish)"))
#for i in range(n):
#    print(k)
#7------
#n=int(input("n sonini kiriting:"))
#S = sum((n + i)**2
#        for i in range(n + 1))
#print(f"S = {S}")
#8------
#n=int(input("n sonni kiriting:"))
#S=sum(1/n+1)
#for i in range(n):
#print(f"S={S}")
#9
#for i in range(1,6):
#    for j in range(1,i+1):
#        print(j,end=" ")
#    print()
#10
#sonlar=[12,5,90,27,3]
#for son in sonlar[::-1]:
#    print(son)
#11
#for i in range(-10,0):
#    print(i)
#12--------------------------------
#13--------------------------------
#for n in range():
#    print(factorial(n))
#14 15------------





    # 6 dars SHART OPERATORLARI= IF,ELSE,ELIF
#1
#a=int(input("a sonnni kiriting:"))
#b=int(input("b sonnni kiriting:"))
#if a>b:
#    print("a katta b dan")
#else:
#    print("b katta a dan ")
#2
#hafta=int(input("1-7 gacha son kiriting:"))
#if hafta==1:
#    print("dushanba")
#elif hafta==2:
#    print("seshanba")
#elif hafta==3:
#    print("chorshanba")
#elif hafta==4:
#    print("payshanba")
#elif hafta==5:
#    print("juma")
#elif hafta==6:
#    print("shanba")
#elif hafta==7:
#    print("yakshanba")
#else:
#print("bundan hafta kuni yoq")
#3
#fam=input("familiyangizni kiritiing:")
#if fam.endswith("va"):
#    print("siz qiz bolasiz")
#elif fam.endswith("v"):
#    print("siz ogil bolasiz")
#else:
#    print("xato familiya!")
#4
#age=int(input("yoshingizni kiriting:"))
#millat=input("millatingizni kiriting:")
#if age>=18 and millat=="ozbek":
#    print("siz ovoz berishngiz mumkin")
#else:
#    print("mumkin emas!")

#5
#yosh=int(input("yoshingizni kiriting:"))
#maosh=int(input("maoshingiz kiriting:"))
#if yosh>=20 and maosh==700:
#    print("sizga mumkin!")
#else:
#    print("mumkin emas!")
   # VAZIFALAR 41-guruh. SHART OPERATORLARI
#1
#son=int(input("son kiriting:"))
#if son%2==0:
#   print("juft son")
#else:
#    print("toq son")
##2
#temp=int(input("temp kiriting:"))
#if temp>36.6:
#    print("yaxshi emas")
#elif temp<36.6:
#    print("bu ham yaxshi emas")
##3
#son=(12,36,98)
#print(min(son))
##4
#temp=int(input("temp kiriting:"))
#if temp<36:
#    print("harorat juda past")
#    print("harorat normal")
#lif temp>=38:
#    print("yengil istma")
#elif temp>38:
#    print("haroratingiz yomon shifokorga boglaning:")
#else:
#    print("bunday istma yo")
#5
#son=int(input("son kiriting:"))
#if son>0:
#    print("musbat son")
#elif son==0:
#    print("nomusbat")
#else:
#    print("manfiy son")
#6
#baho=int(input("bahoni kiriting:"))
#if baho<31:
#    print("1 baho")
#elif baho>32:
#    print("2 bahoni")
#elif baho>55:
#    print("3 bahoni")
#elif baho>71:
#    print("3 bahoni")
#elif baho>86:
#    print("4 bahoni")
#else:
#    print("5 bahoni")
##7
#hafta=int(input("1-7 gacha son kiriting:"))
#if hafta==1:
#    print("dushanba")
#elif hafta==2:
#    print("seshanba")
#elif hafta==3:
#    print("chorshanba")
#elif hafta==4:
#    print("payshanba")
#elif hafta==5:
#    print("juma")
#elif hafta==6:
#elif hafta==7:
#    print("yakshanba")
#else:
##8
#harf=input("harf kiriting:")
#unli=("a","e","i","o","u","o'",)
#if harf in unli:
#    print("unli harf")
#lse:
#    print("undosh harf")
#9
#yil=int(input("yil kiriting:"))
#if yil%4==0:
#    print("kasiba yili")
#else:
##    print("kasiba yili emas")
#10
#son1=int(input("son1 kiriting:"))
#son2=int(input("son2 kiriting:"))
#son3=int(input("son3 kiriting:"))
#if son1+son2>son3:
#   print("uchburchak yasash mumkin")
#elif son1+son3>son2:
##    print("uchburchak yasash mumkin")
#elif son2+son3>son1:
#    print("chubuchak yasash mumkin")
#else:
#    print("mumkin emas!")
##11
#oy_raqami=int(input("oy raqamini kirting:"))
#if oy_raqami==1:
#    print(" yanvar 31-kun")
#elif oy_raqami==2:
#    print("fevral 28-kun")
#elif oy_raqami==3:
#    print("mart 30-kun")
#elif oy_raqami==4:
#    print("aprel 31-kun")
#elif oy_raqami==5:
#    print("may 30-kun")
#elif oy_raqami==6:
#    print("iyun 31-kun")
#elif oy_raqami==7:
#    print("iyul 30-kun")
#elif oy_raqami==8:
#    print("avgust 31-kun")
#elif oy_raqami==9:
#    print("sentyabr 30-kun")
#elif oy_raqami==10:
#    print("oktyabr 31-kun")
#elif oy_raqami==11:
#    print("noyabr 30-kun")
#elif oy_raqami==12:
#    print("dekabr 31-kun")
#else:
#    print("bunday oy yoq")
#12
#son1 = int(input("son1 ni kiriting: "))
#son2 = int(input("son2 ni kiriting: "))
#amal = input("Amalni kiriting (+, -, /, *): ")
#if amal == "+":
#    print(son1 + son2)
#    print(son1 - son2)
#elif amal == "/":
#    print(son1 / son2)
#elif amal == "*":
#    print(son1 * son2)
#else:
#    print("Noto‘g‘ri amal!")

                  #qoshimcha 33ta masala
#1
#for i in range(1,11):
#    print(i)
#2
#for son in range(2, 21, 2):
#    print(son)
#3
#print(sum(range(1, 101)))
#4
#soz="salom"
#for i in range(5):
#    print(soz)
#5
#soz="python"
#for harf in soz:
#    print(harf)
#6
#sozlar=["fotima","rano","guli","lola"]
#for harf in sozlar:
#    print(harf)
#7
#for son in range(1,11):
#    print(son**2)
#8
#for son in range(2,51):
#    if son%3==0:
#      print(son)
#9----------------------------------
#sonlar=[24,3,56,78,43]
#natija=1
#for son in sonlar:
#    natija *= son
#print("sonlar kopaytmasi:",natija)
#10 nechtaligini qaydan bilsa boladi
#for i in range(-12,13):
#    if i>0:
#        print(i)
#11
#sonlar=[12,23,45,65,1]
#for son in sonlar:
#    natija=sum(sonlar)
#print(natija)
#12
#for  son in range(10,0,-1):
#    print(son)
#13--------------------------------------
#14
#soz="fotimaxon"
#for i in soz[::-1]:
#    print(i)
#15
#for i in range(2,10):
#    for j in range(2,10):
#        print(f"{i} x {j} = {i * j}")
#    print()
#16
#sonlar=[1,2,3,45,6]
#for i in sonlar:
#    natija1=max(sonlar)
#    natija2=min(sonlar)
#    print(natija1,natija2)
#17
#a=int(input("a sonni kiriting:"))
#b=int(input("b sonni kiriting:"))
#for i in range(a,b+1):
#   print(i)
#18
#a=int(input("a sonni kiriting:"))
#b=int(input("b sonni kiriting:"))
#natija=sum(range(a,b+1))
#print("yigindi:",natija)
#19 18 bilan ekan
#20
#matn="kuz juda gozal fasl"
#for i in matn:
#    print(i)
#21
#son=int(input("son kiriting:"))
#if son%3==0 and son%5==0:
#    print("FizzBuzz")
#elif son%3==0:
#    print("Buzz")
#elif son%5==0:
#    print("Fizz")
#else:
#    print("son")
#25
#matn="salom yaxshimisiz darsga borasizmi"
#sozlar=matn.split()
#print(sozlar)
#for soz in sozlar:
#    print(len(soz))
#22
#son=int(input("son kiriting:"))

#k = 1
#for i in range(1, son + 1):
#    k = k * i
#print(k)
#23
#son=[1,23,45,65]
#for i in son[::-1]:
#    print(i)
#24
#matn="kuz chiroyli fasl"
#unli=0
#ndosh=0
#unlilar="aeiou"
#undoshlar="qrtypdsfghjklzxvbnmc"
#for i in matn:
#    if i in unlilar:
#        unli+=1
#    if i in undoshlar:
#        undosh+=1
#print(unli)
#print(undosh)
#25
#matn="kuz chiroyli fasl"
#sozlar=matn.split()
#print(sozlar)
#for soz in sozlar:
#    print(len(soz))
#26
#n=23
#for i in range(1,n+1):
#    print('*' * i)
#28
#n=5
#for i in range(1,n+1):
#    for j in range(1,n+1):
#        print(j, end=" ")
#   n=n-1
#    print()
#29
#matn="kuz chiroyli fasl"
#sozlar=matn.split()
#print(sozlar)
#for soz in sozlar:
#    print(len(soz))
#print(min(matn))
#print(max(matn))
            #tanlash operatori
#1
#hafta=input("hafta:(1-7gacha)")
#match hafta:
#    case "1":
#        print("dushanba")
#    case "2":
#        print("seshanba")
#    case "3":
#        print("chorshanba")
#    case "4":
#        print("payshanba")
#    case "5":
#        print("juma")
#    case "6":
#        print("shanba")
#   case "7":
#        print("yakshanba")
#2
#baho=input("baho:(1-5gacha)")
#match baho:
#    case "1":
#        print("yomon")
#    case "2":
#        print("qoniqarsiz")
#    case "3":
#        print("qoniqarli")
#    case "4":
#        print("yaxshi")
#   case "5":
#        print("a'lo ")
#    case _:
#        print("xato")
#3
#oy=input("oyni kiriting:(1-12gacha)")
#match oy:
#    case "yanvar"|"fevral"|"dekabr" :
#   case "mart"|"aprel"|"may" :
#        print("bahor")
#    case "iyun"|"iyul"|"avgust" :
#        print("yoz")
#    case "senyabr"|"octabr"|"noyabr" :
#        print("kuz")
#    case _:
#        print("bunday oy yoq")
#4
#oy=input("oyni kiriting:(1-12gacha)")
               #list va tuple
#append(),insert()
#telefonlar=['redmi','ayfon','nokia','samsung']
#telefonlar.append('poco')
#telefonlar.insert(0,'realmi')
#print(telefonlar)
# remove()
#telefonlar=['redmi','ayfon','nokia','samsung']
#telefonlar.remove('nokia')
#print(telefonlar)
#pop()
#telefonlar=['redmi','ayfon','nokia','samsung']
#telefonlar.pop(2)
#print(telefonlar)
#clear()
#telefonlar=['redmi','ayfon','nokia','samsung']
#telefonlar.clear()
#print(telefonlar)
#sorted tartiblanmedi sort tartiblab chiqaradimi
                        #while loop
                        #topshiriqlar
#
#son=1
#while son<11:
#    print(son)
#    son+=1
#
#son=int(input("son kiriting:"))
#print(factorial(son))
#
#son=int(input("sonni kiriting:"))
#natija=1
#i=1
#while i<=son:
#    natija*=i
#    i+=1
#print(natija)
#oxirgi topshiriq-----------------------------------------
# vazifa dars
#1
#son=2
#while son < 5:
#    son=son+1
            #VAZIFALAR 41 GURUHDAGI
#1
#sonlar=[1,34,67,98,23,4]
#print(sum(sonlar))
#2
#sonlar=[34,67,54,112,90,349]
#print(max(sonlar))
#3
#sozlar=['fotima','guli','lola','anora']
#sozlar.sort()
#print(sozlar)
#4
#sozlar=['fotima','guli','lola','anora']
#sozlar.sort()
#print(sozlar[::-1])
#5
#fruits=['olma','nok','behi','olma','anjir','banan','olma','anor']
#print(fruits.count('olma'))
#6
#ranglar= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#ranglar.pop(0)
#ranglar.pop(-1)
#print(ranglar)
#7
#ranglar=['red', 'green', 'white', 'black', 'pink', 'yellow']
#ranglar.append('blue')
#print(ranglar)
#8
#ismlar=["fotima","guli","lola","anora"]
#ism=input("ism kiriting:")
#if ism in ismlar:
#    print("ism listda bor")
#else:
#    print(ismlar.append(ism)) #none berayapti negadir
#    print("ism royxatga qoshildi")
#print(ismlar)
#9
#sonlar=[1,34,67,98,23,4]
#sonlar.pop(sonlar.index(max(sonlar)))
#print(sonlar)
#10 mazmuni ozgina tushunarsiz----------
#my_list = []
#element1 = input("1-elementni kiriting: ")
#element2 = input("2-elementni kiriting: ")
#my_list.append(element1)
#my_list.append(element2)
#natija= my_list[1].isupper()
#print(natija)
#11
#sonlar=[1,34,67,98,23,4]
#print(max(sonlar))
#12
#sonlar=[1,34,67,98,23,4]
#print(sonlar[2:5])
#13------------------------
#ismlar=['fotima','guli','lola','anora']
#ismlar = [ism for ism in ismlar if len(ism) >= 6]
#print(ismlar)
#14
#sonlar = [10, 25, 30, 45, 50]
#son = int(input("Son kiriting: "))
#if son in sonlar:
#    print(sonlar.index(son))
#else:
#    print("Yo'q")
#15-----------------------
#while True:
#    buyruq=input("buyruqni yozing:")
#    if buyruq.lower()=='stop':
#        print("toxtatildi.")
#        break
#    else:
#        print("ishlayapti")
                # errorlar
#try:
#    a=int(input("a="))
#    b=int(input("b="))
#    natija=a/b
#    print(natija)
#except ZeroDivisionError:
#    print("nolga bolish mumkin emas")
#except ValueError:
#    print("faqat butun son kiriting:")
#try:
#    kurslar = ['Backend', 'Frontend', 'Flutter', 'Grafik Dizayn', 'Kiberxavfsizlik', 'Savodxonlik', "Sun'iy intelekt"]
#    index=int(input("qaysi kursda oqimoqchisz:(0-6)"))
#    print(kurslar[index],"-zor tanlov!")
#except Exception as error:
#    print(error)
#            # zero division error
#try:
#    a=int(input("1 son kiriting:"))
#    b=int(input("2 son kiriting:"))
#    natija=a/b
#   print(natija)
#except ZeroDivisionError:
#    print("mumkin emas.Noldan boshqa songa bol.")
#        # key errror
#try:
#    mevalar={
#        "olma":24,
#        "behi":34}
#    print(mevalar['uzum'])
#except KeyError:
#    print("xato")
#3yosh=int(input("yoshingizni kiriting:"))
#if yosh<150 or yosh <0:
#    raise Exception("YOSH FAQAT 0-150 ORALIGIDA BOLISHI KK")
#print(f"{2025-yosh}-yilda tugulganmisiz?)

#ism=input("ismingizni kiriitng:")
#if len(ism)<3:
#    raise Exception("ism kamida 3ta harfdan iborat bolishi kerak")
#elif not ism.isalpha():
#    raise Excepti
               #dars vazifalari-13
#1
#   ism=['fotima','guli','lola']
#   print(ism[4])
#2
#gullar={
#    "lola":45,
#    "atirgul":32,
#    "moychechak":12}
    #print(gullar['binafsha'])
#3
#son=5
#ism='fotima'
#print(son+ism)
#4
#ismlar={'fotima':6,'sanamgul':8,'guli':4}
#try:
#    print(ismlar['durdona'])
#except KeyError:
#    print("xato, bunday ism topilmadi")
#5
#a=int(input('a='))
#b=int(input('b='))
#try:
#    print(a/b)
#except ZeroDivisionError:
#    print("sonni nolga bolib bomeydiku do'stim")
#6
#ism=['fotima','guli','lola']
#ism1=input("ism kiriiting:")
#if ism1 in ism:
#    print(ism.remove(ism1))
#else:
#    print("bunday element yoq")
#print(ism)
#7
#ism = input("Ismingizni kiriting: ")
#tel_nomer = input("Tel nomer: ")
#if len(ism) <= 3:
#    print("Xato: Ism 3 ta belgidan uzun bo'lishi kerak")
#elif len(tel_nomer) != 13:
#    print("Xato: Tel nomer 13 ta belgidan iborat bo'lishi kerak")
#else:
#    print("To'g'ri")
#8
#familiya=input("familiya kiriting:")
#if familiya.endswith('va') or familiya.endswith('v'):
#    print("togri kiritildi")
#else:
#    raise Exception("Notogri kiritildi")
# drasssssssss
#1
#gullar=["lola","atirgul","moychechak","binafsha"]
#gullar.pop()
#print(gullar)
#2
#gullar=["lola","atirgul","moychechak","binafsha"]
#gullar.remove("binafsha")
#print(gullar)
#3
#gullar={"lola","atirgul","moychechak","binafsha"}
#gullar.add("lola1")                         # add degan metod  faqat setda bolganligi uchun gulli qavs bilan yoziladi.bu metod listda bolmaganligi uchun list qilib qoysak xato beradi.
#print(gullar)
# keyingi
#1
#backend_41={"fotima","rano","ozodbek","muhammadrizo","sardorbek"}
#frontend_37={"rano","ozodbek","asadbek"}
#barchasi=backend_41.union(frontend_37)
#print(barchasi)
#ikkalasi_ham=backend_41.intersection(barchasi)
#print(ikkalasi_ham)
#faqat_backend=backend_41.difference(frontend_37)
#print(faqat_backend)
#faqat_frontend=frontend_37.difference(backend_41)
#print(faqat_frontend)
#bittasi=frontend_37.symmetric_difference(backend_41)
#print(bittasi)
#1


                                #12-dars vazifalari while loop
#1
#while True:
#    print("assalomu alaykum")
#2
#son= int(input('son kiritng:'))
#while son>1:
#    son/=3
#if son==1:
#    print("3 ning darajasi:")
#else:
#    print("3ning darajasi emas:")
#3
#while True:
#    son=int(input("son kiriting:"))
#    if son<0:
#      print("manfiy son kiritildi:")
#      break
#4
#son=int(input("son kiriting:"))
#i=1
#while i<=son:
#    if son%i==0:
#        print(i,end=" ")
#    i+=1
#5---------------------------------
#6---------------------------------
#son=int(input("son kiriitng:"))
#yigindi=0
#for raqam in str(son):
#    if raqam.isdigit():
#        yigindi+=int(raqam)
#print(yigindi)
#7
#parol = "12345"
#urinish = 0
#while urinish < 3:
#    if input("Parolni kiriting: ") == parol:
#        print("Xush kelibsiz!")
#        break
#    urinish += 1
#else:
#    print("3 marta noto'g'ri kiritdingiz. Dastur to'xtadi.")
#8
#a,b =0,1
#for i in range(10):
#    print(a, end=" ")
#    a,b=b,a+b
#9 i=0 nimaga shuna qilyapmiz
#son=int(input())
#i=0
#while son:
#    i=i*10+son%10
#    son=son//10
#print(i)
#10
#for i in range(21):
#    print(i)
#11
#while True:
#    x = input("Son kiriting (to'xtatish uchun 'quit' deb yozing): ")  # foydalanuvchidan son yoki 'quit' so'raladi
#    if x == 'quit':
#        break
#    son = int(x)
#    kvadrat = son ** 2
#    print("Kvadrati:", kvadrat)
#12
#while True:
#    matn=input("matn kiriting:")
#    if matn=="stop":
#        print("toxtatildi")
#        break
#    print("kiritildi matn")
#13------------
#son=input("son kiriting:")
#son1=len(son)
#print(son1,"xona")
#14
#while True:
#    son=int(input("son="))
#    if son<0:
#        print("toxtatildi")
#        break
#    print("davom et")
#15
#yigindi=0
#while True:
#    son = int(input("son="))
#    if son==0:
#        break
#    yigindi+= son
#print(" sonlar yigindisi",yigindi)
#16-----------------buni qayerida xato qilgan bolishim mumkin.
#ortacha=0
#while True:
#    son = input("son kiriting:(exit kiritilsa toxtedi)")
#    if son=="exit":
#        print("toxtadi")
#        break
#    ortacha=sum(son)//len(son)
#print(ortacha)
#17
#while True:
#    login=input("login kiriting:")
#    parol=input("parol kiriting:")
#    if login == "admin" and parol == "1234":
#        print("Xush kelibsiz!")
#        break
#    print("xato,qayta urining:")
#18 ----------
#while True:
#    son = int(input("son="))
#    if son==matn:
#        print("faqat son kiritilganda to‘xtaydi")
#        break
#    print("davom et")
#19
#while True:
#    son=int(input("son kiriting:"))
#    if son>10:
#        print("toxtadi")
#        break
#    print("davom et")
#20
#yigindi=0
#while yigindi<100:
#    son=int(input("son kiriitng:"))
#    yigindi+=son
#print("yigindi 100 ga yetdi yoki oshdi",yigindi)
#21--------------1 tan manfiy kiritsAM TOXTAYAPTI
#while True:
#    son = int(input("son kiriitng:"))
#    if son<0:
#        print("toxtadi")
#        break
#    print("davom et")
#22
#while True:
#    son = int(input("son kiriitng:"))
#    if son%5==0:
#        print("sikl toxtadi")
#        break
#    print("davom et")
#23 menda 3ta sondan kop son sorayapti faqat 3 ta kirishi kk ekan
#while True:
#    son = int(input("son kiriitng:(1-50)"))
#    if son%7==0:
#       print("7 ga karrali son")
#        break
#    print("toxtadi")
#24
# shaygacha chiqmaganlari:5,6,13,16,18,21,24
    # SET VA DICTIONARY 41-guruhdgi vazifa
#1
#ism1={"azim","jahongir","xoji","abu"}
#ism2={"xoji","ali","akbar","bahrom"}
#kesishma=ism1.intersection(ism2)
#print(kesishma)
#2
# ism1={"azim","jahongir","xoji","abu"}
# ism2={"xoji","ali","akbar","bahrom"}
# farq=ism1.difference(ism2)
# print(farq)
#3
#sonlar={1,2,3,4,5,6,7,8,9}
#kattasi=max(sonlar)
#print(kattasi)
#4
#malumot={"jersey":10,"club":"paxtakor","age":28}
#malumot.update({"club":"Neftchi"})
#print("yangi",malumot)
#5
#malumot={"jersey":10,"club":"paxtakor","age":28}
#print(malumot.items())
#6
#sonlar={1,2,3,4,5,3,4,8,9}
#print(len(sonlar))
#7
#ism=input("ismingizni kiriting:")
#yosh=int(input("yoshingizni kiriitng:"))
#fan=input("fanni kiriting:")
#ustoz={"ism":ism,"yosh":yosh,"fan":fan}
#print(ustoz.values())
#8
#ustoz={"ism":"fotima","yosh":19,"fan":"dasturlash"}
#ustoz.update({"fan":"python"})
#print("yangi",ustoz)
#9
#ustoz={"ism":"fotima","yosh":19,"fan":"dasturlash"}
#print(ustoz.values())
#10----------------ikkilanish boldi
#shaharlar = {"Toshkent", "Namangan", "Andijon", "Buxoro", "Xiva"}
#shahar = input("Shahar nomini kiriting: ")
#if shahar in shaharlar:
#    shaharlar.remove(shahar)
#    print(f"{shahar} o‘chirildi.")
#else:
#    print("Bunday shahar topilmadi.")
#print("Qolgan shaharlar:", shaharlar)
#    # 13 dars oyin yaratish
# template=""" --- --- ---
# | 1 | 2 | 3 |
#  --- --- ---
# | 4 | 5 | 6 |
#  --- --- ---
# | 7 | 8 | 9 |
#  --- --- ---
# """
# victories=['123','456','789','147','258','369','159','357']
# x_input=''
# o_input=''
# victory = False
# for qadam in range(1,10):
#     if victory:
#         break
#     elif qadam%2==1:
#         x_input=input(template+"(X) oyinchi maydon kiritsin:(1-9)")
#         while x_input not in ['1','2','3','4','5','6','7','8','9'] or x_input in x_input + o_input:
#             print("xato kiritish")
#             if x_input in x_input + o_input:
#                 print("maydon allaqachon band!")
#             x_input=input("(X) oyinchi qayta kiritsin:(1-9):")
#         x_input +=x_input
#         template = template.replace("X",x_input)
#         for v in victories:
#             if v[0] in x_input and v[1] in x_input and v[2] in x_input:
#                 print("-----------------\n" + template + "(X) oyinchi galaba qozondi")
#                 victory = True
#                 break
#     else:
#         o_input=input(template + "(0) oyinchi maydon kiritsin:(1-9):")
#         while o_input not in ['1','2','3','4','5','6','7','8','9'] or o_input in x_input + o_input:
#             print("xato kiritish")
#             if o_input in x_input + o_input:
#                 print("maydon allaqachon band!")
#             o_input=input("(0) oyinchi qayta kiritsin:(1-9):")
#         o_input +=o_input
#         template = template.replace(o_input,"0")
#         for v in victories:
#             if v[0] in o_input and v[1] in o_input and v[2] in o_input:
#                 print("------------------------\n " + template + "(0) oyinchi galaba qozondi")
#                 victory = True
#                 break
# else:
#     print("-------------------------\n" + template + "durrang natija qayt etildi")

                                 #imtihon
#1
# son="5679824"
# print(son[5])
# #2
# sonlar=(1,2,3,4,5,6,7,8,2,2,2,2)
# n=2
# print(sonlar.count(n))
# #3
# a=int(input("1 son kiriting:"))
# b=int(input("2 son kiriting:"))
# c=int(input("3 son kiriting:"))
# if a%2==0:
#     print("juft son")
# else:
#     print("toq son")
# if b%2==0:
#     print("juft son")
# else:
#     print("toq son")
# if c%2==0:
#     print("juft son")
# else:
#     print("toq son")
#4
# matn=input("matn kiriting:")
# print(matn.replace(".",","))
# #5
# a=int(input("2 xonali son kiriting:"))
# onlar=a//10
# birlar=a%10
# onlar,birlar=birlar,onlar
# print(onlar,birlar)
#6
# ismlar=["fotima","asilbek","maftuna","rano"]
# ismlar.sort()
# print(ismlar)
#7
# a=int(input("3 xonali son kiriting:"))
# yuzlar=a//100
# onlar=a//10%10
# birlar=a%10
# yuzlar,onlar,birlar=birlar,onlar,yuzlar
# print(yuzlar,onlar,birlar)
#11
# ismlar=["fotima","aslbek","maftuna"]
# ism="lola"
# if ism in ismlar:
#      print("allaqachon bor")
# else:
#      ismlar.append(ism)
#      print(ismlar)
#12
# sonlar=[12,23,45,67]
# katta=max(sonlar)
# kichik=min(sonlar)
# orta=(max(sonlar)-min(sonlar))-sum(sonlar)/len(sonlar)
# print(orta)
#13
# sonlar=1,2,3,4,5,6,7,8
# ayirma=max(sonlar)-min(sonlar)
# print(ayirma)
#14 sort qayga qoyiladi
# dict={"yosh":19,"kun":10,"oy":12}
# print(dict.values())
#15
# gap=input("gap kiriting:").title()
# print(gap)
#18 sort qayga yoziladi
# text={"uzbekiston":"toshkent","xitoy":"pekin","turkiya":"anqara"}
# print(text.keys())
# print(text.values())
#19
# son=int(input("son kiriting:"))
# if son%2==0 and son>0:
#     print("juft son","musbat son")
# else:
#     print("toq son","manfiy son")
#21 alohida listga joylolmadim
# son=[12,34,23]
# if son%2==0:
#     print("juft son")
# else:
#     print("toq son")
          # chiqmaganlari 8 9 10 14 16 17 18 20 21 22
# 8---
# d={"ism":"islom","talaba":True,"kurs":2}
# key=input("key kiriitng:")
# value=input("value kiriitng:")
# d[key]=value  # mavjud bolsa ozgartiradi,yoq bolsa qoshadi, lekin ozgarmadi
# print(d)
#9
# son=int(input("son kiriting:"))
# print("xona:",len(str(son)),"xona")
#10---
#14
# d={"yosh":19,"kun":10,"oy":12}
# print(sorted(d.values()))
#16
# a={1,23,4,2,6,8}
# b={2,5,7,3,6,1}
# natija=a.symmetric_difference(b)
# print(natija)
#17
# sonlar=[1,2,3,4,5,6]
# tasodifiy=sonlar.pop()
# print(tasodifiy)
# print(sonlar)
#18
# text={"uzbekiston":"toshkent","xitoy":"pekin","turkiya":"anqara"}
# print(sorted(text.keys()))
# print(sorted(text.values()))
            # 39 guruhdagi imtihon Bismillah
#1
# ism=input("ismingizni kiriitng:")
# yosh=int(input("yoshingizni kiriitng:"))
# print("Mening ismim",ism,"yoshim",yosh,"da" )
#2
# a=23
# b=5
# qoldiq=a%b
# print(qoldiq)
#3
# son=int(input("son kiriting:"))
# kvadrat=son**2
# print(kvadrat)
#4
# ism=input("ismingizni kiriitng:")
# familya=input("familiya:")
# print(ism.title(),familya.title())
#5
# yil=int(input("yilingizni kiriting:"))
# yosh=2025-yil
# print(yosh)
#7
# a=1
# b=2
# a,b=b,a
# print(a,b)
#8---
# def son():
#     if son%2==0:
#         print("juft son")
#     else:
#         print("toq son")
#         print(son)
# son()
#9
# a=int(input('1 son kiriting:'))
# b=int(input('2 son kiriting:'))
# c=int(input('3 son kiriting:'))
# if a>0:
#     print("musbat son")
# else:
#     print("manfiy son")
# if b>0:
#     print("musbat son")
# else:
#     print("manfiy son")
# if c>0:
#     print("musbat son")
# else:
#     print("manfiy son")
#10
# for son in range(101):
#     if son%5==0:
#         print(remove(son))
# print(son)
#11
# import random
# print(random.randint(1-101))
#12
# soz="python"
# for harf in soz:
#     print(soz[::-1])
#13
# a=int(input('a sonni kiriitng:'))
# n=int(input('n sonni kiriitng:'))
# for a in range(a,n):
#     print(a+n)
#14
# d={"yosh":19,"kun":10,"oy":12}
# print(sorted(d.values()))
#15
#sonlar chiqadi
#16
# meva1={"olma","anor","o'rik"}
# meva2={"behi","olma","nok"}
# print(meva1.intersection(meva2))
#17
# ismlar=["fotima","rano","guli"]
# ism=input("ism kiriting:")
# if ism in ismlar:
#     print("siz ro'yxatda borsiz")
# else:
#     print(ismlar.extend(ism))
# print(ismlar)
#18
# ism1=input("ism1 kiriting:")
# ism2=input("ism2 kiriting:")
# ism3=input("ism3 kiriting:")
# print(sorted([ism1,ism2,ism3]))
#19
#5 ta yoki 6ta 1 chiqadi.
#20
# son=int(input("2 xonali son kiriting:"))
# onlar=son//10
# birlar=son%10
# onlar,birlar=birlar,onlar
# print(onlar,birlar)
#21---
# sonlar=[1,2,3,4,5]
# if sonlar%2==0:
#     print("juft son")
# else:
#     print("toq son")
# print("toq",sonlar,"juft",sonlar)
#22
# son=int(input("son kiriitng:"))
# if son%2==0:
#     print("juft son")
# else:
#     juft=son+1
#     print(juft)
# class Talaba:
#     def __init__(self,ism,yosh,kurs):
#         self.ism = ism
#         self.yosh = yosh
#         self.kurs = kurs
#     def tanishtir(self):
#         return f"Ism:{self.ism} Yosh:{self.yosh} Kurs:{self.kurs}"
#     def yoshni_oshir(self):
#         self.yosh +=1
#
# fotima=Talaba("fotima",19,2)
# class Calculator:
#     def __init__(self):
#         self.natija=0
#     def qoshish(self,son):
#         self.natija +=son
#         return self.natija
#     def ayirish(self,son):
#         self.natija -= son
#         return self.natija
#     def kopaytirish(self,son):
#         self.natija*=son
#         return self.natija
#     def bolish(self,son):
#         if son==0:
#             return "cannot divide by zero"
#         self.natija /=son
#         return self.natija
#     def tozalash(self):
#         self.natija=0
#         return self.natija
# k=Calculator()
# print(k.qoshish(51))
# print(k.ayirish(9))
# print(k.kopaytirish(6))
# print(k.bolish(45))
#
# import datetime
# print(str(datetime.datetime.now().strftime("%d.%m.%Y (%H:%M")))
#
# class BankAccount:
#     def __init__(self,ega,karta_raqam,parol,balans=0):
#         self.ega=ega
#         self.karta_raqam=karta_raqam
#         self.parol=parol
#         self.balans=balans
#         self.kirimlar_tarixi=[]
#         self.chiqimlar_tarixi=[]
#
#
#     def malumot(self):
#         return f"{self.ega} | {self.karta_raqam}"
#     def get_balans(self):
#         return  f"Hisob: ${self.balans}"
#     def get_parol(self):
#         return f"Parol: ${self.parol}"
#     def get_kirimlar(self):
#         t="kirimlar tarixi:\n"
#         for i, kirim in enumerate(self.kirimlar_tarixi,start=1):
#             t += f"{i}. {kirim["miqdor"]:4}$ | {kirim.get("vaqt")} | {kirim.get("izoh"):30}\n"
#             return t
#     def get_chiqimlar(self):
#         t="chiqimlar tarixi:\n"
#         for i, chiqimlar in enumerate(self.chiqimlar_tarixi,start=1):
#             t +=f"{i}.{chiqim.get("miqdor"):4}$ | {chiqim.get("get")} | {chiqim.get("izoh"):30}\n"
#             return t
#     def kirim(self,miqdor,izoh=""):
#         self.balans +=miqdor
#         self.kirimlar_tarixi.append({"miqdor":miqdor,"izoh":izoh,"vaqt":str(datetime.datetime.now().strftime("%d.%m.%y(%H:%m)"))})
#     def chiqim(self,miqdor,izoh=""):
#         assert miqdor <=self.balans, "Mablag' yetarli emas!"
#         self.balans -= miqdor
#         self.chiqimlar_tarixi.append({"miqdor":miqdor,"izoh":izoh,"vaqt": str(datetime.datetime.now().strftime("%d.%m.%Y(%H:%M)"))})
# fotima=BankAccount("jaloldinova.txt fotima","9860 0803 7943 4931","7777",200)
# print(fotima.malumot())
# fotima.kirim(800,"oktabr uchun avans")
# fotima.kirim(200,"loyiha uchun daromad")
# fotima.kirim(1400,"oktabr uchun maosh")
# print(fotima.get_balans())
# fotima.chiqm(1500,"noutbuk")
# fotima.chiqim(200,"kitob")
# print(fotima.get_balans())
# print(fotima.get_chiqimlar())
# print(fotima.get_kirimlar())
#
# data={"ism":"fotima",
#       "yosh":18}
# print(data.get("ism"))
#

                       # shart operatorlari 14 ta masala
  #1
# x=12
# y=19
# print(max(x,y))
# print(min(x,y))
  #2
# x=12
# y=34
# z=98
# print(max(x,y,z))
# print(min(x,y,z))
  #3
# x=12
# y=34
# z=98
# print(max(x+y+z,x*y*z))
# print(min(x+y+z/2,x*y*z)+1)
  #4
# a=89
# b=48
# c=45
# if a>=b>=c:
#     print("qanoatlantiradi")
# else:
#     print("qanoatlantirmedi")
  #5
# a=float(input("a sonni kiriting: "))
# b=float(input("b sonni kiriting: "))
# c=float(input("c sonni kiriting: "))
# if a>=b>=c:
#     print(2*a,2*b,2*c)
# else:
#     print(a,b,c)
   #7
# a=float(input("a sonni kiriting:"))
# b=float(input("b sonni kiriting:"))
# if a>b:
#     print(a)
# else:
#     print(a,b)
  #8--
# a=float(input("a sonni kiriting:"))
# b=float(input("b sonni kiriting:"))
# if a<=b:
#     a=0
#     print(a)
# else:
#     print(a,b)
  #9
# a=5
# b=1
# c=2
# if 1<=a<=3:
#     print("a soni 1:3 oraligida yotadi")
# if 1<=b<=3:
#     print("b soni 1:3 oraligida yotadi")
# if 1<=c<=3:
#     print("c soni 1:3 oraligida yotadi")
  #10
# x=float(input("x sonni kirit:"))
# y=float(input("y sonni kirit:"))
# if x>y:
#     print((x+y)/2)
# else:
#     print(2*x*y)
  #11
# a=float(input("a sonni kiriting: "))
# b=float(input("b sonni kiriting: "))
# c=float(input("c sonni kiriting: "))
# if a>0:
#     print(a**2)
# else:
#     print(a)
# if b>0:
#     print(b**2)
# else:
#     print(b)
# if c>0:
#     print(c**2)
# else:
#     print(c)
  #12
# a=float(input("a sonni kiriting: "))
# b=float(input("b sonni kiriting: "))
# c=float(input("c sonni kiriting: "))
# d=float(input("d sonni kiriting: "))
# if d>=c>=b>=a:
#     print(d)
# elif a>b>c>d:
#     print(a,b,c,d)
# else:
#     print(a**2,b**2,c**2
                                       #13-dars
#                 #1
# class Mehmon:
#     def __init__(self,ism,yosh,email):
#         self.ism = ism
#         self.yosh = yosh
#         self.email = email
# mehmon=Mehmon("Fotima","19","jaloldinovafotima@gmail.com")
# print(f"Ismim {mehmon.ism}, yoshim {mehmon.yosh} da,elektron pochtam {mehmon.email}")
#                   #2
# class Student:
#     def __init__(self,ism,baho1,baho2,baho3):
#         self.ism=ism
#         self.baho1=int(baho1)
#         self.baho2=int(baho2)
#         self.baho3=int(baho3)
#     def average_grade(self):
#         return (self.baho1 + self.baho2 + self.baho3) / 3
# student=Student("Fotima","5","3","7")
# print(f"{student.ism} ning ortacha qiymati: {student.average_grade()}")
#                      #3
# class Student():
#     def __init__(self,ism,baho1,baho2,baho3):
#         self.ism=ism
#         self.baho1=int(baho1)
#         self.baho2=int(baho2)
#         self.baho3=int(baho3)
#     def average_grade(self):
#         return (self.baho1 + self.baho2 + self.baho3) / 3
# student=Student("fotima","9","4","6")
# print(f"{student.ism} ning ortacha qiymati: {student.average_grade()}")
#                  #4
# class Meva():
#     def __init__(self,rang,narx,kech_pishishi):
#         self.rang = rang
#         self.narx = narx
#         self.kech_pishishi=kech_pishishi
# meva=Meva("qizil","25000","kecha pishadi")
# print(f"Olma {meva.rang} rangda,narxi {meva.narx} ming,{meva.kech_pishishi}")
#                  #5
# class Math():
#     def __init__(self, a, b):
#         self.natija=0
#     def qoshish(self,son):
#         self.natija +=son
#         return self.natija
#     def ayirish(self,son):
#         self.natija -= son
#         return self.natija
#     def kopaytirish(self,son):
#         self.natija *=son
#         return self.natija
# m=Math(0,0)
# print(m.qoshish(100))
# print(m.ayirish(10))
# print(m.kopaytirish(15))
#                     #6 qoldiqli_bolishini qilolmadim---
# class Math():
#      def __init__(self, a, b):
#          self.a = a
#          self.b = b
#      def qoldiq(self):
#          return self.a%self.b
#      def daraja(self):
#          return self.a ** self.b
# m=Math(3, 2)
# print(m.qoldiq())
# print(m.daraja())
                             #tanlash operatori
# 1
# son=int(input("son kiriitng:(1-12)"))
# match son:
#     case 1:
#         print("yanvar")
#     case 2:
#         print("fevral")
#     case 3:
#         print("mart")
#     case 4:
#         print("aprel")
#     case 5:
#         print("may")
#     case 6:
#         print("iyun")
#     case 7:
#         print("iyul")
#     case 8:
#         print("avgust")
#     case 9:
#         print("sentabr")
#     case 10:
#         print("oktabr")
#     case 11:
#         print("noyabr")
#     case 12:
#         print("dekabr")
# #2
# oy_raqam=int(input("oy raqam:(1-12)"))
# match oy_raqam:
#     case 1|2|12:
#         print("qish")
#     case 3|4|5:
#         print("bahor")
#     case 6|7|8:
#         print("yoz")
#     case 9|10|11:
#         print("kuz")
# #3
# fasl_raqam=int(input("fasl_raqam:(1-4)"))
# match fasl_raqam:
#     case 1:
#         print("yanvar,fevral,dekabr")
#     case 2:
#         print("mart,aprel,may")
#     case 3:
#         print("iyun,iyul,avgust")
#     case 4:
#         print("sentabr,oktabr,noyabr")
# 4
# n = int(input("n son kiriting:(0-100)"))
# onlar = n // 10
# birlar = n % 10
# onlar_soz = ""
# birlar_soz = ""
# match onlar:
#     case 1:
#         onlar_soz = "on"
#     case 2:
#         onlar_soz = "yigirma"
#     case 3:
#         onlar_soz = "o'ttiz"
#     case 4:
#         onlar_soz = "qirq"
#     case 5:
#         onlar_soz = "ellik"
#     case 6:
#         onlar_soz = "oltmish"
#     case 7:
#         onlar_soz = "yetmish"
#     case 8:
#         onlar_soz = "sakson"
#     case 9:
#         onlar_soz = "to'qson"
# match birlar:
#     case 1:
#         birlar_soz = "bir"
#     case 2:
#         birlar_soz = "ikki"
#     case 3:
#         birlar_soz = "uch"
#     case 4:
#         birlar_soz = "to'rt"
#     case 5:
#         birlar_soz = "besh"
#     case 6:
#         birlar_soz = "olti"
#     case 7:
#         birlar_soz = "yetti"
#     case 8:
#         birlar_soz = "sakkiz"
#     case 9:
#         birlar_soz = "to'qqiz"
# if n == 0:
#     print("nol")
# elif n == 100:
#     print("yuz")
# elif n < 10:
#     print(birlar_soz)
# elif birlar == 0:
#     print(onlar_soz)
# else:
#     print(onlar_soz, birlar_soz)
                    # for sikliga oid masalalar
#1
# for i in range(1,11):
#     print(i) #bir qatorda chiqarmoqchi bolsak end"" qilamiz bu hozirgi vertikal holati
# #2
# for i in range(1,101):
#     if i % 2 == 0:
#       print(i)
# #3
# for i in range(1,101):
#     if i % 2 == 1:
#         print(i)
# #4
# n= int(input("n sonni kiriting:"))
# yigindi =0
# for i in range(1,n+1):
#     yigindi+=i
# print(yigindi)
# #5
# n=int(input("n sonni kiriting:"))
# for i in range(1,n+1):
#     print(i**2)
# #6
# n=int(input("n sonni kiriting:"))
# for i in range(n,0,-1):
#     print(i)
#7
# n=int(input("n sonni kiriting:"))
# kopaytma=1
# for i in range(1,n+1):
#     kopaytma*=i
#     print(kopaytma)
#8--- sorash

                  # funksiyalar darturchi uchun funksiyada print bn input ishlatish togri emas
#1
# def salomlashsish():
#     ism=input("ismingizni kiriitng:")
#     print("Assalomu alaykum",ism)
#     print("Xush kelibsiz")
# salomlashsish()
#2
# def yilni_top(yosh):
#     t_yil=2025-yosh
#     return t_yil
# print(yilni_top(19))
# #3
# def eng_kattasi(a,b):
#     if a>=b:
#         return a
#     else:
#         return b
# print(eng_kattasi(10,7))
#4
# def eng_kattasi(*args):
#     args = list(args)
#     args.sort()
#     return args[-1]
# def eng_kichigi(*args):
#     args = list(args)
#     args.sort()
#     return args[0]
# print(eng_kattasi(12,34,6,7,9,3))
# print(eng_kichigi(12,34,6,7,9,3))
# ortacha=lambda a,b,c:(a+b+c)/3
# print(ortacha(23,78,90))
#5
# class Kitob:
#     def __init__(self,nomi,muallifi,sahifa_nomi):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.sahifa_nomi = sahifa_nomi
#     def kitobni_oqi(self):
#         print(f"Kitob nomi {self.nomi} muallifi {self.muallifi} sahifa raqami {self.sahifa_nomi} shu sahifadagi kitobni oqing")
# qalb_iffati=Kitob("qalb_iffati","jaloldinova.txt fotima","43")
# qalb_iffati.kitobni_oqi()
#6
# class Talaba:
#     def __init__(self,ism,kurs,yonalish):
#         self.ism = ism
#         self.kurs = kurs
#         self.yonalish = yonalish
#
#     def talaba(self):
#         print(f"Talaba {self.ism} {self.kurs} kurs yonalishi {self.yonalish}")
# talaba=Talaba("jaloldinova.txt fotima","2","Axborot xavfsizligi")
# talaba.talaba()
#7
# class Kompyuter:
#     def __init__(self,model,narx):
#         self.model = model
#         self.narx = narx
#     def kompyuter(self):
#         print(f"komyuter modele {self.model} narxi {self.narx} $")
# kompyuter= Kompyuter(model="Lenovo",narx="370")
# kompyuter.kompyuter()
#8
# class Hayvon:
#     def __init__(self,turi,ovqat):
#         self.turi = turi
#         self.ovqat = ovqat
#     def hayvon(self):
#         print(f"hayvon turi {self.turi},ovqati nomi {self.ovqat}")
# mushuk=Hayvon("mushuk","kasha")
# mushuk.hayvon()
#9
# class Telefon:
#     def __init__(self,model,narx,batareya):
#         self.model = model
#         self.narx = narx
#         self.batareya = batareya
#     def telefon(self):
#         print(f"Telefon nomi {self.model} narxi {self.narx}$ batareya {self.batareya}%")
# telefon=Telefon("redmi","200","56")
# telefon.telefon()
#10
# class Mashina:
#     def __init__(self,model,tezlik,rang):
#         self.model = model
#         self.tezlik = tezlik
#         self.rang = rang
#     def mashina(self):
#         print(f"Eng zor mashina {self.model} eng yuqori tezligi {self.tezlik} km/s rangi {self.rang}")
# mashina=Mashina("gentra","120","qora")
# mashina.mashina()
#11
# class Oshpaz:
#     def __init__(self,ism,tajriba,taom):
#         self.ism=ism
#         self.tajriba=tajriba
#         self.taom=taom
#     def oshpaz(self):
#         print(f"Eng zor oshpaz {self.ism} tajriba {self.tajriba} yil  eng zor taom {self.taom}")
# oshpaz=Oshpaz("fotima","2","osh")
# oshpaz.oshpaz()
#12
# class Dokon:
#     def __init__(self,nomi,joylashuvi,tovar_soni):
#         self.nomi = nomi
#         self.joylashuvi = joylashuvi
#         self.tovar_soni = tovar_soni
#     def dokon(self):
#         print(f"dokon nomi {self.nomi} joylashuvi {self.joylashuvi}da tovarlar soni {self.tovar_soni} ta")
# dokon=Dokon("family","sent","123")
# dokon.dokon()
#13
# class Ovqat:
#     def __init__(self,nomi,turi):
#         self.nomi = nomi
#         self.turi = turi
#     def ovqat(self):
#         print(f"ovqat nomi {self.nomi}  {self.turi}")
# ovqat=Ovqat("osh","osh")
# ovqat.ovqat()
                                          # dars 14
# class Product:
#     def __init__(self, name, price, quantity,unit):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.unit = unit
# class Market:
#     def __init__(self,name,address):
#         self.name = name
#         self.address = address
#         self.products = []
#         self.sales = "sotuvlar tarixi:\n"
#         self.balance = 0
#     def about(self):
#         return f"{self.name}: {self.address}"
#     def add_product(self,name,price,quantity,unit):
#         new_product = Product(name,price,quantity,unit)
#         self.products.append(new_product)
#     def get_balance(self):
#         return f"Balance: {self.balance} so'm "
#     def get_sales(self):
#         return self.sales[:-1]
#     def get_products(self):
#         t="stare:\n"
#         for product in self.products:
#             t += f"{product.name}: {product.price} so'm -{product.quantity} {product.unit} mavjud!\n "
#             return t[:-1]
#     def sale_product(self,name,quantity,price):
#         sale_product = None
#         for product in self.products:
#             if product.name == name:
#                 sale_product = product
#                 break
#         if sale_product is None:
#             return f"No product named {name}"
#         else:
#             if sale_product.quantity < quantity:
#                 return f"Not enougt product {sale_product.name}.{sale_product.quantity} mavjud!"
#             else:
#                 sale_product.quantity -= quantity
#                 self.balance += quantity * price
#                 self.sales+=f"{sale_product.name}{quantity} {sale_product.unit} sotildi!\n"
#                 return f"{sale_product.name}{quantity} {sale_product.unit} sotildi!"
# baraka=Market("baraka","namangan")
# baraka.add_product("olma",10000,100,"kg")
# baraka.add_product("non",23000,130,"dona")
# baraka.add_product("fanta 1.l", 12000,30,"dona")
# baraka.sale_product("non",20,4000)
# baraka.sale_product("olma",40,12000)
# print(baraka.get_products())
# print(baraka.get_sales())
# print(baraka.get_balance())
               #41 dars vazifalari
# 1
# def salomlashish():
#     print("salom,bolajonlar")
# salomlashish()
# 2
# def uzunligi():
#     ismlar=input("ismlarni kiriitng:").split()
#     uzunligi=max(ismlar,key=len)
#     print(uzunligi)
# uzunligi()
# 3
# def ortacha():
#     baholar=[2,4,6,8,5]
#     ortacha=sum(baholar)/len(baholar)
#     print(ortacha)
# ortacha()
# 4
# def uzunligi():
#      ismlar=input("ismlarni kiriitng:").split()
#      uzunligi=min(ismlar,key=len)
#      print(uzunligi)
# uzunligi()
# 5
# def teskari_tartib():
#     ismlar=input("ismlarini kiriting:")
#     print(ismlar[::-1])
# teskari_tartib()
# 6 rekursiv funksiya
# 7
# def eng_katta():
#     sonlar=[12,45,34,78,65,90]
#     print(max(sonlar))
# eng_katta()
# 8
# def kub():
#     son=int(input("son kiriting:"))
#     print(son**3)
# kub()
# 9
# def juft_toq():
#     son=int(input("son kiriting:"))
#     if son%2==0:
#         print("juft son")
#     else:
#         print("toq son")
# juft_toq()
#10
# def kata_harflar():
#     ismlar=input("ismlarni kiriitng:").upper()
#     print(ismlar)
# kata_harflar()
                    #39 guruhdagi vazifalar
#1
# class List():
#     def __init__(self,append,pop,remove,extend,insert):
#         self.append = append
#         self.pop = pop
#         self.remove = remove
#         self.extend = extend
#         self.insert = insert
#     def list(self):
#         print(f"qoshish vazifani-{self.append},o'chirish vazifasini-{self.pop},qiymatni o'chirish-{self.remove},list qoshish-{self.extend},istagan joyiga qo'shish-{self.insert}")
# list=List("append","pop","remove","extend","insert")
# list.list()
# #2
# class String():
#     def __init__(self,split,strip,count,index,find,replace):
#         self.split = split
#         self.strip = strip
#         self.count = count
#         self.index = index
#         self.find = find
#         self.replace = replace
#     def string(self):
#         print(f"bosh joyni olish-{self.strip},nechta qatnashganini topadi-{self.count},index topadi-{self.index},find topadi-{self.find},alishtiradi-{self.replace},qismlarga ajratish-{self.split}")
# string=String("split","strip","count","index","find","replace")
# string.string()
# #3
# class Set():
#     def __init__(self,add,remove,pop,intersection):
#         self.add = add
#         self.remove = remove
#         self.pop = pop
#         self.intersection = intersection
#     def set(self):
#         print(f"qiymat qoshish-{self.add},aytilganini o'chirish-{self.remove},ochirish-{self.pop},kesishma-{self.intersection}")
# set=Set("add","remove","pop","intersection")
# set.set()
# #4-- davom ettirib ketolmadim
# class Termin():
#     def __init__(self):
#         self.termin={}

#            41-guruhdagi dars rekursiv funksiya
                                   #1
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(27))
                                    #2
# def summa(sonlar):
#     if len(sonlar)==0:
#         return 0
#     else:
#         return sonlar.pop() +summa(sonlar)
# print(summa([1,23,56,7,8,6,3,4,6,6,4,3,2,2]))
                 #41-guruhdagi vazifalar
#1
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# #2
# def fibonachi(n):
#     if n<=1:
#         return n
#     else:
#         return fibonachi(n-1)+fibonachi(n-2)
# 3
# def yigindi(n):
#     if n==0:
#         return 0
#     else:
#         return n%10+yigindi(n//10)
# print(yigindi(100))
# #4
# def kopaytma(n):
#     if n<10:
#         return 0
#     else:
#         return n%10*kopaytma(n//10)
# print(kopaytma(9))
# #5
# def teskari(n,tes=0):
#     if n==0:
#         return tes
#     else:
#         return teskari(n//10,tes*10+n%10)
# print(teskari(1,2))
#1
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(7))
# #2
# def fibonachi(n):
#     if n<=1:
#         return n
#     else:
#         return fibonachi(n-1)+fibonachi(n-2)
# print(fibonachi(17))
#1
# for i in range(5):
#     print("fotima")
# #2
# gullar=['lola','atirgul','qilgoldoq']
# for gul in gullar:
#     print(gul)
#3
# s=0
# for i in range(1,19):
#     s+=i
# print(s)
# #4
# son=int(input("son kiritng:"))
# fac=1
# for i in range(1,son+1):
#     fac*=i
# print(fac)
#5
# parol="7777"
# for i in range(7):
#     parol1=input("parolingizni kiriting:")
#     if parol1==parol:
#         print("xush kelibsiz!")
#         break
#     else:
#         print("xato kitirdingiz!")
# else:
#     print("urinishlar tugadi!")
# parol="123456"
# for i in range(8):
#     parol1=input("parolingizni kiriting:")
#     if parol==parol1:
#         print("xush kelibsiz!")
#         break
#     else:
#         print("xato kiritish!")
# else:
#     print("urinishlar tugadi!")
#                          #41-guruhdagi vazifalar
# 1
# for i in range(1,11):
#     print(i)
# #2 ustoz shayda 0 ham chiqib qolyaptiyu 0 juft son emasku yo xatolikka kirmedimi
# for i in range(0,21,2):
#     print(i)
# #3
# s=0
# for i in range(1,101):
#     s+=i
# print(s)
# #4
# for i in range(5):
#     print("salom")
# #5
# for harf in "python" :
#     print(harf)
# #6 qaysi royxatni aytganini anglamadim
# #7
# for i in range(1,11):
#     print(i**2)
# #8
# for i in range(0,51,3):
#     print(i)
# 9
# sonlar=[1,12,5,4,8,3]
# kopaytma=1
# for i in sonlar:
#     kopaytma*=i
# print("kopaytma",kopaytma)
#
# #10 nechtaligi qande qiladi:
# for i in range(-12,89):
#     if i>0:
#         print("musbat son")
#     elif i==0:
#         print("nomusbat son")
#     else:
#         print("manfiy son")
# 11
# son=0
# for i in range(5):
#     son1=int(input("son kiriitng:"))
#     son+=son1
# print("yigindi",son)
# 12
# for i in range(10,0,-1):
#     print(i)
# 13------
# 14
# soz='Gullar'
# uzunlik = len(soz)
# for i in range(uzunlik - 1, -1, -1):
#     print(soz[i], end="")
# 15
# for i in range(2,10):
#     for j in range(2,6):
#         print(f"{j}*{i} = {i*j:2} ", end="   " )
#     print()
# print()
# for i in range(2,10):
#     for j in range(6,10):
#         print(f"{j}*{i} = {i*j:2} ", end="   ")
#     print()
# 16
# sonlar=[1,2,3,4,5,6,787,98]
# for i in sonlar:
#     print(max(sonlar))
#     break
# print(min(sonlar))
# 17
# a=12
# b=23
# for i in range(a,b+1):
#     print(i)
# 18 har safar nimani qoshayatgandagi sonlarni  yigindisini ham korsatib ketyapti.menga natija kk holos.
# a=12
# b=23
# yigindi=0
# for i in range(a,b+1):
#     yigindi+=i
#     print(yigindi)
# 19
# soz="Romashka"
# for harf in 'Romashka':
#     print(harf)
# 20
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, '=', 'FizzBuzz')
#     elif i % 3 == 0:
#         print(i, '=', 'Fizz')
#     elif i % 5 == 0:
#         print(i, '=', 'Buzz')
# 21
# n=int(input("son kiriitng:"))
# fac=1
# for i in range(1,n+1):
#     fac*=i
# print(n,"!=",fac)
# 22
# list=[1,2,3,4,5]
# for item in reversed(list):
#     print(item)
# 23-----
# 24
# matn=["fotima","asilbek","maftuna"]
# for i in range(len(matn)):
#     print(len(matn[i]))
# 25
# for i in range(1,6):
#     print("*"*i)
# 26---
# 27
# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# 28--
# matn=["fotima","asilbek","lola"]
# for i in range(0,len(matn)):
#     print(max(matn))
#     print(min(matn))
#     break
# 29
# k=1
# n=23
# for i in range(n):
#     print(k)
# 31
# for i in range(-10,0):
#     print(i)
#39guruhdagi
#1
# class Matn:
#     def __unit__(self,matn):
#         self.matn=matn
#     def katta_harf(self):
#         return self.matn.upper()
#     def kichik_harf(self):
#         return self.matn.lower()
#     def sonmi(self):
#         return self.matn.isnumeric()
#     def boshi_katta(self):
#         return self.matn.capitalize()
#     def bosh_joyli_olish(self):
#         return self.matn.strip()
#2
# class Matn:
#     def __unit__(self,matn):
#         self.matn=matn
#         if self.matn.isnumeric():
#             print("sondan iborat")
#         else:
#             self.matn=self.matn.upper()
#             print("katta harflarga ozgartirildi",self.matn)
#5
# class TupleList:
#     def __init__(self, *args):
#         self.data = list(args)  # ichki saqlovchi list
#     def append(self, item):
#         self.data.append(item)
#     def pop(self, index=-1):
#         return self.data.pop(index)
#     def insert(self, index, item):
#         self.data.insert(index, item)
#     def remove(self, item):
#         self.data.remove(item)
#     def __repr__(self):
#         return str(tuple(self.data))
#6
# class Lugat:
#     def __init__(self, ):
#         self.sozlar ={}
#     def qoshish(self,soz,tarjima):
#             self.sozlar[soz]=tarjima
#     def ozgartirish(self,soz,yangi_tarjima):
#             if soz in self.sozlar:
#                 self.sozlar[soz]=yangi_tarjima
#             else:
#                 print("bunday so'z yoq")
#     def tarjima_ber(self,soz):
#         return self.sozlar.get(soz,"so'z topilmadi")
#     def ochirish(self,soz):
#         if soz in self.sozlar:
#             del self.sozlar[soz]
#         else:
#             print("bunday so'z yoq")
#                chiqmaganlari 3-4,7
# nubers = list(map(int,input("sonlarni probel bilan kiriting: ").split()))
# stack=[]
# for num in nubers:
#     stack.append(num)
# print("teskari tartibda:")
# while stack:
#     print(stack.pop(), end=' ')
        #39
# class BankKarta:
#     def __init__(self, karta_raqam,balans=0):
#         self.karta_raqam=karta_raqam
#         self.__balans=balans
#     #getter
#     def get_balans(self):
#         return self.__balans
#     #setter
#     def set_balans(self, miqdor):
#         self.__balans=miqdor
#     def malumot(self):
#         return self.karta_raqam
# bank_karta1=BankKarta("9860 0809 2345 6543",23456)
# print(bank_karta1.set_balans())
# print(bank_karta1.get_balans())
#2
# class Transport:
#     def __init__(self,model,brend):
#         self.model = model
#         self.brend = brend
#     def harakatlan(self):
#         return f"{self.model} harakatlanmoqda!"
# m1=Transport("M123","Kawasaki")
# print(m1.harakatlan())
# class Avtomobil(Transport):
#     def harakatlan(self):
#         return f"{self.model} avtomobili yurmoqda!"
# a1=Avtomobil("Gentra","Chevrolet")
# print(a1.harakatlan())
# class Kema(Transport):
#     def harakatlan(self):
#         return f"{self.model} kemasi suzmoqda!"
# k1=Kema("123 BRF","ATM")
# print(k1.harakatlan())

   #qo'shimcha dars
#1
# class Termin:
#     def __init__(self):
#         self.data=dict()
#
#     def qoshish(self,soha,termin):
#         if soha in self.data.keys():
#             self.data[soha].append(termin)
#         else:
#             self.data[soha]=[termin]
#
#     def get_soha(self,soha):
#         return self.data.get(soha)
#     def sohani_top(self,termin):
#         for soha,terminlar in self.data.items():
#             if termin in terminlar:
#                 return soha
#         return "Mavjud emas!"
#
#
#
# t=Termin()
# t.qoshish("mashina","gentra")
# t.qoshish("mashina","cobalt")
# t.qoshish("mashina","malibu")
# t.qoshish("fan","fizika")
# t.qoshish("fan","ona tili")
# print(t.data)
# print(t.get_soha("mashina"))
# print(t.sohani_top("ona tili"))

#      class va obyektlar qoshimcha
# 1
# class Kitob:
#     def __init__(self,nomi,muallifi,sahifalar_soni):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.sahifalar_soni = sahifalar_soni
#     def malumot(self):
#         return f" Nomi:{self.nomi},Muallifi:{self.muallifi},Sahifalar soni: {self.sahifalar_soni}"
# kitob1=Kitob("Qalb iffati","Nurgul","234")
# kitob2=Kitob("otgan kunlar","Abdulla Qodiriy","7654")
# print(kitob1.malumot())
# print(kitob2.malumot())
# 2
# class Avtomobil:
#     def __init__(self,nomi,rangi,yili):
#         self.nomi=nomi
#         self.rangi=rangi
#         self.yili=yili
#     def mashina_haqida(self):
#         return f"Nomi:{self.nomi},rangi:{self.rangi},yili:{self.yili}"
# avtomobil=Avtomobil("gentra","qora","2019")
# avtomobil1=Avtomobil("cobalt","oq","2018")
# print(avtomobil.mashina_haqida())
# print(avtomobil1.mashina_haqida())
# 3
# class Talaba:
#     def __init__(self,ism,yosh,kurs):
#         self.ism=ism
#         self.yosh=yosh
#         self.kurs=kurs
#     def ozini_tanishtir(self):
#         return f"Mening ismim {self.ism},yoshim {self.yosh}da {self.kurs}-kursman"
# talaba=Talaba("Fotima","19","2")
# talaba1=Talaba("Guli","18","1")
# print(talaba.ozini_tanishtir())
# print(talaba1.ozini_tanishtir())
# 4
# class Hayvon:
#     def __init__(self,turi,rangi):
#         self.turi=turi
#         self.rangi=rangi
#     def chaqirish(self):
#         return f"Turi:{self.turi},rangi:{self.rangi}"
# hayvon=Hayvon("mushuk","oq")
# print(hayvon.chaqirish())
# 5
# class Oqituvchi:
#     def __init__(self,ism,fam,tajriba):
#         self.ism = ism
#         self.fam = fam
#         self.tajriba = tajriba
#     def tanishtir(self):
#         return f"Ismi:{self.ism},fam:{self.fam},tajriba:{self.tajriba} yil"
# ustoz=Oqituvchi("gullola","Jaloldinova","3")
# print(ustoz.tanishtir())
#                   darsdagi vazifalar
# 1
# class Mehmon:
#     def __init__(self,ismi,yoshi,email):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.email = email
#     def malumot(self):
#         return f"Ismi:{self.ismi}\n yoshi:{self.yoshi}\n email:{self.email}\n"
# mehmon=Mehmon("lola","23","abdullayevalola@gmail.com ")
# print(mehmon.malumot())
# 2
# class Student:
#     def __init__(self,ism,onatili_bahosi,rustili_bahosi,algebra_bahosi):
#         self.ism = ism
#         self.onatili_bahosi = onatili_bahosi
#         self.rustili_bahosi = rustili_bahosi
#         self.algebra_bahosi = algebra_bahosi
#     def average_grade(self):
#         return f"Ismi:{self.ism}\n onatili:{self.onatili_bahosi}\n rustili:{self.rustili_bahosi}\n algebra:{self.algebra_bahosi}"
# student=Student("Asilbek","5","4","5")
# print(student.average_grade())
# 3
# class Student:
#     def __init__(self,ism,onatili_bahosi,rustili_bahosi,algebra_bahosi):
#         self.ism = ism
#         self.onatili_bahosi = int(onatili_bahosi)
#         self.rustili_bahosi = int(rustili_bahosi)
#         self.algebra_bahosi = int(algebra_bahosi)
#     def average_grade(self):
#         orta=(self.onatili_bahosi+self.rustili_bahosi+self.algebra_bahosi)/3
#         return f"Ismi:{self.ism}\no'rtacha bahosi:{orta}"
# student=Student("Asilbek ","5","4","5")
# print(student.average_grade())
# 4
# class Meva:
#     def __init__(self,rang,narx,kech_pishar):
#         self.rang=rang
#         self.narx=narx
#         self.kech_pishar=kech_pishar
#     def about(self):
#         return f" Rangi={self.rang}\n narxi={self.narx}\n kech_pishar={self.kech_pishar}"
# meva=Meva("qizil","3400","True")
# print(meva.about())
# 5
# class Anor:
#     def __init__(self,rangi,narxi):
#         self.rangi = rangi
#         self.narxi = narxi
#     def about(self):
#         return f"Anorning rangi {self.rangi} boladi,narxi esa {self.narxi}ming "
# anor=Anor("qizil","50000")
# print(anor.about())
# 6
# class Matem:
#     def __init__(self,x,y):
#         self.x=int(x)
#         self.y=int(y)
#     def amallar(self):
#         qoshish=self.x + self.y
#         ayirish=self.x - self.y
#         kopaytirish=self.x * self.y
#         qoldiq_bolish=self.x % self.y
#         daraja=self.x**self.y
#         return f"qoshish={qoshish}\nayirish={ayirish}\nkopaytirish={kopaytirish}\nqoldiq bolish={qoldiq_bolish}\ndaraja={daraja}"
# matem=Matem("10","5")
# print(matem.amallar())
# 7 qoldiq bn qoldiqli bolishni nima farqi bor
# class Matem:
#     def __init__(self,x,y):
#         self.x=int(x)
#         self.y=int(y)
#     def amallar(self):
#         qoldiq=self.x % self.y
#         daraja=self.x ** self.y
#         return f"qoldiq={qoldiq}\ndaraja={daraja}"
# matem=Matem("21","4")
# print(matem.amallar())
#

                   #Market classi
#1
# class Market:
#     def __init__(self):
#         self.mahsulot={}
#     def add_mahsulot(self,nomi,narx):
#         self.mahsulot[nomi]=narx
# market=Market()
# market.add_mahsulot("olma","7000")
# print(market.mahsulot)
#2
# class Market:
#     def __init__(self):
#         self.mahsulot={}
#     def show_mahsulot(self):
#         if not self.mahsulot:
#             return f"hechnarsa yoq"
#         else:
#             for ism,narx in self.mahsulot.items():
#                 return f"{ism}-{narx}ming"
# market=Market("olma","345")
# market.show_mahsulot()
# print(market.show_mahsulot())
#3
# class Market:
#     def __init__(self):
#         self.mahsulot={}
#     def mahsulot_qoshish(self,nomi,narx):
#         self.mahsulotlar[nomi]=int(narx)
#         return f"{nomi} mahsuloti {narx} so'm qoshildi"
#     def narxni_yangilish(self,nomi,yangi_narx):
#         if nomi in self.mahsulot:
#             self.mahsulot[nomi]=int(yangi_narx)
#             return f"{nomi} narxi {yangi_narx} so'mga yangilandi"
#         else:
#             return f"{nomi} bozorda yoq"
# market=Market()
# print(market.mahsulot_qoshish("olma","1200"))
# print(market.narxni_yangilish("banan","3445"))

#1
# sonlar=[23,45,67,88,65,12]
# katta=sonlar[0]
# kichik=sonlar[0]
# for son in sonlar:
#     if son>katta:
#         son=katta
#     if son<kichik:
#         son=kichik
# print(kichik,katta)
#2
# for i in range(6,0,-1):
#      for j in range(1,i+1):
#          print(j,end=" ")
#      print()

#                #Market classi
# #1
# class Matn:
#     def __init__ (self,matn):
#         self.matn=matn
#     def katta_harf(self):
#         return self.matn.upper()
#     def kichik_harf(self):
#         return self.matn.lower()
#     def sonmi(self):
#         return self.matn.isnumeric()
#     def bosh_harf(self):
#         return self.matn.capitalize()
#     def tozalash(self):
#         return self.matn.strip()
# matn=Matn(" mening ismim fotima")
# print(matn.katta_harf())
# print(matn.kichik_harf())
# print(matn.sonmi())
# print(matn.bosh_harf())
# print(matn.tozalash())
# 2
# class Matn:
#     def __init__(self,matn):
#         self.matn=matn
#     def katta_harf(self):
#         return self.matn.upper()
#     def sonmi(self):
#         return self.matn.isnumeric()
# m=Matn("12345")
# if m.katta_harf():
#     print("faqat harflardan iborot")
# else:
#     print("faqat sonlardan iborat")
# 3
# class Queue:
#     def __init__(self):
#         self.n=[]
#     def enqueue(self, element):
#         self.n.append(element)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.n.pop(0)
#         else:
#             return "Navbat qosh"
#     def front(self):
#         if not self.is_empty():
#             return self.n[0]
#         else:
#             return "Navbat bo'sh"
#     def __len__(self):
#         return len(self.n)
#     def is_empty(self):
#         return len(self.n) == 0
# q=Queue()
# print(q.is_empty())
# q.enqueue("F")
# q.enqueue("E")
# q.enqueue("R")
# print(q.front())
# print(len(q))
# print(q.dequeue())
# print(q.is_empty())
# 4
# class Kvadrat:
#     def __init__(self,x,y=2):
#         self.x =int(x)
#         self.y =int(y)
#     def perimeter_top(self):
#         return self.x**2+self.y**2
# kv=Kvadrat(10,2)
# print(kv.perimeter_top())
# #5-6
# class Tortburchak(Kvadrat):
#     def perimetrini_top(self):
#         return (self.x+self.y)*2
#     def yuzani_top(self):
#         return self.x*self.y
# tortburchak=Tortburchak("5","3")
# print(tortburchak.perimetrini_top())
# print(tortburchak.yuzani_top())
# #7
# class Uchish():
#     def __init__(self,manzil,masofa):
#         self.manzil = manzil
#         self.masofa =int(masofa)
#         self.yoqilgi = 7000
#     def hisoblash(self):
#         return self.yoqilgi - self.masofa * 2


#    dars
# file=open("jaloldinova.txt")
# print(file.read())
# file.close()
# file=open("mevalar.txt")
# print(file.read().upper())
# file.close()
# n=int(input("nechta meva kiritmoqchisiz:"))
# with open("mevalar.txt","a") as file:
#     for i in range(1,n+1):
#         meva=input(f"{i}-meva:")
#         file.write(f'{meva}\n')
# 1
# file=open("line.txt")
# print(file.read())
# file.close()
# 2----
# 3
# with open("line.txt") as file:
#     for ism in file:
#         print(ism.strip())
# 4
# file. close qilmasam ham xato chiqarmayaptiyu
# file=open("jaloldinova.txt")
# jaloldinova=file.read()
# file.close()
# print(jaloldinova)
# 5
# kitob=input("kitob nomini kiriting:")
# fayl=open("jaloldinova.txt","a+")
# fayl.seek(0)
# kitoblar=fayl.read()
# if kitob in kitoblar:
#     print("kitobni oling")
# else:
#     print("bunday kitob yo")
#     fayl.write(kitob+"\n")
# fayl.close()
# 6
# fayl=open("jaloldinova.txt","r")
# qatorlar=fayl.readline()
# fayl.close()
# unlilar="euoiaAEUIO"
# for qator in qatorlar[4:6]:
#     if qator[0] in unlilar:
#         print(qator.strip())
# 7
# file=open("madhiya.txt")
# madhiya= len(file.read())
# file.close()
# print(madhiya)
# 8
# file=open("madhiya.txt")
# madhiya=file.read()
# for qator in file:
#     if "O'zbekiston" in qator:
#         print(qator.strip())
# file.close()
# 9----------------
# 10 chala
# file=open("yangi.txt")
# yangi=file.read()
# if yangi>=15:
#     print("15tadan kop")
# else:
#                      20 ta masala
# 1
# file=open("data.txt")
# data=file.read()
# print(data)
# file.close()
# 2
# file=open("madhiya.txt")
# text=file.read()
# file.close()
# print(text)
# 3 har bir qatordagi sozlarni sonini chiqarish uchun nima qilaman
# file=open("yangi.txt")
# text= len(file.read())
# file.close()
# print(text)
# 4
# fayl = open("yangi.txt")
# python_qatorlari = []
# for q in fayl:
#     if "python" in q.lower():
#         python_qatorlari.append(q.strip())
# fayl.close()
# print(python_qatorlari)
# 5
# file=open("yangi.txt")
# text= len(file.read())
# file.close()
# print(text)
# 6
# tinish_belgilari = ".,!?;:–()[]\"'"
# fayl = open("madhiya.txt")
# matn = fayl.read()
# fayl.close()
# topilgan = [b for b in matn if b in tinish_belgilari] # har bir belgini tekshiradi.tinish belgi bolsa qoshadi
# print("Tinish belgilar:", topilgan)
# print("Tinish belgilar soni:", len(topilgan))
# 7
# file=open("yangi.txt","a+")
# file.write("dasturlash-bu san'at")
# file.close()
# 8
# file=open("yangi.txt")
# yangi=file.read()
# file.close()
# print(yangi[::-1])
# 9
# file=open("line.txt")
# line=file.read().split()
# file.close()
# eng_uzun=max(line,key=len)
# print("eng uzun:",eng_uzun)
# print("uzunligi",len(eng_uzun))
# 10
# with open("line.txt") as fayl:
#     matn = fayl.read()
# sozlar = matn.split()
# sozlar.sort()
# for s in sozlar:
#     print(s)
# 11
# with open("data.txt", "r") as manba:
#     matn = manba.read()
# with open("copy.txt", "w") as maqsad:
#     maqsad.write(matn)
# print("Matn  nusxalandi!")
# 12
# with open("madhiya.txt") as file:
#     matn=file.read()
# katta_harf=matn.upper()
# print(katta_harf)
# 13
# file=open("yangi.txt")
# yangi=file.read()
# takrorlanuvchi=yangi.count("gul")
# print(takrorlanuvchi)
# 14----------
# 15
# with open("madhiya.txt") as fayl:
#     matn = fayl.read()
# toza_matn = matn.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(";", "").replace(":", "").replace("–", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("\"", "").replace("'", "")
# print(toza_matn)
# 16
# with open("madhiya.txt") as fayl:
#     qatorlar = fayl.readlines()
# for q in qatorlar:
#     print(q.strip())
# 17--------------
# 18--------------
# 19
# fayllar=["yangi.txt","madhiya.txt","data.txt"]
# file=open("umumiy.txt",'w')
# 20
#
                                 #41-guruh while loop
#1
# while True:
#     print("assalomu alaykum")
#2
# son = int(input("Butun son kiriting: "))
# if son > 0:
#     while son % 3 == 0:
#         son //= 3
#     if son == 1:
#         print("3 ning darajasi")
#     else:
#         print("3 ning darajasi emas")
# else:
#     print("Musbat son kiriting.")
#3
# while True:
#     son=int(input("son kiriting:"))
#     if son<0:
#         print("manfiy son kiritildi:")
#         break
# print("son kiriting:")
#4
# son=int(input("son kiriting:"))
# print(f"{son} sonning boluvchilari:")
# i=1
# while i<=son:
#     if son%i==0:
#         print(i)
#     i+=1
#5---
#6
# son = int(input("Son kiriting: "))
# yigindi = 0
# while son > 0:
#     raqam = son % 10
#     yigindi += raqam
#     son //= 10
# print("Raqamlar yig‘indisi:", yigindi)


#12-dars vazifalari while loop
#1
#while True:
#    print("assalomu alaykum")
#2
#son= int(input('son kiritng:'))
#while son>1:
#    son/=3
#if son==1:
#    print("3 ning darajasi:")
#else:
#    print("3ning darajasi emas:")
#3
#while True:
#    son=int(input("son kiriting:"))
#    if son<0:
#      print("manfiy son kiritildi:")
#      break
#4
#son=int(input("son kiriting:"))
#i=1
#while i<=son:
#    if son%i==0:
#        print(i,end=" ")
#    i+=1
#5---------------------------------
#6---------------------------------
#son=int(input("son kiriitng:"))
#yigindi=0
#for raqam in str(son):
#    if raqam.isdigit():
#        yigindi+=int(raqam)
#print(yigindi)
#7
#parol = "12345"
#urinish = 0
#while urinish < 3:
#    if input("Parolni kiriting: ") == parol:
#        print("Xush kelibsiz!")
#        break
#    urinish += 1
#else:
#    print("3 marta noto'g'ri kiritdingiz. Dastur to'xtadi.")
#8
#a,b =0,1
#for i in range(10):
#    print(a, end=" ")
#    a,b=b,a+b
#9
#son=int(input())
#i=0
#while son:
#    i=i*10+son%10
#    son=son//10
#print(i)
#10
#for i in range(21):
#    print(i)
#11----
#12
#while True:
#    matn=input("matn kiriting:")
#    if matn=="stop":
#        print("toxtatildi")
#        break
#    print("kiritildi matn")
#13------------
#son=input("son kiriting:")
#son1=len(son)
#print(son1,"xona")
#14
#while True:
#    son=int(input("son="))
#    if son<0:
#        print("toxtatildi")
#        break
#    print("davom et")
#15
#yigindi=0
#while True:
#    son = int(input("son="))
#    if son==0:
#        break
#    yigindi+= son
#print(" sonlar yigindisi",yigindi)
#16-----------------buni qayerida xato qilgan bolishim mumkin.
#ortacha=0
#while True:
#    son = input("son kiriting:(exit kiritilsa toxtedi)")
#    if son=="exit":
#        print("toxtadi")
#        break
#    ortacha=sum(son)//len(son)
#print(ortacha)
#17
#while True:
#    login=input("login kiriting:")
#    parol=input("parol kiriting:")
#    if login == "admin" and parol == "1234":
#        print("Xush kelibsiz!")
#        break
#    print("xato,qayta urining:")
#18 ----------
#while True:
#    son = int(input("son="))
#    if son==matn:
#        print("faqat son kiritilganda to‘xtaydi")
#        break
#    print("davom et")
#19
#while True:
#    son=int(input("son kiriting:"))
#    if son>10:
#        print("toxtadi")
#        break
#    print("davom et")
#20
#yigindi=0
#while yigindi<100:
#    son=int(input("son kiriitng:"))
#    yigindi+=son
#print("yigindi 100 ga yetdi yoki oshdi",yigindi)
#21
# while True:
#    son = int(input("son kiriitng:"))
#    if son<0:
#        print("toxtadi")
#        break
#    print("davom et")
#22
#while True:
#    son = int(input("son kiriitng:"))
#    if son%5==0:
#        print("sikl toxtadi")
#        break
#    print("davom et")
#23 menda 3ta sondan kop son sorayapti faqat 3 ta kirishi kk ekan
#while True:
#    son = int(input("son kiriitng:(1-50)"))
#    if son%7==0:
#       print("7 ga karrali son")
#        break
#    print("toxtadi")
#24--
#25
# while True:
#     son=int(input("son kiriting:"))
#     if son%2==0:
#         print("juft son")
#         break
#     print("toq son")
#26----
#27
# while True:
    # parol1='7777'
    # parol=input("parol kiriitng:")
    # if parol==parol1:
    #     print("togri kiritildi")
    #     break
    # print("xato parol kiritildi! yana uruning parol kiriting:")
#28
# while True:
#     x=int(input("x ni kiriting:"))
#     if x**2>500:
#         break
#     else:
#         print("bu sonni kvadrati-",x**2)
#29-
# matn = input("Matn kiriting: ")
# i = 0
# while i < len(matn):
#     print(matn[i])
#     i += 1
                #while loop
#1
# i=1
# while i<=11:
#     print(i)
#     i+=3
#2lasini bir biridan farqi
# for i in range(1,6,3):
#     print(i)
#2
# i=0
# while i<=50:
#     print(i)
#     i+=2
#3
# while True:
#     son = int(input("son kiriting:"))
#
#     if son<0:
#         print("sikl to'xtadi")
#         break
#     else:
#         print("son kiritishda davom eting!")
#3
# i=1
# sum=0
# while i<=100:
#     sum+=i
#     i+=1
# print("1-100gacha sonlar yigindisi=",sum)
#4
# while True:
#     son=int(input("son kiriting:"))
#     if son==0:
#         print("sikl to'xtadi")
#         break
#     else:
#         print("son kiriitng:")
#10
# i=1
# while i<=20:
#     if i%2==0:
#         print(i)
#     else:
#         False
#     i += 1
          #masalalar
#1
# while True:
#     print("salom")
#3
# while True:
#     son=int(input("son kiriting:"))
#     if son<0:
#         print("manfiy son kiritildi:")
#         break
#     else:
#         print("musbat son kiritildi")
#13
# son=123456789
# xona=0
# while son:
#     son//=10
#     xona+=
#     print(xona,"xona")
    #39-guruhdagi vazifalar topshiriqlar
#1 yoshni qana qilib katta kichigini chiqaradi
# import json
# dostlar={
#     "ism":"Rano",
#     "yosh":19,
#     "kasbi":"talaba",
#     "sevimli_rangi":"qora"
# }
# with open("dostlar.json","w") as dost:
#     json.dump(dostlar,dost,indent=2)
#2
# import json
# student={
#     "ism":"fotima",
#     "yosh":19,
#     "fanlar":['algebra','geometriya'],
#     "confirmed":True
# }
# with open('fotima.json', 'w') as json_file:
#     json.dump(student, json_file, indent=3)
#39 guruh
# from collections import Counter
# text=["Namangan",  "chiroyli", "shahar", "Namangan", "Namangan"]
# c=Counter(text)
# print(c)
# print(c.most_common(3))
# print(c.most_common(7))
# print(c.total())
# from bisect import bisect
# ballar=[0,25,55,71,86,100]
# bal=float(input("Balingizni kiriting:"))
# print(f"{bisect(ballar,bal)}-baho oldingiz!")
#                          vazifalar 39-guruh
# 1
# from datetime import datetime
# sana=datetime.today()
# print(sana)
# #2
# from collections import Counter
# fayl=open("madhiya.txt","r+",encoding="utf-8")
# c=Counter(fayl.readlines())
# print(c.most_common(3))
# 3
# import calendar
# print(calendar.TextCalendar().formatyear(2026))
# 4
# from bisect import bisect
# ballar=[0,20,40,60,80,100]
# bal=float(input("balimgizni kiriting:"))
# print(f"{bisect(ballar,bal)}-baho oldingiz")
# 5
# import turtle
# t = turtle.Turtle()
# for i in range(3):
#     t.forward(100)
#     t.left(120)
# turtle.done()
# 6 ------
# import turtle
# t=turtle.Turtle()
# for i in range(4):
#     t.forward(90)
#     t.left(90)
# turtle.done()

# import turtle
# t=turtle.Turtle()
# for i in range(3):
#     t.forward(100)
#     t.left(120)
# turtle.done()
# from datetime import datetime
# sana=datetime.today()
# print(sana)
# import calendar
# print(calendar.TextCalendar().formatyear(2026)
                               #qoshimcha
                               #IF ELIF ELSE
#1
# yosh=int(input("yoshingizni kiriting:"))
# if yosh>18:
#     print("voyaga yetgan")
# else:
#     print("voyaga yetmagan")
#2
# harorat=int(input("harorotni kiritiing:"))
# if harorat<0:
#     print("sovuq")
# elif harorat<=25:
#     print("iliq")
# elif harorat>25:
#     print("issiq")
# else:
#     print()
#3
# sonlar=2345,98765,348765
# print(max(sonlar))
# print(min(sonlar))
#4
# baho=int(input("bahobni kiriting:"))
# if 90<=baho<=100:
#     print("A")
# elif 80<=baho<=89:
#     print("B")
# elif 70<=baho<=79:
#     print("C")
# elif 60<=baho<=69:
#     print("D")
# else:
#     print("F")
#5
# parol=12345678
# parol1=int(input("parol1 ni kiriting:"))
# if parol1==parol:
#     print("Kirish muvaffaqiyatli!!!")
# else:
#     print("Xato parol")
                    # FOR VA WHILE SIKLLARI
#1
# for i in range(1,11):
#     print(i)
#2
# for i in range(0,21,2):
#      print(i)
#3
# son=int(input("son kiriting:"))
# yigindi=0
# for i in range(1,son+1):
#     yigindi+=i
#     print(yigindi)
#4
# for i in range(1,11):
#     print(i,"-pythonni organaman")
#5
# while True:
#     print("salom")
                     #list
#1
# mevalar=['olma','uzum','nok']
# for meva in mevalar:
#      print(meva)
# #2
# mevalar = ['olma', 'uzum', 'nok']
# print(mevalar.append("xurmo"))
# print(mevalar)
# #3
# print(mevalar.pop())
# print(mevalar)
#4
# sonlar=[1,2,3,4,5]
# ortacha=sum(sonlar)/len(sonlar)
# print(ortacha)
#5
# mevalar = ['olma', 'uzum', 'nok']
# meva=input("meva kiriitng:")
# if meva in mevalar:
#     print(mevalar)
# else:
#     print(meva.append(mevalar))







                     #qiziqarli
                     #1
# a=True
# b=False
# natija=a+b
# print(natija)            #1
                     #2
# a=int("85")
# b=int("42")
# print(a==b)                   #false
                    #3
# nums =25
# if nums%5==0:
#     if nums%2==0:
#         print("java")
#     else:
#         print("python")
# else:
#     print("c++")
                 #4
# num=5
# text="hello"
# print(text*num)
                  #5
# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")
                  #6
# print("     *     ")
# print("    ***       ")
# print("   *****       ")
# print("  *******       ")
# print(" *********      ")
                   #7
# for i in range(5):
#     x="* "
#     x=x*i
#     print(f"{x:^10}")
                   #8
# for i in range(5):
#     x="* "
#     x=x*(5-i)
#     print(f"{x:^10}")
                    #9
# for i in range(5):
#     x="* "
#     x=x*i
#     print(f"{x: <10}")
                  #10
# for i in range(5):
#     x="5 "
#     x=x*(5-i)
#     print(f"{x: >10}")
                   #11
# import time
# text="Python is fun!"
# colors=[31,32,33,34,35,36,37]
# for i in range(10):
#     line=""
#     for idx, char in enumerate(text):
#         color_code=colors[(idx+i)%len(colors)]
#         line+=f"\033[1;{color_code}m{char}\033[0m"
#     print(line)
#     time.sleep(0.3)
                       #12
# class Car:
#     def __init__(self):
#         self.wheels=4
# class Horse(Car):
#     def __init__(self):
#         super().__init__()
# my_horse=Horse()
# print(f"My horse has {my_horse.wheels} wheels!")
                     #13
# print("1 ")
# print("1 2")
# print("1 2 3")
# print("1 2 3 4")
# print("1 2 3 4 5")
                    #14
# while True:
#     print(eval(input(">>>")))   # eval natijani qaytaruvchi funksiya
                   #15
# email=input("Enter email: ")
# if "@" in email and "." in email:
#     print("Looks like a valid email")
# else:
#     print("Invalid email format")
                     #16
# print(max(2,345,7654))
# # print(min(2,345,765))
                      #17
# import turtle
# t=turtle.Turtle();t.speed(0)
# for i in range(36):
#     t.circle(60);t.right(10)
#     t.circle(30);t.left(10)
# turtle.done()


# from sqlite3 import connect
# with connect('tanshish.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS ozim (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ism VARCHAR(10) NOT NULL,
#         yosh INTEGER NOT NULL,
#         manzil VARCHAR(35)
#         )
#         """
#     )
# with connect('tanshish.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         INSERT INTO ozim(ism, yosh, manzil)
#         VALUES ("fotima", 19, "namangan"),
#                ("maftuna", 22, "andijon")
#         '''
#     )
# with connect('tanshish.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         """
#         SELECT * FROM ozim
#         """
#     )
#     for row in cursor.fetchall():
#         print(row)

#                                              vazifalar
#                                1
# from sqlite3 import connect
# with connect('talabalar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS talabalar (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ism VARCHAR(10) NOT NULL,
#         yosh INTEGER NOT NULL,
#         kurs INTEGER NOT NULL,
#         """
#                    )
# with connect("talabalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     """
#     INSERT INTO talabalar (id, ism, yosh, kurs)
#     VALUES(1, 'fotima', 19, 2),
#           (2, 'guli', 21, 3),
#           (3, 'lola', 19, 1)
#     """
#                    )
# with connect("talabalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         """
#         SELECT*FROM talabalar
#         """
#     )
#     for row in cursor.fetchall():
#         print(row)
#                          2
# from sqlite3 import connect
# with connect('ustozlar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS ustozlar(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     ism VARCHAR(15) NOT NULL,
#     yosh INTEGER NOT NULL,
#     fan TEXT)
#     ''')
# with connect('ustozlar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     INSERT INTO ustozlar(ism, yosh, fan)
#     VALUES ('shohida', 38, 'fizika'),
#            ('aziza', 44, 'ingliz tili'),
#            ('gulchehra', 34, 'informatika'),
#            ('karima', 43, 'kimyo'),
#            ('zulhumor', 39, 'algebra')
#     '''
#     )
# with connect('ustozlar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     SELECT*FROM USTOZLAR
#     WHERE  fan IN ('kimyo','fizika')
#
#     '''
#     )
# with connect('ustozlar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#             '''
#     SELECT*FROM USTOZLAR
#     WHERE  yosh>20
#             ''' )
#
#     for row in cursor.fetchall():
#          print(row)
#            3
# from sqlite3 import connect
# with connect('maqola.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS maqola(
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     matn VARCHAR(100) NOT NULL,
#     sarlavha VARCHAR(50) NOT NULL,
#     sana INTEGER)
#      ''')
# with connect('maqola.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     INSERT INTO maqola(matn, sarlavha, sana)
#     VALUES ('Dasturlash — bu kompyuterga buyruqlar berib, muammolarni yechish san’ati.', ' daturlash', 5),
#            ('kuz','Oltin so‘z – ton bilan o‘lchanmas',9),
#            ('Sadoqat','Sadoqat – insoniya fazilati',17)
#     '''
#     )
# with connect('maqola.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         SELECT * FROM maqola
#         WHERE ID>5
#         '''
#     )
# with connect('maqola.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         SELECT * FROM maqola
#         WHERE LOWER(sarlavha) LIKE '%ton%' OR LOWER(sarlavha) LIKE '%iya%
#         '''
#     )
#     for row in cursor.fetchall():
#           print(row)




         #41 GURUH
#1
# sonlar=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x: x**2,sonlar)))
#2
# sonlar=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x: x+10,sonlar)))
#3
# sozlar=['fotima','guli','asilbek','maftuna']
# print(list(map(lambda x: x.capitalize(), sozlar)))
#4
# narx=[12,34,5,6,87]
# print(list(map(lambda x: (x*15)/100, narx)))
#5
# sonlar=[0,1,2,3,4,5,6,7,8,9]
# print(list(map(lambda x: x**3, sonlar)))
#6
# sonlar=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x: x%2==0, sonlar)))  #faqat oshalarni chiqarish uchun nima qilamz
#7
# sozlar = ["olma", "banan", "apelsin", "anor", "shaftoli", "nok", "tarvuz"]
# natija = [soz for soz in sozlar if len(soz) > 5]
# print(natija)  # lambda ichida for ishlatib bolmas ekan
#8
# sonlar=[1,2,3,4,-6,-7,-9,5,]
# musbat= [son for son in sonlar if son>=0]
# print(musbat)
#9
# sozlar=['asilbek','fotima','maftuna','ali']
# natija=[soz for soz in sozlar if soz.startswith('a')]
# print(natija)
#10
# yoshlar=[23,15,78,43,12,18]
# natija=[yosh for yosh in yoshlar if yosh>18]
# print(natija)
#11
# ismlar=['asilbek','fotima','maftuna','ali']
# ismlar.sort()
# print(ismlar)
#12
# mevalar = ["olma", "banan", "apelsin", "anor", "shaftoli", "nok", "tarvuz"]
# for idx, meva in enumerate(mevalar, start=1):
#     print(f"{idx}. {meva}")
#13
# kitoblar=['men','ishq','sen']
# for idx,kitob in enumerate(kitoblar, start=1):
#     print(f"{idx}.{kitob}")
#14
# mevalar = ["olma", "banan", "apelsin", "anor", "shaftoli", "nok", "tarvuz"]
# for idx, meva in enumerate(mevalar, start=1):
#     print(f"{idx}: {meva}")
#15
# darslar=['rustili','adabiyot','onatili','algebra']
# for idx, dars in enumerate(darslar,start=1):
#     print(f"{idx}. {dars}")


 # 39 guruhdagi vazifalar
# from sqlite3 import connect
# with connect('ustozlar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS ustozlar(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     ism VARCHAR(15) NOT NULL,
#     yosh INTEGER NOT NULL,
#     fan TEXT)
#     ''')
# with connect('ustozlar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     INSERT INTO ustozlar(ism, yosh, fan)
#     VALUES ('shohida', 38, 'fizika'),
#            ('aziza', 44, 'ingliz tili'),
#            ('gulchehra', 34, 'informatika'),
#            ('karima', 43, 'kimyo'),
#            ('zulhumor', 39, 'algebra')
#     '''
#     )
# with connect('ustozlar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         UPDATE ustozlar
#         SET yosh = yosh + 1
#         WHERE ism = 'shohida'
#         '''
#     )
#     for row in cursor.fetchall():
#         print(row)
# with connect('ustozlar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         SELECT * FROM ustozlar
#         '''
#     )
#     for row in cursor.fetchall():
#         print(row)

             # topshiriq 1-5
# from sqlite3 import connect
# with connect("talabalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         CREATE TABLE IF NOT EXISTS talabalar (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#         ism VARCHAR(15) NOT NULL,
#         yosh INTEGER NOT NULL,
#         kurs INTEGER)
#         '''
#     )
# with connect("talabalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         INSERT INTO talabalar (ism, yosh, kurs)
#         VALUES ('fotima', 19, 2),
#                ('nodira',  18, 1),
#                ('mohinur', 20, 3)
#         '''
#     )
# with connect("talabalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         SELECT * FROM talabalar
#         '''
#     )
#     for row in cursor.fetchall():
#         print(row)
# with connect("talabalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         UPDATE talabalar
#         SET yosh=20
#         WHERE ism = 'fotima'
#         '''
#     )
# with connect("talabalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         SELECT * FROM talabalar
#         WHERE kurs>4
#         '''
#     )
#     for row in cursor.fetchall():
#         print(row)
#         #6-10
# from sqlite3 import connect
# with connect("mahsulotlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         CREATE TABLE IF NOT EXISTS mahsulotlar (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#         NOMI VARCHAR(50) NOT NULL,
#         NARXI INTEGER NOT NULL,
#         SONI INTEGER DEFAULT 0
#         )
#         '''
#     )
# with connect("mahsulotlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         INSERT INTO mahsulotlar (NOMI, NARXI, SONI)
#         VALUES ('REDMI12', 120, 44),
#                ('NOUTBUK', 370, 8),
#                ('TELEVIZOR', 780, 5),
#                ('STOL', 100, 74),
#                ('DOSKA', 34, 9)
#
#         '''
#     )
#     for row in cursor.fetchall():
#         print(row)
# with connect("mahsulotlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         SELECT * FROM mahsulotlar
#         WHERE NARXI > 500
#         '''
#     )
#     for row in cursor.fetchall():
#         print(row)
# with connect("mahsulotlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         SELECT * FROM mahsulotlar
#         '''
#     )
#     for row in cursor.fetchall():
#         print(f"Jami: {row[2] * row[3]}")
# with connect("mahsulotlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         DELETE FROM mahsulotlar
#         WHERE SONI<10
#         '''
#     )
#     print(f"O'chirilgan mahsulotlar soni: {cursor.rowcount}")
# with connect("mahsulotlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         SELECT * FROM mahsulotlar
#         '''
#     )
#     for row in cursor.fetchall():
#         print(row)
# with connect("mahsulotlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute('''
#         SELECT NOMI, NARXI FROM mahsulotlar
#         ORDER BY NARXI DESC
#         LIMIT 1
#         ''')
#     eng_qimmat = cursor.fetchone()
# with connect("mahsulotlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute('''
#       SELECT NOMI, NARXI FROM mahsulotlar
#       ORDER BY NARXI ASC
#       LIMIT 1
#       ''')
#     eng_arzon = cursor.fetchone()
#     print(f"Eng qimmat mahsulot: {eng_qimmat[0]} - {eng_qimmat[1]} so'm")
#     print(f"Eng arzon mahsulot: {eng_arzon[0]} - {eng_arzon[1]} so'm")
                   # vazifalar
# from sqlite3 import connect
# with connect('boshqaruv.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS mahsulotlar(
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     nomi NOT NULL,
#     kategoriya NOT NULL,
#     narxi NOT NULL,
#     soni DEFAULT 0,
#     qoshilgan_sana)
#     '''
#     )
#     # cursor.execute(
#     # '''
#     # CREATE TABLE IF NOT EXISTS sotuvlar(
#     # ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     # mahsulot_id NOT NULL,
#     # miqdor NOT NULL,
#     # jami_summa DEFAULT 0,
#     # sana NOT NULL)
#     # '''
#     # )
#     for row in cursor.fetchall():
#         print(row)
# with connect('mahsulot.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         INSERT INTO mahsulotlar(nomi,kategoriya,narxi,soni,qoshilgan_sana)
#         VALUES ('nomi' ,'kategoriya', 'narxi', 'soni', 'qoshilgan_sana')
#         '''
#     )
# from sqlite3 import connect
# from prettytable import PrettyTable
#
# with connect('tasks.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         CREATE TABLE IF NOT EXISTS tasks (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title VARCHAR(255),
#         status VARCHAR(255) DEFAULT 'todo',
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#          )
#         ''')
# def add_task(title):
#     with connect('tasks.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(
#         '''
#         INSERT INTO tasks (title)
#         VALUES (?)
#         ''',(title,))
#         print(f"Task added successfully (ID: {cursor.lastrowid})")
# def update_task(title):
#     with connect('tasks.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(
#             '''
#             UPDATE tasks
#             SET title = ?
#             WHERE id = ?
#             ''',(new_title, id)
#         )
# def mark_task(id,new_status):
#     with connect('tasks.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(
#             '''
#             UPDATE tasks
#             SET status = ?
#             WHERE id = ?
#             ''',(new_status,id)
#         )
# def delete_task(id):
#     with connect('tasks.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(
#             '''
#             DELETE FROM tasks
#             WHERE id = ?
#             ''',(id,)
#         )
# def list_tasks(status=None):
#     with connect('tasks.db') as connection:
#         cursor = connection.cursor()
#         if status is not None:
#             cursor.execute(
#             '''
#             SELECT * FROM tasks
#             WHERE status = ?
#             ''',(status,)
#         )
#         else:
#             cursor.execute(
#                 '''
#                 SELECT * FROM tasks
#                 '''
#             )
#         tasks = cursor.fetchall()
#         table = PrettyTable()
#         table.field_names = ['id', 'title', 'status', 'created_at']
#         for task in tasks:
#             table.add_row(task)
#         print(table)
# while True:
#     command = input("task-cli")
#     if command.startswith("add"):
#          title=command[5:-1]
#          add_task(title)
#     elif command.startswith("update"):
#         id = command.split()[1]
#         new_title=command[command.index('"') + 1:-1]
#         update_task(id, new_title)
#     elif command.startswith("delete"):
#         id=command.split()[1]
#         delete_task(id)
#     elif command.startswith("mark"):
#         id=command.split()[2]
#         new_status =command.split()[1]
#         mark_task(id,new_status)
#     elif command=="list":
#         list_tasks()
#     elif command.startswith("list"):
#         status=command.split()[1]
#         list_tasks(status)

# class student:
#     def __init__(self,ism,yosh,yonalish):
#         self.ism=ism
#         self.yosh=yosh
#         self.yonalish=yonalish
#     def about(self):
#         return f"Ismim {self.ism} yoshim {self.yosh}da {self.yonalish}da o'qiyman"
# fotima=student('fotima',19,'axborot xavfsizligi')
# rano=student('rano',19,'kompyuter injiniringi')
# print(fotima.about())
# print(rano.about())
from sqlite3 import connect

from Tools.scripts.generate_token import update_file
from aiogram.dispatcher import router
from aiogram.fsm.context import FSMContext

# from prettytable import PrettyTable
# with connect('expense.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS expense
#     (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,title VARCHAR
#     )
#     '''
#     )
                        # vazifalar do'kon boshqaruvi
# from sqlite3 import connect
# with connect("dokon.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS mahsulotlar (
#       id INTEGER PRIMARY KEY AUTOINCREMENT,
#       nomi TEXT NOT NULL,
#       kategoriya TEXT NOT NULL,
#       narxi REAL NOT NULL,
#       soni INTEGER NOT NULL,
#       qoshilgan_sana TEXT NOT NULL
#     ) ''')
#     cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS sotuvlar (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         mahsulot_id INTEGER NOT NULL,
#         miqdor INTEGER NOT NULL,
#         jami_summa NOT NULL,
#         sana TEXT NOT NULL
#     ''')
#     for row in cursor.fetchall():
#          print(row)
# with connect("dokon.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         SELECT * FROM mahsulotlar
#         '''
#     )
  #41-GURUH VAZIFALAR
# class student:
#     def __init__(self,ism,yosh,yonalish):
#         self.ism=ism
#         self.yosh=yosh
#         self.yonalish=yonalish
#     def about(self):
#         return f"Ismim {self.ism} yoshim {self.yosh}da {self.yonalish}da o'qiyman"
# fotima=student('fotima',19,'axborot xavfsizligi')
# rano=student('rano',19,'kompyuter injiniringi')
# print(fotima.about())
# print(rano.about())
                #1
# class Mehmon:
#     def __init__(self,ismi,yoshi,email):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.email = email
#     def tanishtirish(self):
#         return f"Mehmonning ismi {self.ismi} yoshi {self.yoshi} emaili {self.email}"
# mehmon1=Mehmon('Fotima',19,'jaloldinovafotima@gmail.com')
# mehmon2=Mehmon('rano',19,'rana@gmail.com')
# print(mehmon1.tanishtirish())
# print(mehmon2.tanishtirish())
               #2
# class Student:
#     def __init__(self, name, matem,kimyo,tarix):
#         self.name = name
#         self.matem = matem
#         self.kimyo = kimyo
#         self.tarix = tarix
#     def average_grade(self):
#         return f"Ismi {self.name}\n baho1={self.matem}\n baho2={self.kimyo}\n baho3={self.tarix}\n"
# ortacha_baho=Student('Fotima',5, 7,9)
# print(ortacha_baho.average_grade())
#                  #3
# class Student:
#     def __init__(self,ism,onatili_bahosi,rustili_bahosi,algebra_bahosi):
#         self.ism = ism
#         self.onatili_bahosi = int(onatili_bahosi)
#         self.rustili_bahosi = int(rustili_bahosi)
#         self.algebra_bahosi = int(algebra_bahosi)
#     def average_grade(self):
#         orta=(self.onatili_bahosi+self.rustili_bahosi+self.algebra_bahosi)/3
#         return f"Ismi:{self.ism}\no'rtacha bahosi:{orta}"
# student=Student("fotima ","5","4","5")
# print(student.average_grade())
#                       #4
# class Meva:
#     def __init__(self,rang,narx,kech_pishar):
#         self.rang=rang
#         self.narx=narx
#         self.kech_pishar=kech_pishar
#     def about(self):
#         return f" Rangi={self.rang}\n narxi={self.narx}\n kech_pishar={self.kech_pishar}"
# meva=Meva("qizil","3400","True")
# print(meva.about())
#                       #5
# class Anor:
#     def __init__(self,rangi,narxi):
#         self.rangi = rangi
#         self.narxi = narxi
#     def about(self):
#         return f"Anorning rangi {self.rangi} boladi,narxi esa {self.narxi}ming "
# anor=Anor("qizil","50000")
# print(anor.about())
#                      #6-7
# class Matem:
#     def __init__(self,x,y):
#         self.x=int(x)
#         self.y=int(y)
#     def amallar(self):
#         qoshish=self.x + self.y
#         ayirish=self.x - self.y
#         kopaytirish=self.x * self.y
#         qoldiq_bolish=self.x % self.y
#         daraja=self.x**self.y
#         return f"qoshish={qoshish}\nayirish={ayirish}\nkopaytirish={kopaytirish}\nqoldiq bolish={qoldiq_bolish}\ndaraja={daraja}"
# matem=Matem("10","5")





# from sqlite3 import connect
# from prettytable import PrettyTable
# with connect('expense.db') as connection:      # EXPENSE-HARAJATLAT
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS expense(
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     info TEXT,
#     amount NUMERIC NOT NULL
#     ''')
# def add_expense(info,amount):
#     with connect('expense.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(
#         '''
#         INSERT INTO expense(info, amount)
#         VALUES(?, ?)
#         ''', (info,amount))
#         print(f"Added {amount} to expense")
# def update_expense(info,amount):
#     with connect('expense.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(
#         '''
#         UPDATE expense SET info = ?, amount = ?
#         WHERE ID = ?
#         ''', (info,amount,info))
# def delete_expense(info):
#     with connect('expense.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute(
#         '''
#         DELETE FROM expense WHERE ID = ?
#         ''', (info,))
#     with (connect('expense.db')) as connection:
#         cursor = connection.cursor()
#         cursor.execute(
#             '''
#             SELECT*FROM expense
#             ''')
#         expense = cursor.fetchall()
#         expense = PrettyTable(expense)
#         table=PrettyTable([
#             'ID',
#             'info',
#             'amount',
#         ])
#         for exp in expense:
#             table.add_row(exp)
#         print(table)
# while True:  damon ettir




#41-GURUH



# class Stack:
#     def __init__(self):
#         self.stack = list()
#     def push(self, item):
#         self.stack.append(item)
#     def pop(self):
#         return self.stack.pop()
#     def peek(self):
#         return self.stack[-1]
#     def size(self):
#         return len(self.stack)
#     def is_empty(self):
#         if len(self.stack)==0:
#             return True
#         else:
#             return False
#     def __str__(self):
#         return f"Stack{self.stack}"
# my_stack = Stack()
# print(my_stack.is_empty())
# my_stack.push('olma')
# my_stack.push('behi')
# my_stack.push('olcha')
# my_stack.push('gilos')
# print(my_stack)
# print(my_stack.is_empty())
# print(my_stack.is_empty())
# print(my_stack.peek())
                  #IMTIHON 39-GURUH
#2-3
# from sqlite3 import connect
# with connect('uztozlar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS ustozlar (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     ism VARCHAR(15) NOT NULL,
#     familiya VARCHAR(23) NOT NULL,
#     fan VARCHAR(14),
#     yosh INTEGER NOT NULL
#     ''')
#     for row in cursor.fetchall():
#          print(row)
# with connect('uztozlar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     INSERT INTO uztozlar (ism, familiya, fan, yosh)
#     VALUES('mamura', 'ganiyeva', 'matematika', 34)
#     ''')
#     for row in cursor.fetchall():
#         print(row)
#5----
# with connect('uztozlar.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#     '''
#     SELECT * FROM uztozlar
#     WHERE  = ?
#     ''')
#     for row in cursor.fetchall():
#         print(row)
#6-7
# class Matematika:
#     def __init__(self, x,y):
#         self.x = x
#         self.y = y
#     def daraja(self):
#         daraja=self.x**self.y
#         qoldiqli_bol=self.x/self.y
#         qoldiqsiz_bol=self.x//self.y
#         qoldiqni_top=self.x%self.y
#         return f"daraja={daraja}\nqoldiqli_bol={qoldiqli_bol}\nqoldiqsiz_bol={qoldiqsiz_bol}\nqoldiqni_top={qoldiqni_top}\n"
# matematika = Matematika(10, 2)
# print(matematika.daraja())
#18
# import json
# student={
#     "ism":"Umar",
#     "yosh":15,
#     "shahar":"Fergana"
# }
# with open("student.json","w") as student:
#     json.dump(student,student,indent=2)
#19
# import json
# fotima={
#     "ism":"fotima",
#     "yosh":19,
#     "shahar":"Namangan"
# }
# with open ("fotima.json",'w') as ozim:
#     json.dump(fotima,ozim,indent=2)
#11
# class Queue:
#     def __init__(self):
#         self. queue = list()
#     def push(self, item):
#         return self.queue.push(item)
#     def pop(self):
#         return self.queue.pop()
#     def front(self):
#         return self.queue[0]
# my_Queue = Queue()
# print(my_Queue.push())
# print(my_Queue.pop())
# print(my_Queue.front())
#13
# class Queue:
#     def __init__(self):
#         self.queue = []
#     def size(self):
#            return len(self.queue)
#     def is_empty(self):
#         if len(self.queue)==0:
#             return True
#         else:
#             return False
#     def __str__(self):
#             return f"Queue{self.queue}"
# my_queue = Queue()
# print(my_queue.is_empty())
#12
 #6,7,8,9,10 chunki har safar 5ga 1ni qoshib ketadi, a=10 teng bolganda toxtaydi.
#16
# with open("kitobxon.cvs","r") as f:
#     cvs = f.read()
#     print(cvs)
#15
# class Deque:
#     def __init__(self):
#         self.deque = deque()
#     def append(self, value):
#         self.deque.append(value)
#     def popleft(self):
#         return self.deque.popleft()
#     def pop(self):
#         return self.deque.pop()
# myDeque = Deque()
# print(myDeque.append('olma'))
# print(myDeque.append('behi'))
# print(myDeque.append('olcha'))
# print(myDeque.append('gilos'))
# print(myDeque.popleft())
# print(myDeque.pop())



# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
#
# TOKEN = "8382867061:AAF3cKnamafTHssTRVK8KabDyob9A6CRWgk"
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# @dp.message(Command("start"))
# async def start_handler(message: types.Message):
#     await message.answer("Assalomu alaykum! Bot ishga tushdi ")
# @dp.message(Command("help"))
# async def help_handler(message: types.Message):
#     await message.answer(
#         "Yordam:\n"
#         "/start- botni ishga tushurish\n"
#         "help-yordam olish"
#     )
# @dp.message(Command("info"))
# async def info_handler(message: types.Message):
#     await message.answer(
#         "Ism: Fotima\n"
#         "Yosh: 19\n"
#         "Kasb: talaba"
#     )
# async def main():
#     print("Bot ishga tushdi...")
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())

            # topshiriqlar bot
# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from datetime import datetime
# from random import randint
# TOKEN ="8202947468:AAG6sHdHZYJ7xRnXZVMVEYsH8KDzdenea_0"
# bot=Bot(token=TOKEN)
# dp=Dispatcher()
# @dp.message(Command("start"))
# async def start_handler(message: types.Message):
#     await message.answer(
#         "Assalomu alaykum😊!"
#     )
# @dp.message(Command("bugun"))
# async def bugun_handler(message: types.Message):
#     today = datetime.now().strftime("%d-%B, %Y")
#     await message.answer(f"bugun: {today}")
#
# @dp.message(Command("vaqt"))
# async def vaqt_handler(message: types.Message):
#     now=datetime.now().strftime("%H:%M")
#     await message.answer(f"now: {now}")
# @dp.message(Command("random"))
# async def random_handler(message: types.Message):
#     son = random.randint(1,100)
#     await message.answer(f"son:{son}")
# @dp.message()
# async def message_handler(message: types.Message):
#     await message.answer("Men faqat choy damledigan bot😬")
# async def main():
#     print("bot ishlamoqda")
#     await dp.start_polling(bot)
# if __name__ == "__main__":
#     asyncio.run(main())
                     #41-guruh
# fayl=open("davlatlar.txt")
# print(fayl.read())
# fayl.close()
# fayl=open("madhiya.txt")
# print(fayl.read(12))
# print(fayl.read())
# fayl.seek(0)
# fayl.close()


# fayl=open("davlatlar.txt")
# print(fayl.readline())
# fayl.close()

# fayl=open("davlatlar.txt")
# lines=fayl.readlines()
# for line in lines:
#     print(line.upper(),end="")
# fayl.close()
#1
# fayl=open("davlatlar.txt","w")
# davlat=input('yangi davlat:')
# fayl.write(davlat)
# fayl.close()
#2
# fayl=open("davlatlar.txt","a")
# davlat=input('yangi davlat:')
# fayl.write(davlat + "\n")
# fayl.close()
# with open("musiqa.txt",'r+') as f:
#     musiqa = f.read()
#     print(musiqa.replace('janona','gul'))
# f.close()
                #topshiriqlar
#1-2
# fayl=open("data.txt")
# print(fayl.read())
# fayl.close()
# 3-4 qatorni qande ajratamiz.
#5
# fayl=open("data.txt")
# print(len(fayl.read()))
# fayl.close()
#6
# matn = input("Matn kiriting: ")
# belgilar_soni = len(matn)
# print("Jami belgilar soni:", belgilar_soni)
#7
# with open("data.txt", "a") as file:
#     file.write("Dasturlash – bu san’at")
# file.close()
#8
# fayl=open("data.txt")
# print(fayl.read()[::-1])
# fayl.close()
#9
# with open("data.txt", "r") as file:
#     matn = file.read()
# sozlar = matn.split()
# eng_uzun = max(sozlar, key=len)
# print("Eng uzun so‘z:", eng_uzun)
#10
# with open("data.txt", "r") as file:
#     matn = file.read()
#     sozlar=matn.split("\n")
#     tartib=sorted(sozlar)
#     print(tartib)
#12
# with open("data.txt") as f:
#     matn=f.read()
#     print(matn.upper())
#13
# with open("data.txt") as f:
#     matn=f.read()
#     print(matn.count())
#15 tinish belgilarni qande belgilab olsak boladi
# with open("data.txt") as f:
#     matn=f.read()
#     print(matn.replace(".", " "))
# f.close()
#16
# with open("davlatlar.txt") as f:
#     matn=f.read()
#     print(matn.split(" "))
#17
#chiqmaganlari 3,4,11,14,17-20




                 # bot yaratish vazifa26_bot


# import asyncio
# from aiogram import Bot, Dispatcher,types,F
# from aiogram.filters import Command
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
#
# TOKEN = '8202947468:AAG6sHdHZYJ7xRnXZVMVEYsH8KDzdenea_0'
#
# bot = Bot(token=TOKEN)
# dp=Dispatcher()
#
# lang_buttons=InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="🇺🇿 O'zbekcha",callback_data="lang_uz")],
#         [InlineKeyboardButton(text="🇹🇷 turkcha",callback_data="lang_turk")],
#         [InlineKeyboardButton(text="🇬🇧 English",callback_data="lang_eng")],
#
#     ]
# )
# contact_buttons=ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="☎️Telefon raqamni yuborish",request_contact=True)],
#         [KeyboardButton(text="📍Lokatsiya yuborish",request_location=True)],
#     ],
#     resize_keyboard=True,
# )
# @dp.message(Command('start'))
# async def start(message: types.Message):
#     await message.answer('Xush kelibsiz!😊', reply_markup=lang_buttons)
# @dp.callback_query(F.data == 'lang_uz')
# async def lang_uz(callback: types.CallbackQuery):
#     await callback.message.answer("🇺🇿 O'zbekcha tili tanlandi!")
#     await callback.answer()
# @dp.callback_query(F.data=='lang_turk')
# async def lang_turk(callback: types.CallbackQuery):
#     await callback.message.answer("🇹🇷 turkcha tili tanlandi!")
#     await callback.answer()
# @dp.callback_query(F.data=='lang_eng')
# async def lang_eng(callback: types.CallbackQuery):
#     await callback.message.answer("🇬🇧 English  tili tanlandi!")
#     await callback.answer()
# async def main():
#     print('bot started')
#     await dp.start_polling(bot)
#
# @dp.message(Command('contact'))
# async def contact(message: types.Message):
#     await message.answer(
#         "shaxsiy malumotlarni ulashish:",
#         reply_markup=contact_buttons,
#     )
# @dp.message(F.contact)
# async def contact(message: types.Message):
#     phone_number = message.contact.phone_number
#     await message.answer(f"Raqamingiz ro'yxatga qo'shildi:\n"
#                          f"{phone_number}\n"
#                          f"Tez orada siz bilan bog'lanamiz!")
# @dp.message(F.location)
# async def location(message: types.Message):
#     location_x = message.location.latitude
#     location_y = message.location.longitude
#     await message.answer(f"Manzil qabul qilindi:{location_x},{location_y}")
#     #topshiriq
# @dp.message(Command("test"))
# async def test_handler(message: types.Message):
#     keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="50sekund", callback_data="ans_wrong")],
#         [InlineKeyboardButton(text="60sekund", callback_data="ans_correct")],
#         [InlineKeyboardButton(text="100sekund", callback_data="ans_wrong")],
#         [InlineKeyboardButton(text="120 sekund", callback_data="ans_wrong")]
#     ])
#     await message.answer("1minutda necha sekund bor?", reply_markup=keyboard)
#
# @dp.callback_query(F.data == "ans_correct")
# async def correct_answer(callback: types.CallbackQuery):
#     await callback.message.answer("✅ To'g'ri javob!")
#     await callback.answer("To'g'ri!", show_alert=True)
#
# @dp.callback_query(F.data == "ans_wrong")
# async def wrong_answer(callback: types.CallbackQuery):
#     await callback.message.answer("❌ Noto'g'ri javob!")
#     await callback.answer("Noto'g'ri!", show_alert=True)
#
#
#
# @dp.message()
# async def echo_handler(message: types.Message):
#     await message.answer(message.text)
# if __name__ == '__main__':
#     asyncio.run(main())

# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# import random
# from aiogram.types import InlineKeyboardButton
# Token="8202947468:AAG6sHdHZYJ7xRnXZVMVEYsH8KDzdenea_0"
# bot = Bot(token=Token)
# dp=Dispatcher()
# @dp.message(Command("oyin"))
# async def start_command(message: types.Message):
#     tugmalar=["🔴","🟠","🟡"]
#     yutuq=random.choice(tugmalar)
#     keyboard = types.InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text=t, callback_data=f"{t}_{yutuq}")
# for t in tugmalar             ]
#         ]
#     )
#     await message.answer("Tugmalardan birini tanlang!!!", reply_markup=keyboard)
# @dp.callback_query()
# async def callback_query(message: types.CallbackQuery, data: types.CallbackQuery):
#     butn, win = callback_query.data.split("_")
#     if butn == "win":
#         await message.answer("Siz togri topdingiz tabrikleman")
#     else:
#         await callback_query.answer("Javobingiz notogri iltimos qayta unirinib korin")
# async def main():
#     await dp.start_polling(bot)
# if __name__ == "__main__":
#     asyncio.run(main())
#             41 - guruhdagi mavzu json
# import json
# student={
#     "ism":"fotima",
#     "yosh":19,
#     "fanlar":['algebra','geometriya'],
#     "confirmed":True
# }
# with open('fotima.json', 'w') as json_file:
#     json.dump(student, json_file, indent=3)
#    toshiriqlar
# 1
# import json
# kitoblar={
#     "sarlavha":"qalb iffati",
#     "muallifi":"nurgul",
#     "yili":2020,
#     "janr":"badiiy"
# }
# with open("kitoblar.json","w") as kitob:
#     json.dump(kitoblar,kitob,indent=4)
#   1
# import json
# dostlar=[{
#     "ism":"Rano",
#     "yosh":19,
#     "kasbi":"talaba",
#     "sevimli_rangi":"qora"
# },
#     {
#         "ism":"guli",
#         "yosh":23,
#         "kasbi":"talaba",
#         "sevimli_rangi":"oq"
#     },
#     {
#         "ism":"durdona",
#         "yosh":24,
#         "kasbi":"talaba",
#         "sevimli_rangi":"sariq"
#     }]
# with open("dostlar.json","w") as dost:
#     json.dump(dostlar,dost,indent=2)
# import json
# with open("dostlar.json", "r", encoding="utf-8") as file:
#     royxat = json.load(file)
# eng_yosh = min(royxat, key=lambda d: d["yosh"])
# eng_katta = max(royxat, key=lambda d: d["yosh"])
# print("Eng yosh do‘st:")
# print(eng_yosh)
# print("\nEng katta do‘st:")
# print(eng_katta) #oxiri yangi rang statistikasini yarating:
# 2
# import csv
# kitoblar = [
#     ["Yanvar", "Alkimyogar", 210, "Roman"],
#     ["Fevral", "Sariq devni minib", 150, "Fantastika"],
#     ["Mart", "Ikki eshik orasi", 350, "Dramma"],
#     ["Aprel", "Tutun", 280, "Roman"],
#     ["May", "Boy ota kambag'al ota", 320, "Biznes"],
#     ["Iyun", "Dunyoning ishlari", 200, "Hikoya"],
#     ["Iyul", "Shaytanat", 450, "Detektiv"],
#     ["Avgust", "O‘tkan kunlar", 280, "Roman"],
#     ["Sentyabr", "Askar o‘g‘li", 190, "Dramma"],
#     ["Oktyabr", "Ufq", 360, "Roman"],
#     ["Noyabr", "Olam-alam odamlar", 240, "Hikoya"],
#     ["Dekabr", "Atlas Shrugged", 550, "Roman"]
# ]
# with open("kitobxon.csv", "w", newline="", encoding="utf-8") as file:#newline=CSV faylda har bir yozuvdan keyin bitta bo‘sh qator qo‘shilib ketadi.
#     yozuvchi = csv.writer(file)
#     yozuvchi.writerow(["oy", "kitob_nomi", "sahifalar_soni", "janr"])# 1 qator yozadi
#     yozuvchi.writerows(kitoblar)
# print("kitobxon.csv yaratildi!")
# #Har bir janr bo'yicha o'qilgan kitoblar sonini chiqaring.
# import csv
# from collections import Counter
# janrlar = []
# with open("kitobxon.csv", "r", encoding="utf-8") as file:
#     oquvchi = csv.DictReader(file)
#     for qator in oquvchi:
#         janrlar.append(qator["janr"])
# statistika = Counter(janrlar)
# print("Janrlar bo‘yicha statistika:")
# for janr, soni in statistika.items():
#     print(janr, ":", soni)
# 3 jsondan csv ga otkazish dostlar.json -> dostlar.csv
# import json
# import csv
# with open("dostlar.json", "r", encoding="utf-8") as f:
#     dostlar = json.load(f)
# with open("dostlar.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["ism", "yosh", "kasbi", "sevimli_rangi"])
#     for d in dostlar:
#         writer.writerow([d["ism"], d["yosh"], d["kasbi"], d["sevimli_rangi"]])
# print("dostlar.csv yaratildi!")
# #kitobxon.csv -> kitobxon.json
# import csv
# import json
# with open("kitobxon.csv", "r", encoding="utf-8") as f:
#     oquvchi = csv.DictReader(f)
#     kitoblar = list(oquvchi)
# with open("kitobxon.json", "w", encoding="utf-8") as f:
#     json.dump(kitoblar, f, ensure_ascii=False, indent=4)
# print("kitobxon.json yaratildi!")
#
# load=> ichiga oladi(matndan obyektga)
# dump=>tashlaydi(obyektdan matnga)
#            takrorlash
# 6
# import json
# matematika=int(input("matematika bahosini kiriting:"))
# fizika=int(input(" fizika bahosini kiriting:"))
# ingliz_tili=int(input(" ingliz tili bahosini kiriting:"))
#
# ballar = {
#     "matem": matematika,
#     "fizika": fizika,
#     "ingliz": ingliz_tili,
# }
# with open("Dictionaryni.json","w") as file:
#     json.dump(ballar,file)
# 7
# import json
# with open("Dictionaryni.json") as file:
#     baholar = json.load(file)
#     max_baho=0
#     max_fan=None
#     for fan, baho in baholar.items():
#         if baho > max_baho:
#             max_baho=baho
#             max_fan=fan
#     print(max_baho, max_fan)
# 8
# import json
# with open("Dictionaryni.json") as file:
#     baholar = json.load(file)
#     max_baho=0
#     max_fan=None
#     print(sum(baholar.values())/len(baholar))
# 9
# import csv
# with open("imdb.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         sarlavha = row["Title"]
#         if len(sarlavha.split())>3:
#             print(sarlavha)
# 10
# import csv
# with open("imdb.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         Rate=float(row["Rate"])
#         if Rate >=9.2:
#             print(Rate)
# 12 xato bor
# import csv
# with open("imdb.csv", newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         Title = row["Title"]
#         if int(Title[-5:-1]) > 2010:
#             print(row['Title'])
# 13--------------
#14 xato bor
# import json
# with open("dostlar.json","r") as file:
#     data = json.load(file)
# fan=input("Fanni kirit:")
# baho=int(input("Baho kirit:"))
# data[fan]=baho
# with open("dostlar.json","w") as file:
#     json.dump(data,file)
# print("baho qoshildi")
#15
# import csv
# with open("imdb.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         Duration=row["Duration"]
#         Duration=int(Duration.split(" ")[0])
#         if Duration<120:
#             print(Duration)
                          #bot
# from aiogram import dp
# from aiogram.filters import Command
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.fsm.context import FSMContext
# class RegisterStates(StatesGroup):
# @dp.message(Command("register"))
# async def start_register(messege:Message,state:FSMContext):
#     await message.answer("Ismingizni kiriting:")
#     await state.set_state(RegisterStates.name)
# @dp.message(Command("register"))
# async def get_name(messege:Message,state:FSMContext):
#     await state.update_data(name=message.text)
#     await messege.answer("Yoshingizni kiriting:")
#     await state.set_state(RegisterStates.age)
# @dp.mesage(RegisterStates.age)
# async def get_age(messege:Message,state:FSMContext):
#     if not message.text.isdigit():
#         return await messege.answer("Yosh faqat son bo'lishi kerak!")
#     await state.update_data(age=message.text)
#     await messege.answer("Telefon raqqamingizni kiriting:")
#     await state.set_state(RegisterStates.phone)
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message, CallbackQuery
#
# kurs_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Backend🥇",callback_data="backend")],
#         [InlineKeyboardButton(text="Frontend🌐",callback_data="Frontend")],
#         [InlineKeyboardButton(text="SMM🎥",callback_data="SMM")],
#         [InlineKeyboardButton(text="Grafik dizayn📈",callback_data="Grafik dizayn")],
#
#     ]
# )
# @dp.message(RegisterStates.phone)
# async def get_phone(messege:Message,state:FSMContext):
#     await state.update_data(phone=message.text)
#     await message.answer("Qaysi kursda o'qimoqchisiz?" reply_markup=kurs_markup)
#     await state.set_state(RegisterStates.kurs)
# tajriba_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Bor",callback_data="bor")],
#         [InlineKeyboardButton(text="Yo'q",callback_data="yoq")],
#     ]
# )
# vaqti_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="09:00–13:00",callback_data="09:00–13:00")],
#         [InlineKeyboardButton(text="14:00–18:00",callback_data="14:00–18:00")],
#     ]
# )
# yakuniy_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Tasdiqlayman✅",callback_data="tasdiqlayman")],
#         [InlineKeyboardButton(text="Bekor qilindi❌",callback_data="bekor qilindi")],
#
#     ]
# )
# @dp.callback_query(RegisterStates.tajriba)
# async def get_tajriba(callback:CallbackQuery,state:FSMContext):
#     await state.update_data(tajriba=callback.data)
#     data=await state.get_data()
#     text=(
#         "Ro'yxatdan o'tish malumotlar:*\n\n"
#         f"Ism:{data['name']}\n"
#         f"Yosh🔢:{data['age']}\n"
#         f"Telefon☎️:{data['phone']}\n"
#         f"Lavozim🌀:{data['lavozim']}\n"
#         "HURMATLI MIJOZ MA'LUMOTLARINGIZ TO'G'RIMI?😊"
#     )
#     await callback.message.edit_text(text,
#                                      reply_markup=kurs_markup,
#                                      parse_mode="Markdown")
#     await state.set_state(RegisterStates.confirm)
# @dp.callback_query(RegisterStates.confirm, lambda c: c.data == "confirm_yes")
# async def confirm_register(callback: CallbackQuery, state: FSMContext):
#     await callback.message.edit_text(
#         "*Tabriklaymiz!*\nSiz muvaffaqiyatli ro‘yxatdan o‘tdingiz.🤩",
#         parse_mode="Markdown"
#     )
#     await state.clear()
# @dp.callback_query(RegisterStates.confirm, lambda c: c.data == "confirm_no")
# async def cancel_register(callback: CallbackQuery, state: FSMContext):
#     await state.clear()
#     await callback.message.edit_text(
#         "Hurmatli mijoz malumotlar bekor qilindi.❌\n"
#         "Iltimos, qayta /register orqali ro‘yxatdan o‘ting.↩️"
#     )

















# from aiogram import Bot, Dispatcher
# from aiogram.filters import Command
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.fsm.context import FSMContext
# from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
#
# TOKEN = "8010488853:AAGQnt4B-X2LChkQTaZjnPTgC8E54SSx8QY"
#
# bot = Bot(TOKEN)
# dp = Dispatcher()
#
# # STATES
# class RegisterStates(StatesGroup):
#     name = State()
#     age = State()
#     phone = State()
#     kurs = State()
#     tajriba = State()
#     vaqt = State()
#     confirm = State()
# # KURS TANLASH KNOPKALARI
# kurs_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Backend🥇", callback_data="backend")],
#         [InlineKeyboardButton(text="Frontend🌐", callback_data="frontend")],
#         [InlineKeyboardButton(text="SMM🎥", callback_data="smm")],
#         [InlineKeyboardButton(text="Grafik dizayn📈", callback_data="design")],
#     ]
# )
# tajriba_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Bor", callback_data="bor")],
#         [InlineKeyboardButton(text="Yo'q", callback_data="yoq")],
#     ]
# )
# vaqt_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="09:00–13:00", callback_data="09-13")],
#         [InlineKeyboardButton(text="14:00–18:00", callback_data="14-18")],
#     ]
# )
# confirm_markup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Tasdiqlayman✅", callback_data="confirm_yes")],
#         [InlineKeyboardButton(text="Bekor qilindi❌", callback_data="confirm_no")],
#     ]
# )
# @dp.message(Command("register"))
# async def start_register(message: Message, state: FSMContext):
#     await message.answer("Ismingizni kiriting:")
#     await state.set_state(RegisterStates.name)
# # GET ism
# @dp.message(RegisterStates.name)
# async def get_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer("Yoshingizni kiriting:")
#     await state.set_state(RegisterStates.age)
# # GET yosh
# @dp.message(RegisterStates.age)
# async def get_age(message: Message, state: FSMContext):
#     if not message.text.isdigit():
#         await message.answer("Yosh faqat son bo‘lishi kerak!")
#         return
#     await state.update_data(age=message.text)
#     await message.answer("Telefon raqamingizni kiriting:")
#     await state.set_state(RegisterStates.phone)
# #GET PHONE
# @dp.message(RegisterStates.phone)
# async def get_phone(message: Message, state: FSMContext):
#     await state.update_data(phone=message.text)
#     await message.answer("Qaysi kursni tanlaysiz?", reply_markup=kurs_markup)
#     await state.set_state(RegisterStates.kurs)
# #GET KURS
# @dp.callback_query(RegisterStates.kurs)
# async def get_kurs(callback: CallbackQuery, state: FSMContext):
#     await state.update_data(kurs=callback.data)
#     await callback.message.edit_text(
#         "Tajriba bormi?", reply_markup=tajriba_markup
#     )
#     await state.set_state(RegisterStates.tajriba)
# # GET TAJRIBA
# @dp.callback_query(RegisterStates.tajriba)
# async def get_tajriba(callback: CallbackQuery, state: FSMContext):
#     await state.update_data(tajriba=callback.data)
#     await callback.message.edit_text(
#         "Qaysi vaqtda o‘qimoqchisiz?", reply_markup=vaqt_markup
#     )
#     await state.set_state(RegisterStates.vaqt)
# #GET VAQT
# @dp.callback_query(RegisterStates.vaqt)
# async def get_time(callback: CallbackQuery, state: FSMContext):
#     await state.update_data(vaqt=callback.data)
#     data = await state.get_data()
#
#     text = (
#         "*Ro‘yxatdan o‘tish ma’lumotlari:*\n\n"
#         f"👤 Ism: *{data['name']}*\n"
#         f"🔢 Yosh: *{data['age']}*\n"
#         f"☎️ Telefon: *{data['phone']}*\n"
#         f"📚 Tanlangan kurs: *{data['kurs']}*\n"
#         f"🧪 Tajriba: *{data['tajriba']}*\n"
#         f"⏰ Vaqt: *{data['vaqt']}*\n\n"
#         "HURMATLI MIJOZ, MA'LUMOTLAR TO‘G‘RIMI?"
#     )
#
#     await callback.message.edit_text(
#         text,
#         reply_markup=confirm_markup,
#         parse_mode="Markdown"
#     )
#     await state.set_state(RegisterStates.confirm)
# @dp.callback_query(RegisterStates.confirm, lambda c: c.data == "confirm_yes")
# async def confirm_register(callback: CallbackQuery, state: FSMContext):
#     await callback.message.edit_text(
#         "*Tabriklaymiz!*\nSiz muvaffaqiyatli ro‘yxatdan o‘tdingiz.🤩",
#         parse_mode="Markdown"
#     )
#     await state.clear()
# @dp.callback_query(RegisterStates.confirm, lambda c: c.data == "confirm_no")
# async def cancel_register(callback: CallbackQuery, state: FSMContext):
#     await state.clear()
#     await callback.message.edit_text(
#         "Hurmatli mijoz, ma’lumotlar bekor qilindi❌\n"
#         "Iltimos, qayta /register orqali ro‘yxatdan o‘ting.↩️"
#     )
#
#
# async def main():
#     print("Bot ishga tushdi...")
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())

              #vazifalar
#1
# import datetime
# print(datetime.datetime.now())
#2
# from collections import Counter
# with open("data.txt",encoding="utf-8") as f:
#     matn=f.read()
# print(Counter(matn).most_common(3))
#3
# import calendar
# print(calendar.TextCalendar().formatyear(2026))
#4
# import bisect
# son=int(input("1-100 gacha son kiriting:"))
# baholar=[20,40,60,80,100]
# baho=bisect.bisect(baholar,son)
# print(f"sizning bahongiz:{baho}")
#5
# import turtle
# for i in range(3):
#     turtle.forward(100)
#     turtle.left(120)
# turtle.done()
#6
                #lunh algoritmi
# 2+5+1+0+0+6+6+9 toq ozgarmagan
# 8+8+2+0+8+0+0+7 juft*2 agar 10dan katta bolsa 9ni ayrimiz
# 29+33


                     #41-guruh topshiriqlari
# from sqlite3 import connect
# with connect("kursdoshlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         CREATE TABLE IF NOT EXISTS kursdoshlar (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#         ism VARCHAR(15) NOT NULL,
#         yosh INTEGER NOT NULL,
#         kurs INTEGER)
#         '''
#     )
# with connect("kursdoshlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     INSERT INTO kursdoshlar (ism, yosh, kurs)
#     VALUES
#     ("Fotima", 19, 2),
#     ("Durdona",22, 3),
#     ("Guli", 20, 1)
#     """)
# with connect("kursdoshlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     SELECT * FROM kursdoshlar
#     WHERE KURS >2
#     """)
# for row in cursor.fetchall():
#     print(row)

                 #MAHSULOTLAR JADVALI
# from sqlite3 import connect
# with connect("mahsulotlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS MAHSULOTLAR (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         nomi TEXT NOT NULL,
#         narxi INTEGER NOT NULL,
#         soni VARCHAR(30)
#     )
#     """)
#
# with connect("mahsulotlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     INSERT INTO MAHSULOTLAR (nomi, narxi, soni)
#     VALUES
#         ('olma', 20000, '70kg'),
#         ('gilos', 10000, '40kg'),
#         ('behi', 5000, '60kg'),
#         ('olcha', 200, '80kg'),
#         ('shaftoli', 900, '100kg')
#     """)
#
# with connect("mahsulotlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     SELECT * FROM MAHSULOTLAR
#     WHERE narxi > 500
#     """)
#
# for row in cursor.fetchall():
#     print(row)
                        #fayldagi 41-guruh
# from sqlite3 import connect
#
# # 1.
# with connect("ustozlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS USTOZLAR(
#         ism TEXT,
#         yosh INTEGER,
#         fan TEXT
#     )
#     """)
#
# # 2.
# with connect("ustozlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     INSERT INTO USTOZLAR (ism, yosh, fan)
#     VALUES
#         ('Dilshod', 35, 'matematika'),
#         ('Gulbahor', 29, 'kimyo'),
#         ('Anvar', 41, 'fizika'),
#         ('Malika', 22, 'ingliz tili'),
#         ('Javohir', 19, 'informatika'),
#         ('Saodat', 28, 'fizika')
#     """)
#     connection.commit()
#
# # 3.
# print("3) Yosh bo‘yicha tartiblangan ustozlar:")
# with connect("ustozlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM USTOZLAR ORDER BY yosh")
#     for row in cursor.fetchall():
#         print(row)
#
# # 4.
# print("\n4) Kimyo yoki fizika ustozlari:")
# with connect("ustozlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     SELECT * FROM USTOZLAR
#     WHERE fan='kimyo' OR fan='fizika'
#     """)
#     for row in cursor.fetchall():
#         print(row)
#
# # 5.
# print("\n5) Yoshi 20 dan katta ustozlar:")
# with connect("ustozlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     SELECT * FROM USTOZLAR
#     WHERE yosh > 20
#     """)
#     for row in cursor.fetchall():
#         print(row)
# from sqlite3 import connect
#
# # 6.
# with connect("maqolalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS MAQOLA(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         matn TEXT,
#         sarlavha TEXT,
#         sana TEXT
#     )
#     """)
# with connect("maqolalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     INSERT INTO MAQOLA (matn, sarlavha, sana)
#     VALUES
#         ('Bahorda dasturlashni o‘rganish foydali, chunki bahor yangi boshlanish faslidir.',
#          'Bahor faslida dasturlash asoslari', '2025-03-10'),
#
#         ('Yoz faslida Python bilan kichik loyihalar qilish talabaning amaliy tajribasini oshiradi.',
#          'Yozgi Python marafoni', '2025-07-01'),
#
#         ('Kuz faslida kitob o‘qish va algoritmlar bo‘yicha bilimni mustahkamlash mumkin.',
#          'Kuzgi ilhom va algoritmlar', '2024-10-15'),
#
#         ('Qish faslida onlayn kurslar orqali web dasturlashni chuqur o‘rganish mumkin.',
#          'Qish faslida web dasturlash', '2024-12-20'),
#
#         ('Web dasturlash asoslari: frontend va backend tushunchalarini oddiy misollar bilan tushuntiramiz.',
#          'Frontend va backendni tushunish', '2025-01-05'),
#
#         ('Ma’lumotlar bazasi bilan ishlashda SQL tili asosiy vositalardan biridir.',
#          'SQL bilan ishlash bo‘yicha qo‘llanma', '2023-11-11'),
#
#         ('Python dasturlashga kirish kursida o‘zgaruvchilar, sikllar va funksiyalar o‘rganiladi.',
#          'Python dasturlashga kirish', '2025-02-01'),
#
#         ('Algoritmlar va optimizatsiya mavzusi murakkab bo‘lsa-da, juda qiziqarli hisoblanadi.',
#          'Algoritmlar va optimizatsiya', '2025-05-10')
#     """)
#     connection.commit()
#
# # 7.
# print("7) Sarlavhasida 'dasturlash' so‘zi bor maqolalar:")
# with connect("maqolalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     SELECT * FROM MAQOLA
#     WHERE sarlavha LIKE '%dasturlash%'
#     """)
#     for row in cursor.fetchall():
#         print(row)
#
# # 8.
# print("\n8) id < 5 bo‘lgan maqolalar (sana bo‘yicha tartiblangan):")
# with connect("maqolalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     SELECT * FROM MAQOLA
#     WHERE id < 5
#     ORDER BY sana
#     """)
#     for row in cursor.fetchall():
#         print(row)
#
# # 9.
# print("\n9) Matnida fasl nomi bor maqolalar:")
# with connect("maqolalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     SELECT * FROM MAQOLA
#     WHERE matn LIKE '%bahor%'
#        OR matn LIKE '%yoz%'
#        OR matn LIKE '%kuz%'
#        OR matn LIKE '%qish%'
#     """)
#     for row in cursor.fetchall():
#         print(row)
#
# # 10.
# print("\n10) Eng so‘nggi 3 ta maqola (sana bo‘yicha):")
# with connect("maqolalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     SELECT * FROM MAQOLA
#     ORDER BY sana DESC
#     LIMIT 3
#     """)
#     for row in cursor.fetchall():
#         print(row)
#
# # 11.
# print('\n11) Sarlavhasida "ton" yoki "iya" qatnashgan maqolalar:')
# with connect("maqolalar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     SELECT * FROM MAQOLA
#     WHERE sarlavha LIKE '%ton%'
#        OR sarlavha LIKE '%iya%'
#     """)
#     for row in cursor.fetchall():
#         print(row)
   # 41-guruh vazifalari
# from sqlite3 import connect
# with connect("kursdoshlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(
#         '''
#         CREATE TABLE IF NOT EXISTS kursdoshlar (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#         ism VARCHAR(15) NOT NULL,
#         yosh INTEGER NOT NULL,
#         kurs INTEGER)
#         '''
#     )
# with connect("kursdoshlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     INSERT INTO kursdoshlar (ism, yosh, kurs)
#     VALUES
#     ("Fotima", 19, 2),
#     ("Durdona",22, 3),
#     ("Guli", 20, 1)
#     """)

    #UPDATE
# with connect("kursdoshlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     UPDATE kursdoshlar
#     SET yosh = yosh + 1
#     WHERE ism='Durdona' AND 'Guli'
#     """)
    #delete
# with connect("kursdoshlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     delete from kursdoshlar
#     WHERE ID=2
#     """)
#     connection.commit()
#     print(f"{cursor.rowcount} tasi o'zgartirildi")
    #ALTER TABLE
# with connect("kursdoshlar.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#     ALTER TABLE kursdoshlar
#     ADD COLUMN manzil TEXT
#     """)
#     cursor.execute("""
#     ALTER TABLE kursdoshlar
#     RENAME COLUMN manzil to yashash_joy
#     """)
#     connection.commit()
#     print("Jadval o'zgartirildii")
# with conn
