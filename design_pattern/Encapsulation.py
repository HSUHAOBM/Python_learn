# -*- coding: UTF-8 -*-# -*- coding: UTF-8 -*-
# 封裝(Encapsulation) 不可改
class Product():
    @property
    def price(self):
        return 100
Product().price
Product().price = 150
# error AttributeError: can't set attribute