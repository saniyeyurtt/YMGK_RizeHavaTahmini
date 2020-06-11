# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:56:00 2020

@author: saniyy
"""

import pandas as pd

import matplotlib.pyplot as plt

df1 = pd.read_excel("Koronalı günler 2020.xlsx")

df2 = pd.read_excel("Koronasız günler 2018.xlsx")


print(df1.columns)
print(df1.info())

print(df1.describe())

dfkoronalırize = df1.drop(["Tarih"],axis=1) #Tarih bilgisi df1'den çıkarıldı.
dfkoronasızrize = df2.drop(["Tarih"],axis=1) #Tarih bilgisi df2'den çıkarıldı.

dfkoronalırize.plot(grid=True)
plt.show()

dfkoronasızrize.plot(grid=True)
plt.show()

plt.plot(df1["PM10 ( µg/m³ )"],df2["PM10 ( µg/m³ )"])
plt.plot(df1["SO2 ( µg/m³ )"],df2["SO2 ( µg/m³ )"])
plt.plot(df1["NO2 ( µg/m³ )"],df2["NO2 ( µg/m³ )"])
plt.plot(df1["NOX ( µg/m³ )"],df2["NOX ( µg/m³ )"])
plt.plot(df1["NO ( µg/m³ )"],df2["NO ( µg/m³ )"])
plt.plot(df1["O3 ( µg/m³ )"],df2["O3 ( µg/m³ )"])

plt.xlabel("Koronalı Günler")
plt.ylabel("Koronasız Günler")


def grafik(a,b):
    x=df1[a]
    y=df2[b]
        

    fig, ax = plt.subplots()


    line1, = ax.plot(x, y, label= a)
    line1.set_dashes([2, 2, 10, 2])  

    line2, = ax.plot(x, y - 0.2, dashes=[6, 2], label= b)

    ax.legend()
    plt.show()
    plt.xlabel("Koronalı Günler")
    plt.ylabel("Koronasız Günler")

grafik("PM10 ( µg/m³ )","PM10 ( µg/m³ )")
grafik("SO2 ( µg/m³ )","SO2 ( µg/m³ )")
grafik("NO2 ( µg/m³ )","NO2 ( µg/m³ )")
grafik("NOX ( µg/m³ )","NOX ( µg/m³ )")
grafik("NO ( µg/m³ )","NO ( µg/m³ )")
grafik("O3 ( µg/m³ )","O3 ( µg/m³ )")


#%%

 
# Grafik için gerekli kütüphaneler. Axes3D 3 boyutlu bir grafik için.
from matplotlib import pyplot as  plt
from mpl_toolkits.mplot3d import Axes3D
 
class knn():

    def __init__(self, dataset, k, nfrom, nto):
        self.b, self.g, self.r, self.class_attr = [], [], [], []
        self.inp = [264,124,183]
        self.k = k
 
    # Veri setimizi nfrom satırından nto satırına kadar okuyoruz.
    # Ayrıca veri setindeki her sutunu bir listeye atıyoruz. (r,g,b,class_attr)
        with open(dataset, "r") as f:
            for i in f.readlines()[nfrom:nto]:
                self.r.append(int(i.split()[0]))
                self.g.append(int(i.split()[1]))
                self.b.append(int(i.split()[2]))
                self.class_attr.append(i.split()[3])
 

    # öklid = 2, manhattan=1
    def distance(self, dist=1):
        self.dist = []
        # for döngüsündeki karışık gibi gelen üs alma, mutlak değer gibi işlemler
        # minkowski formulunun karşılığından ibarettir.
        for i in range(len(self.class_attr)):
            self.dist.append((pow((pow((
            abs(int(self.b[i]) - int(self.inp[0])) +
            abs(int(self.g[i]) - int(self.inp[1])) +
            abs(int(self.r[i]) - int(self.inp[2]))), dist)), 1/dist), i))
 
        return self.dist
 

    def findClass(self):
        self.class_values = []
        self.result = ""
 
        for i in sorted(self.dist)[:self.k]:
            self.class_values.append(self.class_attr[i[1]])
 
        self.first = self.class_values.count("1")
        self.secnd = self.class_values.count("2")
 
        print("Birinci Sınıf:", self.first)
        print("İkinci Sınıf:", self.secnd)
 
        if self.first > self.secnd:
            self.result = "1. Sınıf(Kırmızı)"
        else:
            self.result = "2. Sınıf(Yeşil)"
 
        print("SONUÇ: "+self.result)
 
#GORSELLEŞTİRME

    def grafik(self):
        fig = plt.figure()
        ax  = fig.add_subplot(111, projection='3d')
 
        for bi, gj, rk, class_attr in zip(self.b, self.g, self.r, self.class_attr):
         if class_attr == "1":
          ax.scatter(bi,gj,rk, c='r', marker='.')
         else:
          ax.scatter(bi,gj,rk, c='g', marker='.')
 
        ax.scatter(int(self.inp[0]), int(self.inp[1]), int(self.inp[2]), c='b')
        ax.set_xlabel('X Ekseni')
        ax.set_ylabel('Y Ekseni')
        ax.set_zlabel('Z Ekseni')
 
        fig.text(0, 0, "Kırmızı(1)[PM10] : "+str(self.first)+
                " -- Yeşil(2)[SO2] : "+str(self.secnd)+
                " -- {{SONUÇ : "+self.result+"}}")
 
        plt.legend()
        plt.show()
 
# Sınıfımızdan nesne türetip gerekli metodlarımızı çağırıyoruz. En yakın 17 komşuya bakıyoruz. Ola ki eşit çıkma durumu olduğundan k değerinin tek seçilmesinde yarar vardır. Ve sonuç.
ins = knn("ten_dataset.txt", 17, 50300, 51000)
ins.distance(1)
ins.findClass()
ins.grafik()
 
 


