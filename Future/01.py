import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as sc

print("Reading Data...")
df = pd.read_csv("BTC_Price_15m.csv", index_col="Datetime")
df["Date"] = df.index
print("Done")
print("Plotting...")

peaks, no = sc.find_peaks(df["Close"])
troughs, _ = sc.find_peaks(-df["Close"])


plt.plot(df["Date"], df["Close"], "blue", label="Close price")
plt.plot(df["Date"].iloc[peaks+1], df["Close"].iloc[peaks+1],"r--", label="Peaks")
plt.xticks(ticks=df["Date"].iloc[::200], rotation=45)
plt.plot(df["Date"].iloc[troughs+1], df["Close"].iloc[troughs+1], "g--", label="Troughs")
plt.legend()
plt.grid()
print("Done")
plt.savefig("BTC_Min_Max.jpg")
plt.show()


