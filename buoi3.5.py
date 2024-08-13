# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:25:50 2024

@author: Huynh Dieu My
"""
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
if a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
elif a == 0 and b != 0:
    print("Phương trình vô nghiệm")
elif a != 0 and b != 0:
    x = -b/a
    print("Nghiệm của phương trình là:",x)
else:
    print("Không xác định")