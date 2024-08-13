# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:43:38 2024

@author: Huỳnh Diệu Mỹ
Bai1:
    distance = float(input("Nhập độ dài đến trường (m):"))
    if distance>1200:
        print ("Đường đến trường quá xa.")
--------------------
Bai2:
    distance = float(input("Nhập độ dài đến trường (m):"))
    if distance>1200:
        print ("Đường đến trường quá xa.")
    else:
        print("Không xác định được xa-gần.")
--------------------
Bai3:
    distance = float(input("Nhập độ dài đến trường (m):"))
    if distance<300:
        print ("Đường đến trường quá gần. Thôi! Đi bộ")
    elif distance > 1200:
        print("Đường đến trường quá xa. Thôi! Đi xe máy")
    elif distance >= 300 and distance <= 700:
        print("Đường đến trường không xa. Thôi! Đi xe đạp")
    else:
        print("Không xác định")
--------------------
Bai4:
    GPA = float(input("Thông báo xếp hạng học lực:"))
    if GPA < 3.5:
        print("Học lực Kém")
    elif GPA >= 3.5 and GPA < 5.0:
        print("Học lực Yếu")
    elif GPA >= 5.0 and GPA < 7.0:
        print("Học lực Trung bình")
    elif GPA >= 7.0 and GPA < 8.0:
        print("Học lực Khá")
    elif GPA >= 8.0 and GPA < 9.0:
        print("Học lực Giỏi")
    elif GPA >= 9.0 and GPA <= 10.0:
        print("Học lực Xuất sắc")
    else:
        print("Không xác định")
--------------------
Bai5:
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
--------------------
Bai6
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
--------------------
Bai7
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
if a+b>c and a+c>b and b+c>a:
    print("Đó là ba cạnh của 1 tam giác ")
--------------------
Bai8
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
--------------------
Bai9
distance = float(input("Nhập số km quãng đường đi được: "))
if distance <=1:
    print("Số tiền phải trả là 20000")
elif distance >1 and distance <=3:
    print("Số tiền phải trả: ", distance*13000)
elif distance >=4 and distance <=8:
    print("Số tiền phải trả: ", (distance - 3) *12000 + 39000)
elif distance >8:
    print("Số tiền phải trả: ", (distance - 8) *10000 + 39000 + 60000)
elif ((distance - 8) *10000 + 39000 + 60000) >= 100:
    print("Số tiền phải trả ", ((distance - 8) *10000 + 39000 + 60000)-((distance - 8) *10000 + 39000 + 60000)*0.08)
else:
    print("Cước xe này miễn phí cho bạn")
--------------------
Bai10
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
"""

