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

def linear_scan(trades):
    for trade in trades:
        _ = trade + " processed"

def nested_scan(trades):
    for t1 in trades:
        for t2 in trades:
            _ = t1 + t2

def benchmark(func, trades):
    start = time.time()
    func(trades)
    end = time.time()
    print(f"{func.__name__}: {end - start:.6f} seconds")

trades = [f"Trade{i}" for i in range(1000)]
benchmark(linear_scan, trades)
benchmark(nested_scan, trades[:100])  # smaller for quadratic test
