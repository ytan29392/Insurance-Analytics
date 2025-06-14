import pandas as pd


def load_data(path: str, sep: str = "|") -> pd.DataFrame:
    """
    Load the insurance dataset using a custom delimiter (pipe).
    Automatically skips malformed rows.
    """
    return pd.read_csv(path, sep=sep, on_bad_lines='skip', engine='python')


def summarize_numerical(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Return summary statistics for numeric columns."""
    return df[cols].describe()


def check_missing(df: pd.DataFrame) -> pd.Series:
    """Return count of missing values per column."""
    return df.isnull().sum()
