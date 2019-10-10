import uuid
from itertools import groupby
from functools import reduce

from order import Order
from order_type import OrderType
from summary_info import SummaryInfo


class SilverBarsLiveOrdersBoard:

    def __init__(self) -> None:
        self.orders = []

    def register(self, order: Order) -> str:
        """Registers a valid order in the live orders board, returning the id assigned to the new order"""
        if not order.is_valid():
            raise ValueError('Cannot register an invalid order!')
        order.id = uuid.uuid1()
        self.orders.append(order)
        return order.id

    def summary(self) -> SummaryInfo:
        """Shows a summary list for all the existing orders in the board"""
        summaries = []

        orders_by_type = dict()
        for order_type, items in groupby(self.orders, key=lambda order: order.type):
            items_for_type = list(items)
            if order_type == OrderType.SELL:
                items_for_type.sort(key=lambda order: order.price)
            else:
                items_for_type.sort(key=lambda order: order.price, reverse=True)
            orders_by_type[order_type] = items_for_type

        final_orders = dict()
        for order_type in orders_by_type.keys():
            items = orders_by_type[order_type]
            final_orders[order_type] = dict()
            for price, items_by_price in groupby(list(items), key=lambda order: order.price):
                order = reduce(lambda left, right: Order(right.user_id, left.quantity + right.quantity, right.price, right.type, right.id), list(items_by_price))
                final_orders[order_type][price] = [order]

        for orders_by_price in final_orders.values():
            for orders in orders_by_price.values():
                for order in orders:
                    summaries.append(order.summary())
        return SummaryInfo(*summaries)

    def cancel(self, order_id: str) -> None:
        """Cancels an existing order in the board. Raises exception if order does not exist."""
        for order in self.orders:
            if order.id == order_id:
                self.orders.remove(order)
                return
        raise ValueError(f'Order with id {order_id} does not exist!')
