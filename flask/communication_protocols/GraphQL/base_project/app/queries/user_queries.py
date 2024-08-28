import graphene
from ..models import UserType, users, orders, OrderType


class UserQuery(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int(required=True))
    all_users = graphene.List(UserType)

    def resolve_user(self, info, id):
        user_data = users.get(id)
        if user_data:
            order_data = orders.get(user_data['order'])
            return UserType(id=id, name=user_data['name'], gender=user_data['gender'], order=OrderType(**order_data))
        return None

    def resolve_all_users(self, info):
        return [UserType(id=id, name=user['name'], gender=user['gender']) for id, user in users.items()]
