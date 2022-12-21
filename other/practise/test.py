# -*- coding: utf-8 -*-

def count():                # 建立一個 count 函式
    a = []                    # 函式內有區域變數 a 是串列
    def avg(val):             # 建立內置函式 avg ( 閉包 )
        a.append(val)           # 將參數數值加入變數 a
        print(a)                # 印出 a
        return sum(a)/len(a)    # 回傳 a 串列所有數值的平均
    return avg                # 回傳 avg

test = count()
test(10)      # 將 10 存入 a
test(11)      # 將 11 存入 a
print(test(12))      # 印出 12
