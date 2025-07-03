"""
Unit test for dividend_schedule_linkedlist.py
"""
import unittest
from src.dividend_schedule_linkedlist import DividendSchedule

class TestDividendSchedule(unittest.TestCase):
    def test_add_and_print_schedule(self):
        ds = DividendSchedule()
        ds.add_dividend("2025-01-01", "AAPL", 0.25)
        ds.add_dividend("2025-01-15", "MSFT", 0.30)
        self.assertIsNotNone(ds.head)
        self.assertEqual(ds.head.ticker, "AAPL")
        self.assertEqual(ds.head.next.ticker, "MSFT")

if __name__ == '__main__':
    unittest.main()
