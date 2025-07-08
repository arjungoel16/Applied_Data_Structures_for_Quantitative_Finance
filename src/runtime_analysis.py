"""
runtime_analysis.py

Benchmarks the performance of common data processing functions (linear scan, nested loops) to demonstrate
real-world Big-O runtime implications.

Real-Life Use Case:
Used by quant developers and researchers to profile large-scale data pipelines and algorithm performance.
Performance diagnostics help optimize latency-sensitive components like signal generation and trade simulation.

Core Concepts:
- Time complexity comparison
- Real-time benchmarking and performance logging
"""

"""
Runtime Analysis of Trade Evaluation

Compares time complexity of different operations in a quant pipeline.
"""

import time
from typing import Callable, List


class Timer:
    def __init__(self, label: str):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *_):
        elapsed = time.perf_counter() - self.start
        print(f"{self.label}: {elapsed:.6f} seconds")


def constant_access(trades: List[str]) -> None:
    _ = trades[0]


def linear_scan(trades: List[str]) -> None:
    for i in range(len(trades)):
        _ = trades[i]


def quadratic_scan(trades: List[str]) -> None:
    for i in range(len(trades)):
        for j in range(len(trades)):
            _ = trades[i] + trades[j]


def binary_search(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def main():
    trades = [f"T{i}" for i in range(1000)]
    prices = list(range(1000))

    with Timer("O(1) Access"):
        constant_access(trades)

    with Timer("O(n) Linear Scan"):
        linear_scan(trades)

    with Timer("O(n^2) Quadratic Scan"):
        quadratic_scan(trades[:100])  # limit for test feasibility

    with Timer("O(log n) Binary Search"):
        idx = binary_search(prices, 750)
        print(f"Found target at index: {idx}")


if __name__ == "__main__":
    main()
