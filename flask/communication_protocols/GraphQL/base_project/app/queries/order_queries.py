import graphene
from ..models import OrderType, orders


class OrderQuery(graphene.ObjectType):
    order = graphene.Field(OrderType, id=graphene.Int(required=True))
    all_orders = graphene.List(OrderType)

    def resolve_order(self, info, id):
        order_data = orders.get(id)
        if order_data:
            return OrderType(product=order_data['product'], quantity=order_data['quantity'], price=order_data['price'])
        return None

    def resolve_all_orders(self, info):
        return [OrderType(product=order['product'], quantity=order['quantity'], price=order['price']) for id, order in orders.items()]
