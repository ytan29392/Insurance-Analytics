import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(df, target, categorical_cols, numeric_cols, dropna=True):
    df = df.copy()
    if dropna:
        df = df[categorical_cols + numeric_cols + [target]].dropna()

    df_encoded = pd.get_dummies(df[categorical_cols], drop_first=True)
    df_final = pd.concat([df_encoded, df[numeric_cols], df[target]], axis=1)
    X = df_final.drop(columns=[target])
    y = df_final[target]
    return train_test_split(X, y, test_size=0.2, random_state=42)
