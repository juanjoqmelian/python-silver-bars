# coding=utf-8
import unittest
from decimal import Decimal

from order import Order
from order_type import OrderType
from summary_info import SummaryInfo
from silver_bars_live_orders_board import SilverBarsLiveOrdersBoard


class SilverBarsLiveOrdersBoardTest(unittest.TestCase):

    def setUp(self) -> None:
        self.live_orders_board = SilverBarsLiveOrdersBoard()

    def test_register_an_order(self):
        self.live_orders_board.register(Order('my-user-id', 10, Decimal(12.5), OrderType.BUY))
        summary = self.live_orders_board.summary()
        self.assertEqual(SummaryInfo('BUY: 10 kg for £12.50'), summary)

    def test_register_invalid_order(self):
        self.assertRaises(ValueError, lambda:self.live_orders_board.register(Order('user-id', 0, Decimal(12.5), OrderType.BUY)))

    def test_board_is_empty_after_cancelling_existing_order(self):
        order_id = self.live_orders_board.register(Order('my-user-id', 10, Decimal(12.5), OrderType.BUY))
        self.live_orders_board.cancel(order_id)
        self.assertEqual(SummaryInfo(), self.live_orders_board.summary())
