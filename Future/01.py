import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as sc
import numpy as np
print("Reading Data...")
df = pd.read_csv("BTC_Price_15m.csv", index_col="Datetime")
df["Date"] = df.index
print("Done")
print("Plotting...")

plt.plot(df["Date"], df["Close"], "blue", label="Close price")
plt.xticks(ticks=df["Date"].iloc[::10], rotation=45)
plt.grid()
peaks, no = sc.find_peaks(df["Close"])
plt.plot(df["Date"].iloc[peaks+1], df["Close"].iloc[peaks+1],"r--", label="Peaks")

troughs, _ = sc.find_peaks(-df["Close"])

plt.plot(df["Date"].iloc[troughs+1], df["Close"].iloc[troughs+1], "g--", label="Troughs")
plt.legend()
plt.savefig("BTC_DA.jpg")
plt.show()

