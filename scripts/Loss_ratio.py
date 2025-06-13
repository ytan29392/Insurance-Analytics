import pandas as pd


def calculate_loss_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a LossRatio column to the DataFrame.
    Avoids division by zero.
    """
    df = df.copy()
    df['LossRatio'] = df.apply(
        lambda row: row['TotalClaims'] /
        row['TotalPremium'] if row['TotalPremium'] != 0 else 0,
        axis=1)
    return df


def loss_ratio_by_group(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """
    Returns average loss ratio by group (e.g., Province, Gender).
    """
    return df.groupby(group_col)[
        'LossRatio'].mean().sort_values(ascending=False)
