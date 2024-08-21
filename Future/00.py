import pandas as pd
import numpy as np

print("Reading Data...")
df = pd.read_csv("BTC_Price_15m.csv", index_col="Datetime")
print("Done")
print("Creating New Csv File For ML...")

df["std_7"] = df["Close"].rolling(window=7).std()
df["std_14"] = df["Close"].rolling(window=14).std()
df["std_21"] = df["Close"].rolling(window=21).std()
df["std_30"] = df["Close"].rolling(window=30).std()
df["mean_7"] = df["Close"].rolling(window=7).mean()
df["mean_14"] = df["Close"].rolling(window=14).mean()
df["mean_21"] = df["Close"].rolling(window=21).mean()
df["mean_30"] = df["Close"].rolling(window=30).mean()
df["stdp7"] = df["mean_7"] + df["std_7"]
df["stdp7"] = df["mean_7"] - df["std_7"]
df["stdp14"] = df["mean_14"] + df["std_14"]
df["stdn14"] = df["mean_14"] - df["std_14"]
df["stdp21"] = df["mean_21"] + df["std_21"]
df["stdn21"] = df["mean_21"] - df["std_21"]
df["stdp30"] = df["mean_30"] + df["std_30"]
df["stdn30"] = df["mean_30"] - df["std_30"]
df["min"] = df["Close"].rolling(window=30).min()
df["max"] = df["Close"].rolling(window=30).max()


print("Done")
print(df.corr())

if not df.to_csv("BTC_ML.csv"):
    print("New Csv File Is Ready ")
else:
    print("Somthing Went Wrong ; Try Again")