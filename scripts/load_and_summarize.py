import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load the dataset."""
    # return pd.read_csv(path)
    return pd.read_csv(path, on_bad_lines='skip')


def summarize_numerical(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Return summary statistics for numeric columns."""
    return df[cols].describe()

def check_missing(df: pd.DataFrame) -> pd.Series:
    """Return count of missing values per column."""
    return df.isnull().sum()
