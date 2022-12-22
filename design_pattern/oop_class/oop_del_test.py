import time
import sys

# del , python 直譯器回收

# 引用數量
# sys.getrefcount()

# del xxx 不會主動呼叫__del__方法，
# 只有引用計數 == 0，__del__()才會被執行

class Test:
    def __del__(self):
        print('刪除')

t = Test()
print('t 的引用數：', sys.getrefcount(t)) # 2  (1 + 傳入)

v = t
print('t 的引用數：', sys.getrefcount(t)) # 3

print('記憶體位置', id(v))
print('記憶體位置', id(t))

del v

print('t 的引用數：', sys.getrefcount(t)) # 2



del t
# t 觸發 del
# print('t 的引用數：', sys.getrefcount(t)) # name 't' is not defined


u = Test()
print('u 的引用數：', sys.getrefcount(u))


print("程式3秒鐘後繼續")
time.sleep(3)

# u 觸發 del
