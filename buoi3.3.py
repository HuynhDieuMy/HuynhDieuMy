# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:00:48 2024

@author: L13
"""

distance = float(input("Nhập độ dài đến trường (m):"))
if distance<300:
    print ("Đường đến trường quá gần. Thôi! Đi bộ")
elif distance > 1200:
    print("Đường đến trường quá xa. Thôi! Đi xe máy")
elif distance >= 300 and distance <= 700:
    print("Đường đến trường không xa. Thôi! Đi xe đạp")
else:
    print("Không xác định")