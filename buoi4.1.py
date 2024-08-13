# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:39:27 2024

@author: Huỳnh Diệu Mỹ
"""
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
if a==b==c:
    print("Tam giác đều")
elif a*a == b*b + c*c or  b*b == a*a + c*c or  c*c == a*a + b*b:
    print("Tam giác vuông")
elif a==b or  a==c or  b==c:
    print("Tam giác cân")
else:
    print("Tam giác thường")