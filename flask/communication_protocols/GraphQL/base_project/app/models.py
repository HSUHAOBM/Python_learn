# 模擬數據
import graphene


users = {
    123: {"name": "Bob", "gender": "male", "order": 456}
}

orders = {
    456: {"product": "abc", "quantity": 2, "price": "100.00"}
}


# 定義訂單類型
class OrderType(graphene.ObjectType):
    product = graphene.String()
    quantity = graphene.Int()
    price = graphene.String()


# 定義用戶類型
class UserType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    gender = graphene.String()
    order = graphene.Field(OrderType)
