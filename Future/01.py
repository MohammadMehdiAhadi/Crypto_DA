import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as sc
import numpy as np

df = pd.read_csv("BTC_Price_15m.csv", index_col="Datetime")

df["Date"] = df.index

plt.plot(df["Date"], df["Close"], "blue", label="Close price")
plt.xticks(ticks=df["Date"].iloc[::10], rotation=45)
plt.grid()
peaks, no = sc.find_peaks(df["Close"])
plt.plot(df["Date"].iloc[peaks+3], df["Close"].iloc[peaks+3],"r--", label="Peaks")

troughs, _ = sc.find_peaks(-df["Close"])

plt.plot(df["Date"].iloc[troughs+3], df["Close"].iloc[troughs+3], "g--", label="Troughs")
plt.legend()
plt.show()

