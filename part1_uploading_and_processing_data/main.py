from typing import Any

import pandas as pd


def main() -> None:
    car_sample_url = "https://raw.githubusercontent.com/mmonj/CSCI-381-Applied-Data-Science/refs/heads/main/part1_uploading_and_processing_data/data/car-sample35.txt"
    headers = [
        "price",
        "maintenance",
        "doors",
        "passengers",
        "luggage",
        "safety",
        "classification",
    ]

    df_cars = get_df(car_sample_url, headers)

    extract_attributes(df_cars)
    print()

    find_indices_price_med(df_cars)
    print()

    find_passengers_price_med(df_cars)
    print()

    find_indices_high_price_not_low_maint(df_cars)
    print()

    find_indices_price_med_lc(df_cars)
    print()

    find_passengers_price_med_lc(df_cars)
    print()

    find_indices_high_price_not_low_maint_lc(df_cars)
    print()

    extract_from_nlist()


def get_df(url: str, headers: list[str]) -> pd.DataFrame:
    """Task 1"""
    return pd.read_csv(url, names=headers)


def extract_attributes(df_cars: pd.DataFrame) -> None:
    """Task 2"""
    price_list = df_cars["price"].tolist()
    maintenance_list = df_cars["maintenance"].tolist()
    doors_list = df_cars["doors"].tolist()
    passengers_list = df_cars["passengers"].tolist()
    luggage_list = df_cars["luggage"].tolist()
    safety_list = df_cars["safety"].tolist()
    classification_list = df_cars["classification"].tolist()

    print("Price list: ", price_list)
    print("maintenance list:", maintenance_list)
    print("Doors list:", doors_list)
    print("Passengers list:", passengers_list)
    print("Luggage list:", luggage_list)
    print("Safety list:", safety_list)
    print("Classification list:", classification_list)


def find_indices_price_med(df_cars: pd.DataFrame) -> None:
    """Task 3"""
    price_list = df_cars["price"].tolist()
    indices = []
    for idx, price in enumerate(price_list):
        if price == "med":
            indices.append(idx)
    print("Indices with price == 'med':", indices)


def find_passengers_price_med(df_cars: pd.DataFrame) -> None:
    """Task 4"""
    price_list = df_cars["price"].tolist()
    passengers_list = df_cars["passengers"].tolist()
    result = []
    for idx, price in enumerate(price_list):
        if price == "med":
            result.append(passengers_list[idx])
    print("Passengers for cars with price is med:", result)


def find_indices_high_price_not_low_maint(df_cars: pd.DataFrame) -> None:
    """Task 5"""
    price_list = df_cars["price"].tolist()
    maintenance_list = df_cars["maintenance"].tolist()
    indices = []
    for idx, (price, maint) in enumerate(zip(price_list, maintenance_list, strict=True)):
        if price == "high" and maint != "low":
            indices.append(idx)
    print("Indices with price is high and maintenance is not low:", indices)


def find_indices_price_med_lc(df_cars: pd.DataFrame) -> None:
    """Task 6"""
    price_list = df_cars["price"].tolist()
    indices = [idx for idx, price in enumerate(price_list) if price == "med"]
    print("Indices with price is med:", indices)


def find_passengers_price_med_lc(df_cars: pd.DataFrame) -> None:
    """Task 7"""
    price_list = df_cars["price"].tolist()
    passengers_list = df_cars["passengers"].tolist()
    result = [passengers_list[idx] for idx, price in enumerate(price_list) if price == "med"]
    print("Passengers for cars with price is med:", result)


def find_indices_high_price_not_low_maint_lc(df_cars: pd.DataFrame) -> None:
    """Task 8"""
    price_list = df_cars["price"].tolist()
    maintenance_list = df_cars["maintenance"].tolist()
    indices = [
        idx
        for idx, (price, maint) in enumerate(zip(price_list, maintenance_list, strict=True))
        if price == "high" and maint != "low"
    ]
    print("Indices with price is high and maintenance is not low:", indices)


def extract_from_nlist() -> None:
    """Task 9"""
    nlist: list[list[Any]] = [[1, 2, 3], ["A", "B", "C"], [4, 5], ["D", "E"]]

    result = [f for sublist in nlist for f in sublist]
    print("Individual elements:", result)


if __name__ == "__main__":
    main()
