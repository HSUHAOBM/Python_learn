# -*- coding:UTF-8 -*-


n=30

# 因數
def test(n):
    num=[]
    for i in range(1,n+1):
        if n % i == 0:
            num.append(i)
    print(num)

# 質數
def test1(n):
    num=[]
    for j in range(1,n+1):
        a=0
        for i in range(1,n+1):
            if j % i == 0:
                a+=1
                if a >2:
                    break
        if a==2:
            num.append(j)
    print(num)

def test2(n):
    num=[]
    for i in range(2,n+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            num.append(i)
    print(num)

test(n)
test1(n)
test2(n)



# 質數 一行解
# result = [x for x in range(2, 101) if all(x % i for i in range(2, x))]

# all() : [1,2,3] > True , [1,2,3,0] > False , all True -> True
# 質數 x % i for i in range(2, x) -> x % i = not 0
# x = 10
# print([ x % i for i in range(2, x)])
# print(all( [0, 1, 2, 0, 4, 3, 2, 1]))
# print( [ x for x in range(2, 101) if all( ['1'] ) ] )