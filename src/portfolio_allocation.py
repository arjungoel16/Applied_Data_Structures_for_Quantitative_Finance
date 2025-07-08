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

from decimal import Decimal, getcontext
from typing import NamedTuple, List

getcontext().prec = 6  # Control floating point precision

class Asset(NamedTuple):
    symbol: str
    weight: Decimal

def normalize_weights(assets: List[Asset]) -> List[Asset]:
    total = sum(asset.weight for asset in assets)
    if total == 0:
        raise ValueError("Total weight cannot be zero.")
    return [Asset(asset.symbol, (asset.weight / total).quantize(Decimal("0.01"))) for asset in assets]

def main():
    portfolio = [
        Asset("AAPL", Decimal("0.25")),
        Asset("MSFT", Decimal("0.25")),
        Asset("GOOGL", Decimal("0.25")),
        Asset("TSLA", Decimal("0.25"))
    ]

    # Insert NVDA dynamically
    portfolio.append(Asset("NVDA", Decimal("0.20")))

    # Normalize
    portfolio = normalize_weights(portfolio)

    for asset in portfolio:
        print(f"{asset.symbol}: {asset.weight * 100:.0f}%")

if __name__ == "__main__":
    main()
