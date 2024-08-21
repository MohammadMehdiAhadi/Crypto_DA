import requests
import warnings
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime as dt
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3
warnings.simplefilter('ignore', InsecureRequestWarning)

# Initialize lists to store time and price data
times = []
prices = []

def get_btc_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url, verify=False)  # Disable SSL verification
    data = response.json()

    # Check if the response contains the expected data
    if 'bitcoin' in data and 'usd' in data['bitcoin']:
        return data['bitcoin']['usd']
    else:
        print("Error: Unexpected API response format")
        return None

# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot_date(times, prices, '-')

def update(frame):
    global times, prices  # Declare the lists as global variables

    # Get the current time and BTC price
    current_time = dt.datetime.now()
    current_price = get_btc_price()

    if current_price is not None:
        # Append the new data to the lists
        times.append(current_time)
        prices.append(current_price)

        # Limit the lists to the last 20 items
        times = times[-20:]
        prices = prices[-20:]

        # Update the line data
        line.set_data(times, prices)
        ax.relim()
        ax.autoscale_view()

    return line,

# Create an animation
ani = FuncAnimation(fig, update, interval=1000)

# Display the plot
plt.show()
