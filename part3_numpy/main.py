import numpy as np
import pandas as pd

DATA_FILE_URL = "https://github.com/mmonj/CSCI-381-Applied-Data-Science/raw/refs/heads/main/part3_numpy/data/Module6_Data.xlsx"


def task1() -> None:
    """Task 1"""
    print("Task 1")
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

    unique_a = np.unique(a)
    unique_b = np.unique(b)

    common_unique = np.intersect1d(unique_a, unique_b)

    print(f"Arrays:\na = {a}\nb = {b}")
    print(f"Distinct common elements: {common_unique}")


def task2() -> np.ndarray:
    """Task 2"""
    print("Task 2")

    arr = np.arange(1, 16).reshape(5, 3)
    print("5x3 array:")
    print(arr)
    return arr


def task3(arr: np.ndarray) -> np.ndarray:
    """Task 3"""
    print("Task 3")

    flattened = arr.flatten()
    print(f"Flattened array: {flattened}")
    return flattened


def task4(arr: np.ndarray) -> np.ndarray:
    """Task 4"""
    print("Task 4")

    col1 = arr[:, 0]
    col2 = arr[:, 1]
    col3 = arr[:, 2]

    arr_3d = np.array([col1, col2, col3])
    print("3D array (columns as dimensions):")
    print(arr_3d)
    return arr_3d


def task5(arr_3d: np.ndarray) -> np.ndarray:
    """Task 5"""
    print("Task 5")

    arr_2d = np.column_stack((arr_3d[0], arr_3d[1], arr_3d[2]))
    print("Back to 2D array:")
    print(arr_2d)
    return arr_2d


def task6() -> None:
    """Task 6"""
    print("Task 6:")
    a = np.array([12, 5, 7, 15, 3, 1, 8])
    b = np.array([14, 6, 3, 11, 19, 12, 5])

    print(f"Original arrays:\na = {a}\nb = {b}")

    mask = ~np.isin(a, b)
    filtered_a = a[mask]

    print(f"Array a after removing elements present in b: {filtered_a}")


def task7() -> None:
    """
    NYC water consumption data.
    """
    print("Task 7:")

    nyc_data = pd.read_excel(DATA_FILE_URL)

    consumption = nyc_data["NYC Consumption(Million gallons per day)"].to_numpy()
    years = nyc_data["Year"].to_numpy()
    per_capita = nyc_data["Per Capita(Gallons per person per day)"].to_numpy()
    population = nyc_data["New York City Population"].to_numpy()

    max_consumption = np.max(consumption)
    max_year = years[np.argmax(consumption)]
    print(
        f"1. Maximum yearly NYC consumption: {max_consumption} million gallons per day (in {max_year})"
    )

    num_years = years.shape[0]
    print(f"2. Number of calendar years in the dataset: {num_years}")

    mean_per_capita = np.mean(per_capita)
    std_per_capita = np.std(per_capita)
    print(
        f"3. Per capita daily water consumption: Mean = {mean_per_capita}, Standard Deviation = {std_per_capita}"
    )

    pop_diff = np.diff(population)
    print("4. Population change from year to year:")
    for i, diff in enumerate(pop_diff):
        print(f"{years[i]} to {years[i + 1]}: {int(diff)} people")


def main() -> None:
    task1()

    arr_2d = task2()

    task3(arr_2d)

    arr_3d = task4(arr_2d)

    task5(arr_3d)

    task6()

    task7()


if __name__ == "__main__":
    main()
