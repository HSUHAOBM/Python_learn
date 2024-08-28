import graphene
from .queries.user_queries import UserQuery
from .queries.order_queries import OrderQuery
from .mutations.user_mutations import UserMutation
from .mutations.order_mutations import OrderMutation


class Query(UserQuery, OrderQuery, graphene.ObjectType):
    pass


class Mutation(UserMutation, OrderMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
