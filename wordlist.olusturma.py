#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install crunch")
os.system("clear")
os.system("figlet Wordlist Olusturma")
print("-"*50)
print("Trojan Oluşturma Aracına Hoşgeldiniz   instagram = zumrudu_anka_team ")
print("Bu Araç Treangle Tarafından Oluşturulmuştur")
print("-"*50)
minimumkarakter = input("Minimum Karakter Sayısını Giriniz :")
maksimumkarakter = input("Maksimum Karakter Sayısını Giriniz :")
karakter = input("İstediğiniz Karakterleri Girin :")
kayityeri = input("Nereye Kaydetsin :")

os.system("crunch" + minimumkarakter + " " + maksimumkarakter + " " + karakter + " -o " + kayityeri)

print("İşlem Başarı İle Tamamlandı Treangle Başarılar Diler")