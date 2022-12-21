# -*- coding:UTF-8 -*-


# row  =  int ( input ( '請輸入行數: ' ))
# for  i  in  range ( row ):
#     for  _  in  range ( row  -  i  -  1 ):
#         print ( ' ' , end = '' )
#         print(_)

#     for  _  in  range ( 2  *  i  +  1 ):
#         print ( '*' , end = '' )
#     print ()

# for i in range(row):
#     # print(i)
#     for _ in range(i+1):   #3  3  2 1
#         print("*",end=" ")
#     print ()

# # 正上
# for i in range(row+1):
#     print('*'*i,end=" ")
#     print('')

# # 正下
# for i in range(row+1):
#     print('*'*(row-i),end=" ")
#     print('')



# # 正下
# for i in range(row+1):
#     for j in range(row-i):
#         print('*',end="")
#     print('')

# # 反上
# for i in range(row+1):
#     for j in range(row):
#         if j < row :
#             print(' ',end="")
#         else:
#             print('*',end="")
#     print('')


# for i in range(row+1):
#     for j in range(row):
#         if  row < j+i+1 :
#             print(' ',end="")
#         else:
#             print('*',end="")
#     print('')


    # j=0
    # j=1
    # 5  0 1 2 3 4



def triangle(row):
    # 正上
    for i in range(row+1):
        print('*'*i,end=" ")
        print('')

    # 正下
    for i in range(row+1):
        print('*'*(row-i),end=" ")
        print('')

    for i in range(row+1):
        for _ in range(row-i):
            print(' ' ,end="")
        for _ in range(i):
            print('*' ,end="")
        print('')

    for i in range(row+1):
        for _ in range(i):
            print(' ' ,end="")
        for _ in range(row-i):
            print('*' ,end="")
        print('')

    # 菱形
    for i in range(row+1):
        print(' ' * (row-i) + '*' * (2*i-1) ,end=" ")
        print('')

    for i in range(row+1):
        print(' ' * (i) + '*' * (2*(row-i)-1) ,end=" ")
        print('')

    for i in range(row):
        print(' ' * (row-i) ,end="")
        for _ in range(2*i-1):
            if _ ==0 or _==i*2-2:
                print('*',end="")
            else:
                print(' ',end="")
        print('')
    for i in range(row):
        print(' ' * (i) ,end="")
        for _ in range((2*(row-i)-1)):
            if _ ==0 or _==2*(row-i) -2:
                print('*',end="")
            else:
                print(' ',end="")
        print('')

triangle(5)
