import pandas as pd

DATA_URL = "https://github.com/mmonj/CSCI-381-Applied-Data-Science/raw/refs/heads/main/quiz1/data/diamonds.csv"


def main() -> None:
    df_diamonds = pd.read_csv(DATA_URL, index_col=0)

    print(df_diamonds.head())


if __name__ == "__main__":
    main()
