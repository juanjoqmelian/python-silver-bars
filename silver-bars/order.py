from decimal import Decimal, ROUND_HALF_EVEN

from order_type import OrderType


class Order:
    def __init__(self, user_id: str, quantity: int, price: Decimal, order_type: OrderType, order_id='') -> None:
        self.id = order_id
        self.user_id = user_id
        self.quantity = quantity
        self.price = price.quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN) if price else price
        self.type = order_type

    def is_valid(self) -> bool:
        return bool(self.user_id) \
               and bool(self.quantity) and self.quantity > 0 \
               and bool(self.price) and self.price > 0 \
               and self.type is not None

    def summary(self) -> str:
        return f'{self.type.name}: {self.quantity} kg for £{self.price}'

    def __str__(self) -> str:
        return f'id: {self.id}, user_id: {self.user_id}, quantity: {self.quantity}, price: {self.price}, type: {self.type}'

    def __repr__(self) -> str:
        return f'id: {self.id}, user_id: {self.user_id}, quantity: {self.quantity}, price: {self.price}, type: {self.type}'
