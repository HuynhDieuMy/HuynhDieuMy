# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:50:59 2024

@author: Huỳnh Diệu Mỹ
"""
import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
if a==0 and b==0 and c==0:
    print("Phương trình vô số nghiệm")
elif a==0 and b!=0 and c!=0:
    print("Phương trình có 1 nghiệm:x= ",-c/b)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có nghiệm kép: x1=x2= ",-b/2*a)
    elif delta > 0:   
        x1= ((-b - math.sqrt (delta))/(2*a))
        x2= ((-b + math.sqrt (delta))/(2*a))
        print("Phương trình có 2 nghiệm phân biệt: ", x1)
        print("Phương trình có 2 nghiệm phân biệt: ", x2)