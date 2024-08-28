import graphene
from ..models import UserType, users


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        gender = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, name, gender):
        new_id = max(users.keys()) + 1
        users[new_id] = {"name": name, "gender": gender, "order": None}
        return CreateUser(user=UserType(id=new_id, name=name, gender=gender))


class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        gender = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, id, name=None, gender=None):
        user_data = users.get(id)
        if user_data:
            if name:
                user_data['name'] = name
            if gender:
                user_data['gender'] = gender
            return UpdateUser(user=UserType(id=id, name=name, gender=gender))
        return None


class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        if id in users:
            del users[id]
            return DeleteUser(success=True)
        return DeleteUser(success=False)


class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
