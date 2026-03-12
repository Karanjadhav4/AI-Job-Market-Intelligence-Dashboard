import pandas as pd

def clean_jobs(df):

    df = df.drop_duplicates()

    df["title"] = df["title"].str.strip()
    df["company"] = df["company"].str.strip()

    df = df.dropna()

    return df