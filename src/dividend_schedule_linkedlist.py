"""
dividend_schedule_linkedlist.py

Represents dividend payment events using a custom singly linked list to preserve chronological order.

Real-Life Use Case:
Used in back-office systems and financial data pipelines to store, track, and report dividend schedules per asset
without relying on built-in data structures. This mirrors data feed models used in accounting and clearing firms.

Core Concepts:
- Custom Linked List for event storage
- Node objects representing dividend metadata
"""

"""
Dividend Payment Schedule using a Linked List

Each dividend event is recorded as a node in a linked list to simulate chronological order.
"""

class Node:
    def __init__(self, date, ticker, amount):
        self.date = date
        self.ticker = ticker
        self.amount = amount
        self.next = None

class DividendSchedule:
    def __init__(self):
        self.head = None

    def add_dividend(self, date, ticker, amount):
        new_node = Node(date, ticker, amount)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def print_schedule(self):
        cur = self.head
        while cur:
            print(f"{cur.date} - {cur.ticker}: ${cur.amount}")
            cur = cur.next

ds = DividendSchedule()
ds.add_dividend("2025-08-01", "AAPL", 0.24)
ds.add_dividend("2025-08-10", "MSFT", 0.28)
ds.add_dividend("2025-08-15", "NVDA", 0.32)
ds.print_schedule()
