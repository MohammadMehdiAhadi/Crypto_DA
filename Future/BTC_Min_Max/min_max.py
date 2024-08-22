try:

    import pandas as pd
    import matplotlib.pyplot as plt
    import scipy.signal as sc

    print("Reading Data...")
    df = pd.read_csv("C:/Crypto_DA/Future/Creating_Data/BTC_Price_15m.csv")
    df.set_index(df["Datetime"], inplace=True)
    print("Done")
    print("Plotting...")

    peaks, no = sc.find_peaks(df["Close"])
    troughs, _ = sc.find_peaks(-df["Close"])


    plt.plot(df["Datetime"], df["Close"], "blue", label="Close price")
    plt.plot(df["Datetime"].iloc[peaks+1], df["Close"].iloc[peaks+1],"r--", label="Peaks")
    plt.xticks(ticks=df["Datetime"].iloc[::500], rotation=45)
    plt.plot(df["Datetime"].iloc[troughs+1], df["Close"].iloc[troughs+1], "g--", label="Troughs")
    plt.legend()
    plt.grid()
    print("Done")
    plt.savefig("BTC_Min_Max.jpg")
    plt.show()

except Exception as e:
    print(e)
