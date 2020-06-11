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



