import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt

df = yf.download("BTC-USD")

y = df["Close"].iloc[:20].dropna().values.reshape(-1, 1)
print(y)
X = np.arange(len(y)).reshape(-1, 1)
X_bias = np.c_[np.ones(X.shape[0]), X]

print(X.shape)
print(y.shape)
print(X_bias.shape)

learning_rate = 0.01

num_samples, num_features = X_bias.shape
theta = np.zeros((num_features, 1))

rmse = []

from matplotlib.animation import FuncAnimation


def update(frame):
    global theta, learning_rate, X, y, X_bias, rmse
    prediction = np.dot(X_bias, theta)  # y = theta * x  + x_bias
    errors = prediction - y
    gradient = np.dot(X_bias.T, errors) / num_samples
    theta -= learning_rate * gradient
    x_data = X
    y_data = X_bias.dot(theta)
    rmse_metric = np.sqrt(np.mean(np.power(errors, 2)))
    print(rmse_metric)
    rmse.append(rmse_metric)
    line.set_data(x_data, y_data)
    return line,


fig, ax = plt.subplots()
ax.plot(X, y)
x_data, y_data = [], []
line, = ax.plot(x_data, y_data)

# ax.set_xlim(X.min(), X.max())
# ax.set_ylim(y.min(),y.max())

ax.set_xlim(0, X.max())
ax.set_ylim(0, y.max())

ani = FuncAnimation(fig, update, frames=1, interval=30, blit=True)
plt.show()

plt.plot(rmse)
plt.show()
