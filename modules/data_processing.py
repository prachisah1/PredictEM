import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df


def preprocess(df):
    X = df.drop("triage_category", axis=1)
    y = df["triage_category"]
    return X, y