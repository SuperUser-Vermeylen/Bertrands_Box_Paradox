from bertrand_box_paradox.simulation import bertrand_box_paradox, simulate_trial


def test_simulate_trial_returns_valid_box_contents() -> None:
    trial = simulate_trial()
    assert trial["box"] in {"Box1", "Box2", "Box3"}
    assert trial["first_coin"] in {"Gold", "Silver"}
    assert trial["second_coin"] in {"Gold", "Silver"}
    valid_box_contents = {
        "Box1": {"Gold"},
        "Box2": {"Gold", "Silver"},
        "Box3": {"Silver"},
    }
    assert {trial["first_coin"], trial["second_coin"]} <= valid_box_contents[trial["box"]]


def test_bertrand_box_paradox_shape() -> None:
    result = bertrand_box_paradox(10)
    assert len(result) == 5
    assert len(result[0]) == 10
    assert len(result[1]) == 10
    assert sum(result[2:]) == 10


def test_probability_dataframe_has_expected_columns() -> None:
    df = __import__("bertrand_box_paradox.probability", fromlist=["probability_dataframe"]).probability_dataframe(5)
    expected_columns = {
        "Box 1",
        "Box 2",
        "Box 3",
        "First Coin: Gold",
        "First Coin: Silver",
        "Second Coin: Gold",
        "Second Coin: Silver",
        "Gold",
        "Silver",
    }
    assert set(df.columns) == expected_columns
    assert len(df) == 5
