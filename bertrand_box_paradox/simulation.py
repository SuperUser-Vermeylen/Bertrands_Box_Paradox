from __future__ import annotations

import random

BOX_NAMES = ("Box1", "Box2", "Box3")
BOX_CONTENTS = {
    "Box1": ("Gold", "Gold"),
    "Box2": ("Gold", "Silver"),
    "Box3": ("Silver", "Silver"),
}


def simulate_trial() -> dict[str, str]:
    """Return a single random trial result for the Bertrand box paradox."""
    box_name = random.choice(BOX_NAMES)
    coins = BOX_CONTENTS[box_name]
    first_index = random.choice((0, 1))
    first_coin = coins[first_index]
    second_coin = coins[1 - first_index]
    return {"box": box_name, "first_coin": first_coin, "second_coin": second_coin}


def simulate_trials(iterations: int) -> dict[str, object]:
    """Run a set of trials and return aggregated results."""
    if iterations < 1:
        raise ValueError("iterations must be at least 1")

    box_counts = {box_name: 0 for box_name in BOX_NAMES}
    first_coins: list[str] = []
    second_coins: list[str] = []

    for _ in range(iterations):
        trial = simulate_trial()
        box_name = trial["box"]
        box_counts[box_name] += 1
        first_coins.append(trial["first_coin"])
        second_coins.append(trial["second_coin"])

    return {
        "first_coins": first_coins,
        "second_coins": second_coins,
        "box_counts": box_counts,
    }


def bertrand_box_paradox(iterations: int) -> list[object]:
    """Compatibility wrapper preserving the original return structure."""
    data = simulate_trials(iterations)
    box_counts = data["box_counts"]
    return [
        data["first_coins"],
        data["second_coins"],
        box_counts["Box1"],
        box_counts["Box2"],
        box_counts["Box3"],
    ]


Bertrand_Box_Paradox = bertrand_box_paradox
