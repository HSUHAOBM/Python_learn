# import numpy as np
# print(np.round(3.153, 2))
# print(np.round(3.154, 2))
# print(np.round(4.155, 2))
# print(np.round(4.156, 2))

import numpy as np
# # def round_v2(num, decimal):
# #     num = np.round(num, decimal)
# #     num = float(num)
# #     return num


# # print(round(3.15, 1))
# # print(round_v2(3.15, 1))

# print(round(4.15, 1))
# print(round(4.25, 1))
# print(round(4.35, 1))

print(np.round(20.175, 2))
print(np.round(20.185, 2))


def example_1_except():
    try:
        1 / 0
    except Exception:
        print("1")
        return "3"
    finally:
        print("2")

print(example_1_except())



class A:
    def show(self):
        self.a=1
        print('123')

class B(A):
    def show(self):
        super().show()
        print('bb')