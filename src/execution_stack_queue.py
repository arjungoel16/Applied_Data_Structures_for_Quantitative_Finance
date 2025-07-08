"""
execution_stack_queue.py

Models the behavior of an order management system that queues trade instructions and supports order reversals
using stacks.

Real-Life Use Case:
Used in trading infrastructure where real-time trades are queued for execution. In case of market anomalies or
errors, traders can quickly revert or cancel a few of the most recent trades.

Core Concepts:
- Queue (FIFO) to process trade instructions
- Stack (LIFO) to support undo functionality
"""

"""
Execution Queue and Order Backtracking using Stack and Queue

Simulates the management of a trade execution system with queues and undo stack.
"""

from collections import deque

from typing import NamedTuple


class Trade(NamedTuple):
    action: str
    symbol: str


def execute_trade_queue(trade_queue: deque[Trade]) -> list[Trade]:
    undo_stack = []
    while trade_queue:
        trade = trade_queue.popleft()
        print(f"Executing: {trade.action} {trade.symbol}", flush=True)
        undo_stack.append(trade)
    return undo_stack


def revert_last_n(stack: list[Trade], n: int) -> None:
    print("Undoing:")
    for _ in range(n):
        if stack:
            last = stack.pop()
            print(f"Reverting: {last.action} {last.symbol}", flush=True)


def main():
    trade_queue = deque([
        Trade("Buy", "AAPL"),
        Trade("Sell", "TSLA"),
        Trade("Buy", "NVDA"),
    ])
    undo_stack = execute_trade_queue(trade_queue)
    revert_last_n(undo_stack, 2)


if __name__ == "__main__":
    main()
