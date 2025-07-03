"""
risk_registry.py

Simulates a risk monitoring registry system within a financial institution. Each financial instrument is mapped to its
associated risk rating using dictionaries. Sets are used to efficiently track and detect instruments flagged
for compliance review.

Real-Life Use Case:
Used in compliance departments and risk management dashboards to quickly identify which active instruments are
under investigation or need review due to elevated risk levels.

Core Concepts:
- Dictionaries for storing instrument metadata
- Sets for efficient membership and intersection operations
"""

"""
Risk Assessment and Registry using Dictionaries and Sets

Simulates a registry of financial instruments with flagged risk categories.
Uses sets for quick lookup and dictionaries for structured metadata.
"""

# Risk registry: instrument ID to metadata
risk_registry = {
    "BND001": {"name": "10Y Treasury", "risk": "low"},
    "EQ002": {"name": "Tesla Equity", "risk": "high"},
    "OPT003": {"name": "S&P Options", "risk": "medium"},
}

# Flagged IDs for compliance review
flagged_ids = {"EQ002", "OPT003", "ETF005"}

# Identify instruments needing review
intersection = flagged_ids.intersection(set(risk_registry.keys()))
print("Instruments under compliance review:")
for rid in intersection:
    print(rid, "→", risk_registry[rid])
