# coding=utf-8
import unittest
from decimal import Decimal

from order import Order
from order_type import OrderType
from silver_bars_live_orders_board import SilverBarsLiveOrdersBoard
from summary_info import SummaryInfo


class SilverBarsLiveOrdersBoardTest(unittest.TestCase):

    def setUp(self) -> None:
        self.live_orders_board = SilverBarsLiveOrdersBoard()

    def test_register_an_order(self):
        self.live_orders_board.register(Order('my-user-id', 10, Decimal(12.5), OrderType.BUY))
        summary = self.live_orders_board.summary()
        self.assertEqual(SummaryInfo('BUY: 10 kg for £12.50'), summary)

    def test_register_invalid_order(self):
        self.assertRaises(ValueError,
                          lambda: self.live_orders_board.register(Order('user-id', 0, Decimal(12.5), OrderType.BUY)))

    def test_board_is_empty_after_cancelling_existing_order(self):
        order_id = self.live_orders_board.register(Order('my-user-id', 10, Decimal(12.5), OrderType.BUY))
        self.live_orders_board.cancel(order_id)
        self.assertEqual(SummaryInfo(), self.live_orders_board.summary())

    def test_register_two_identical_orders_and_remove_only_one_of_them(self):
        self.live_orders_board.register(Order('my-user-id', 10, Decimal(12.5), OrderType.BUY))
        order_id = self.live_orders_board.register(Order('my-user-id', 10, Decimal(12.5), OrderType.BUY))
        self.assertEqual(SummaryInfo(
            'BUY: 10 kg for £12.50',
            'BUY: 10 kg for £12.50'
        ),
            self.live_orders_board.summary()
        )
        self.live_orders_board.cancel(order_id)
        self.assertEqual(SummaryInfo('BUY: 10 kg for £12.50'), self.live_orders_board.summary())

    def test_raise_exception_when_deleting_non_existing_order(self):
        self.assertRaises(ValueError, lambda: self.live_orders_board.cancel('non-existing-order-id'))

    def test_register_multiple_orders(self):
        self.live_orders_board.register(Order('my-user-id', 10, Decimal(12.5), OrderType.BUY))
        self.live_orders_board.register(Order('my-user-id', 20, Decimal(27.2), OrderType.SELL))
        self.assertEqual(SummaryInfo(
            'BUY: 10 kg for £12.50',
            'SELL: 20 kg for £27.20'
        ),
            self.live_orders_board.summary()
        )

    def test_sort_sell_orders_by_price_ascending(self):
        self.live_orders_board.register(Order('my-user-id', 20, Decimal(27.2), OrderType.SELL))
        self.live_orders_board.register(Order('my-user-id', 20, Decimal(27.9), OrderType.SELL))
        self.assertEqual(SummaryInfo(
            'SELL: 20 kg for £27.20',
            'SELL: 20 kg for £27.90'
        ),
            self.live_orders_board.summary()
        )

    def test_sort_buy_orders_by_price_descending(self):
        self.live_orders_board.register(Order('my-user-id', 20, Decimal(27.2), OrderType.BUY))
        self.live_orders_board.register(Order('my-user-id', 20, Decimal(27.9), OrderType.BUY))
        self.assertEqual(SummaryInfo(
            'BUY: 20 kg for £27.90',
            'BUY: 20 kg for £27.20'
        ),
            self.live_orders_board.summary()
        )

    def test_multiple_orders_of_different_types_in_the_right_order(self):
        self.live_orders_board.register(Order('my-user-id', 20, Decimal(27.2), OrderType.BUY))
        self.live_orders_board.register(Order('my-user-id', 20, Decimal(27.9), OrderType.BUY))
        self.live_orders_board.register(Order('my-user-id', 20, Decimal(27.2), OrderType.SELL))
        self.live_orders_board.register(Order('my-user-id', 20, Decimal(27.9), OrderType.SELL))
        self.assertEqual(SummaryInfo(
            'BUY: 20 kg for £27.90',
            'BUY: 20 kg for £27.20',
            'SELL: 20 kg for £27.20',
            'SELL: 20 kg for £27.90'
        ),
            self.live_orders_board.summary()
        )
