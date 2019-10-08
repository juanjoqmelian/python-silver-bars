import uuid

from order import Order
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
        for order in self.orders:
            summaries.append(order.summary())
        return SummaryInfo(*summaries)

    def cancel(self, order_id: str) -> None:
        """Cancels an existing order in the board. Raises exception if order does not exist."""
        for order in self.orders:
            if order.id == order_id:
                self.orders.remove(order)
                return
        raise ValueError(f'Order with id {order_id} does not exist!')


