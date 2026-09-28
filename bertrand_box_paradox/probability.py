from __future__ import annotations

from collections import Counter

import pandas as pd

from .simulation import bertrand_box_paradox


def probability_dataframe(iterations: int) -> pd.DataFrame:
    """Build the probability table used by the plotting dashboard."""
    if iterations < 1:
        raise ValueError("iterations must be at least 1")

    rows: list[dict[str, float]] = []

    for k in range(1, iterations + 1):
        first_coins, second_coins, box1_count, box2_count, box3_count = bertrand_box_paradox(k)
        first_coin_counts = Counter(first_coins)
        second_coin_counts = Counter(second_coins)

        total_first_gold = first_coin_counts.get("Gold", 0)
        total_first_silver = first_coin_counts.get("Silver", 0)

        same_gold = sum(1 for first, second in zip(first_coins, second_coins) if first == "Gold" and second == "Gold")
        same_silver = sum(1 for first, second in zip(first_coins, second_coins) if first == "Silver" and second == "Silver")

        if total_first_gold == 0:
            gold_probability = 0.0
        else:
            gold_probability = same_gold / total_first_gold

        if total_first_silver == 0:
            silver_probability = 0.0
        else:
            silver_probability = same_silver / total_first_silver

        rows.append(
            {
                "Box 1": box1_count / k,
                "Box 2": box2_count / k,
                "Box 3": box3_count / k,
                "First Coin: Gold": first_coin_counts.get("Gold", 0) / k,
                "First Coin: Silver": first_coin_counts.get("Silver", 0) / k,
                "Second Coin: Gold": second_coin_counts.get("Gold", 0) / k,
                "Second Coin: Silver": second_coin_counts.get("Silver", 0) / k,
                "Gold": gold_probability,
                "Silver": silver_probability,
            }
        )

    return pd.DataFrame(rows)
