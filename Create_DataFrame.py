from bertrand_box_paradox.probability import probability_dataframe

__all__ = ["probability_dataframe"]


if __name__ == "__main__":
    df = probability_dataframe(10)
    print(df.head())
