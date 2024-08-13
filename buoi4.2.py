# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:58:24 2024

@author: Huỳnh Diệu Mỹ
"""

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