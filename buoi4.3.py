# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:20:09 2024

@author: Huỳnh Diệu Mỹ 
"""
import random
luachon = ["Kéo", "Búa", "Bao"]
Ngchoi = input("Ra cái gì: ")
print("Bạn chọn", Ngchoi)
print("Máy chọn", random.choice(luachon))
if Ngchoi == luachon:
    print("Hòa")
elif Ngchoi == "Kéo" and luachon == "Bao" or \
    Ngchoi == "Búa" and luachon == "Kéo" or \
        Ngchoi =="Bao" and luachon == "Búa":
    print ("Bạn thắng gòyy")
else:
    print ("Bạn thua gòyy")