"""
portfolio_allocation.py

This script simulates a portfolio allocation process in a quantitative investment system.
It uses Python lists to manage a dynamic set of financial instruments and their associated weights.

Real-Life Use Case:
Used by quantitative portfolio managers to initialize and rebalance portfolios. As assets are added or removed,
the system automatically recalculates normalized weights to ensure total capital is allocated accurately.

Core Concepts:
- Lists for managing assets and weights
- Appending and inserting elements dynamically
- Rebalancing via normalization
"""

"""
Portfolio Allocation using Lists and Arrays

This script demonstrates how to initialize, update, and rebalance a multi-asset portfolio
using Python lists and basic arithmetic.
"""

# Define portfolio assets and their weights
assets = ["AAPL", "MSFT", "GOOGL", "TSLA"]
weights = [0.25, 0.25, 0.25, 0.25]  # Equal-weighted portfolio

# Add a new stock
assets.append("NVDA")
weights.append(0.2)

# Normalize weights
total_weight = sum(weights)
weights = [round(w / total_weight, 2) for w in weights]

# Output rebalanced portfolio
for asset, weight in zip(assets, weights):
    print(f"{asset}: {weight*100}%")
