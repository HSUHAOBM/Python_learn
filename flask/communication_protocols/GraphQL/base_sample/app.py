from flask import Flask
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)

# 模擬數據
users = {
    123: {"name": "Bob", "gender": "male", "order": 456}
}

orders = {
    456: {"product": "abc", "quantity": 2, "price": "100.00"}
}


# 定義訂單類型
class OrderType(graphene.ObjectType):
    product = graphene.String()  # 訂單的產品名稱
    quantity = graphene.Int()     # 訂單的數量
    price = graphene.String()      # 訂單的價格


# 定義用戶類型
class UserType(graphene.ObjectType):
    id = graphene.Int()           # 用戶的 ID
    name = graphene.String()      # 用戶的名稱
    gender = graphene.String()    # 用戶的性別
    order = graphene.Field(OrderType)  # 用戶的訂單，類型為 OrderType


# 定義查詢類型
class Query(graphene.ObjectType):
    user = graphene.Field(
        UserType, id=graphene.Int(required=True))  # 查詢特定用戶的字段
    all_users = graphene.List(UserType)  # 查詢所有用戶的字段

    # 解決查詢的邏輯：查詢特定用戶
    def resolve_user(self, info, id):
        user_data = users.get(id)  # 根據 ID 獲取用戶數據
        if user_data:
            order_data = orders.get(user_data['order'])  # 根據用戶的訂單 ID 獲取訂單數據
            return UserType(id=id, name=user_data['name'], gender=user_data['gender'], order=OrderType(**order_data))
        return None  # 如果用戶不存在，返回 None

    # 解決查詢的邏輯：查詢所有用戶
    def resolve_all_users(self, info):
        return [UserType(id=id, name=user['name'], gender=user['gender'],
                         order=OrderType(**orders.get(user['order'], {})))
                for id, user in users.items()]


# 定義新增用戶的 Mutation
class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)  # 用戶名稱，必填
        gender = graphene.String(required=True)  # 用戶性別，必填

    user = graphene.Field(UserType)  # 返回的用戶類型

    # 定義新增用戶的邏輯
    def mutate(self, info, name, gender):
        new_id = max(users.keys()) + 1  # 簡單的 ID 生成邏輯，獲取當前最大 ID 並加 1
        users[new_id] = {"name": name,
                         "gender": gender, "order": None}  # 新增用戶到數據中
        # 返回新增的用戶
        return CreateUser(user=UserType(id=new_id, name=name, gender=gender))


# 定義修改用戶的 Mutation
class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)  # 用戶 ID，必填
        name = graphene.String()           # 用戶名稱，可選
        gender = graphene.String()         # 用戶性別，可選

    user = graphene.Field(UserType)  # 返回的用戶類型

    # 定義修改用戶的邏輯
    def mutate(self, info, id, name=None, gender=None):
        user_data = users.get(id)  # 根據 ID 獲取用戶數據
        if user_data:
            if name:  # 如果提供了名稱，則更新
                user_data['name'] = name
            if gender:  # 如果提供了性別，則更新
                user_data['gender'] = gender
            return UpdateUser(user=UserType(id=id, **user_data))  # 返回更新後的用戶
        return None  # 如果用戶不存在，返回 None


# 定義新增用戶刪除的 Mutation
class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)  # 用戶 ID，必填

    success = graphene.Boolean()  # 返回刪除是否成功

    def mutate(self, info, id):
        if id in users:
            del users[id]  # 從 users 字典中刪除該用戶
            return DeleteUser(success=True)  # 刪除成功，返回 success=True
        return DeleteUser(success=False)  # 刪除失敗，返回 success=False


# 定義 Mutation 類型
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()  # 定義新增用戶的 Mutation
    update_user = UpdateUser.Field()   # 定義修改用戶的 Mutation
    delete_user = DeleteUser.Field()  # 定義刪除用戶的 Mutation


# 定義 GraphQL 的 schema
schema = graphene.Schema(query=Query, mutation=Mutation)
# 這裡的 `schema` 是 GraphQL 的結構，包含了查詢和變更的定義。
# - `query=Query` 表示我們定義的查詢類型，這裡可以查詢用戶信息。
# - `mutation=Mutation` 表示我們定義的變更類型，這裡可以新增和修改用戶信息。


# 設置 GraphQL 的路由
app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)  # 啟動 Flask 應用
