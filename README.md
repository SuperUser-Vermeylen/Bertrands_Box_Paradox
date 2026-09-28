# Bertrand's Box Paradox

This project simulates Bertrand's Box Paradox and visualizes how the observed probabilities change as more trials are generated.

## What the project does

The simulation models the classic paradox where one of three boxes contains two gold coins, one contains two silver coins, and one contains one gold and one silver coin. Each trial randomly selects a box and then a coin from that box. The project tracks the distribution of box choices, first-coin colors, and the conditional probability that the second coin matches the first coin.

## Repository layout

- `bertrand_box_paradox/simulation.py` — core simulation logic
- `bertrand_box_paradox/probability.py` — probability data generation
- `bertrand_box_paradox/plotting.py` — plotting and visualization
- `Coin_Problem.py` — compatibility wrapper for the original simulation name
- `Create_DataFrame.py` — compatibility wrapper for probability generation
- `Plot.py` — compatibility wrapper for the original plotting script
- `tests/` — validation for the simulation and probability logic

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python Plot.py
```

## Run the tests

```bash
pytest -q
```

## Notes

This refactor preserves the original behavior while making the code easier to read, validate, and extend. The goal is to keep the scientific logic intact while improving maintainability.
