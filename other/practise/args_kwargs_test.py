# def plus(*nums):
#     res = 0
#     print(nums) # //type Tuple
#     for i in nums:
#         res += i
#     return res

# a=plus(1,2,3)
# print(a)

# /------------------------/

# def plus(*args):
#     res = 0
#     print(args) # //type Tuple
#     for i in args:
#         res += i
#     return res

# a=plus(1,2,3)
# print(a)

# /------------------------/

# def fun(**_settings):
#     print(_settings)

# fun(name='Sky', attack=100, hp=500)

# /------------------------/

# def fun(**settings):
#     settings.setdefault('name', 'Hello')
#     settings.setdefault('attack', 50)
#     settings.setdefault('defense', 0)
#     settings.setdefault('hp', 150)
#     print(settings)
# fun(name='Sky', attack=100, hp=500)


# /------------------------/

# def fun(*args, **kwargs):
#     print(args, kwargs, sep='\n')

# fun(1,2,3,4,5,6,name='Sky', attack=100, hp=500)



def fun(a, b=20, *, kw1, kw2=40):
    print(a, b, kw1, kw2)

# fun(1, 2, kw1=3, kw2=4)  # 1 2 3 4
fun(1,2,kw1=3)
# fun(10, kw1=30)  # 10 20 30 40
# 在傳入引數時，在 * 後面的（kw1 和 kw2）一定要以關鍵字引數（指名）傳入