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

# Queue for pending trades
trade_queue = deque(["Buy AAPL", "Sell TSLA", "Buy NVDA"])
# Stack for undoing actions
undo_stack = []

# Process trades
while trade_queue:
    trade = trade_queue.popleft()
    print("Executing:", trade)
    undo_stack.append(trade)

# Undo last two actions
print("Undoing:")
for _ in range(2):
    if undo_stack:
        print("Reverting:", undo_stack.pop())
