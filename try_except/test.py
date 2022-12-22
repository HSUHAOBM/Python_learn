# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# 參考
# https://www.runoob.com/python/python-exceptions.html
# https://www.w3schools.com/python/python_try_except.asp

try:
  print(x)
except Exception as e:
    print(e)
else:
    pass
finally:
    print('end')

