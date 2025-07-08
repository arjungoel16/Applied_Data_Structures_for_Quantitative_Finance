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

from typing import TypedDict, Dict, FrozenSet


class Instrument(TypedDict):
    name: str
    risk: str


def get_flagged_instruments(
    registry: Dict[str, Instrument],
    flagged_ids: FrozenSet[str]
) -> Dict[str, Instrument]:
    return {iid: registry[iid] for iid in flagged_ids & registry.keys()}


def main():
    # Static registry
    registry: Dict[str, Instrument] = {
        "BND001": {"name": "10Y Treasury", "risk": "low"},
        "EQ002": {"name": "Tesla Equity", "risk": "high"},
        "OPT003": {"name": "S&P Options", "risk": "medium"},
    }

    # Incoming flagged list
    flagged: FrozenSet[str] = frozenset({"EQ002", "OPT003", "ETF005"})

    matches = get_flagged_instruments(registry, flagged)

    print("Instruments under compliance review:")
    for iid in sorted(matches):
        record = matches[iid]
        print(f"{iid} → {record['name']} ({record['risk']})")


if __name__ == "__main__":
    main()
