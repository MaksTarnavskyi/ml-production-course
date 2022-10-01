import os
import time
from functools import wraps
from pathlib import Path
from typing import Union

import numpy as np
import pandas as pd


def generate_dataset(
    n_rows: int, n_columns: int, fill_value: Union[str, int]
) -> pd.DataFrame:
    """Generate syntetic dataset

    Args:
        n_rows (int): desired number of rows
        n_columns (int): desired number of columns
        fill_value (Union[str, int]): value for fill in dataset

    Returns:
        (pd.DataFrame): generated syntetic dataset
    """
    column_names = ["col_" + str(col_index) for col_index in range(n_columns)]
    row_values = np.full((n_rows, n_columns), fill_value=fill_value)
    df = pd.DataFrame(data=row_values, columns=column_names)
    return df


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs) -> float:
        """Measure execution time

        Returns:
            (float): measured execution time in seconds
        """
        start_time = time.perf_counter()

        func(*args, **kwargs)

        end_time = time.perf_counter()
        total_time = end_time - start_time
        return total_time

    return timeit_wrapper


def call_function_by_name(funtion_name: str, *args, **kwargs):
    result = globals()[funtion_name](*args, **kwargs)
    return result


def get_path(folder_path: str, file_name: str, file_format: str) -> Path:
    path = Path(folder_path, f"{file_name}.{file_format}")
    return path


def measure_save_time(
    df: pd.DataFrame, folder_path: str, file_name: str, file_format: str
):
    save_path = get_path(folder_path, file_name, file_format)
    seconds = call_function_by_name(f"save_{file_format}", df, save_path)
    return seconds


def measure_load_time(folder_path: str, file_name: str, file_format: str):
    load_path = get_path(folder_path, file_name, file_format)
    seconds = call_function_by_name(f"load_{file_format}", load_path)
    return seconds


def get_file_size(file_path: Path):
    size_in_bytes = os.path.getsize(file_path)
    size_in_megabytes = size_in_bytes * (0.1**6)
    return size_in_megabytes


def measure_file_size(folder_path: str, file_name: str, file_format: str):
    file_path = get_path(folder_path, file_name, file_format)
    file_size_in_megabytes = get_file_size(file_path)
    return file_size_in_megabytes


def check_folder(folder_path: str):
    os.makedirs(folder_path, exist_ok=True)


@timeit
def save_csv(df: pd.DataFrame, path: str):
    df.to_csv(path)


@timeit
def load_csv(path: str):
    pd.read_csv(path)


@timeit
def save_json(df: pd.DataFrame, path: str):
    df.to_json(path)


@timeit
def load_json(path: str):
    pd.read_json(path)


@timeit
def save_xml(df: pd.DataFrame, path: str):
    df.to_xml(path)


@timeit
def load_xml(path: str):
    pd.read_xml(path)


@timeit
def save_excel(df: pd.DataFrame, path: str):
    df.to_excel(path)


@timeit
def load_excel(path: str):
    pd.read_excel(path)


@timeit
def save_feather(df: pd.DataFrame, path: str):
    df.to_feather(path)


@timeit
def load_feather(path: str):
    pd.read_feather(path)


@timeit
def save_parquet(df: pd.DataFrame, path: str):
    df.to_parquet(path)


@timeit
def load_parquet(path: str):
    pd.read_parquet(path)


@timeit
def save_pickle(df: pd.DataFrame, path: str):
    df.to_pickle(path)


@timeit
def load_pickle(path: str):
    pd.read_pickle(path)
