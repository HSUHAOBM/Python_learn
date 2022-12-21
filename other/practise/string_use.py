# -*- coding: utf-8 -*-

# 隨機產數字
from random import choice
from string import digits

def a():
    result = "".join(choice(digits) for i in range(10))
    return result
result = a()
print(result)

# 0123456789 取
print(choice(digits))
# -------------------------------------------------------------

# import string library function
import string

# Storing the value in variable result
result = string.digits #0123456789
result = choice(digits)
# # Printing the value
print(result)

# -------------------------------------------------------------
# Importing random to generate
# random string sequence
import random

# Importing string library function
import string

def rand_pass(size):

    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice( string.ascii_uppercase +
                                            string.ascii_lowercase +
                                            string.digits)
                                            for n in range(size)])

    return generate_pass

# Driver Code
password = rand_pass(10)
print(password)