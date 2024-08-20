import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print("Reading Data...")
df = pd.read_csv("BTC_Price_15m.csv", index_col="Datetime")
df["Date"] = df.index
print("Done")
print("Plotting...")

mean_btc = np.mean(df["Close"])
std_btc = np.std(df["Close"])
std_p = mean_btc + std_btc
std_n = mean_btc - std_btc
std2_p = mean_btc + (std_btc * 2)
std2_n = mean_btc - (std_btc * 2)

plt.plot(df.index, df["Close"], "r--", label="close")
plt.axhline(mean_btc, color='blue', linestyle='-', label="Mean")
plt.axhline(std_p, color='green', linestyle='--', label="Positive Std")
plt.axhline(std2_p, color='green', linestyle='--', label="Negative Std")
plt.axhline(std_n, color='orange', linestyle='--', label="Negative Std")
plt.axhline(std2_n, color='orange', linestyle='--', label="Negative Std")

plt.xticks(ticks=df["Date"].iloc[::200], rotation=45)
plt.legend()
print("Done")
plt.savefig("BTC_Behavior.jpg")
plt.show()
