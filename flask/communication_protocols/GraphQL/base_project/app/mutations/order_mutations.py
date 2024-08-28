import graphene
from ..models import OrderType, orders

class CreateOrder(graphene.Mutation):
    class Arguments:
        product = graphene.String(required=True)
        quantity = graphene.Int(required=True)
        price = graphene.String(required=True)

    order = graphene.Field(OrderType)

    def mutate(self, info, product, quantity, price):
        new_id = max(orders.keys()) + 1
        orders[new_id] = {"product": product, "quantity": quantity, "price": price}
        return CreateOrder(order=OrderType(product=product, quantity=quantity, price=price))

class UpdateOrder(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        product = graphene.String()
        quantity = graphene.Int()
        price = graphene.String()

    order = graphene.Field(OrderType)

    def mutate(self, info, id, product=None, quantity=None, price=None):
        order_data = orders.get(id)
        if order_data:
            if product:
                order_data['product'] = product
            if quantity:
                order_data['quantity'] = quantity
            if price:
                order_data['price'] = price
            return UpdateOrder(order=OrderType(product=product, quantity=quantity, price=price))
        return None

class DeleteOrder(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        if id in orders:
            del orders[id]
            return DeleteOrder(success=True)
        return DeleteOrder(success=False)

class OrderMutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()
