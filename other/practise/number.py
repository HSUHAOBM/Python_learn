# -*- coding:UTF-8 -*-
#練習：輸入兩個正整數，計算它們的最大公約數和最小公倍數。
a = int(input('a='))
b = int(input('b='))
#IF a> b 交換 a和b的值
# if a > b:
#     a , b = b , a
#從兩個數較小的數開始遞減循環
for factor in range(min(a,b), 0, -1):
    print(factor)
    if a % factor == 0 and b % factor == 0:
        print("%d和%d的最大公約數是%d" %(a,b,factor))
        print("%d和%d的最小公倍數是%d" %(a,b,a * b // factor))
        break