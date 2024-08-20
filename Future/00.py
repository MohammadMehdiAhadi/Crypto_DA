import yfinance as yf

print("Downloading Data ...")
print("Please Wait")

df = yf.download("BTC-USD", period="60d", interval="15m")

if not df.empty:
    df.to_csv("BTC_Price_15m.csv")
    print("It's Done; Enjoy!")
else:
    print("Check Your Connection please!")

