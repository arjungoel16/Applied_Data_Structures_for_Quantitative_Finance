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

from typing import NamedTuple, Optional


class Dividend(NamedTuple):
    date: str
    ticker: str
    amount: float


class Node:
    __slots__ = ("data", "next")  # Save memory
    def __init__(self, data: Dividend):
        self.data: Dividend = data
        self.next: Optional[Node] = None


class DividendSchedule:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def add(self, dividend: Dividend) -> None:
        new_node = Node(dividend)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node  # append in O(1)
        self.tail = new_node

    def print_schedule(self) -> None:
        cur = self.head
        while cur:
            d = cur.data
            print(f"{d.date} - {d.ticker}: ${d.amount:.2f}")
            cur = cur.next


def main():
    schedule = DividendSchedule()
    schedule.add(Dividend("2025-08-01", "AAPL", 0.24))
    schedule.add(Dividend("2025-08-10", "MSFT", 0.28))
    schedule.add(Dividend("2025-08-15", "NVDA", 0.32))
    schedule.print_schedule()


if __name__ == "__main__":
    main()
