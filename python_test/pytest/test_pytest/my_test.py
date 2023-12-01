# pytest
# python3 -m pytest my_test.py -v -s
# pytest my_test.py

#  記憶體使用
#   pip install memory_profiler
#   mprof run my_test.py
#

from memory_profiler import profile
a=0

def sum(a,b):
    return a+b

@profile
def add(a):
    for i in range(100):
        a+=i
    print(a)
    return a

def test01_A_answer():
    result_4 = sum(5,6)
    assert result_4 == 11
test01_A_answer()

if __name__ == "__main__":
    test01_A_answer()
    add(a)
