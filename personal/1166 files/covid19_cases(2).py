# Import CSV for Data Analysis
import pandas as pd
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Graph Import
df = pd.read_csv("covid19_global.csv")
x = df["t"]
y = df["C"]

# Curve Fit
def exp_fit(x, a, c, d):
    return a * np.exp(-c * x) + d


# Plot Unfitted Data
plt.scatter(x, y, label="Cases")
# plt.show()

# Initial parameter
# initialGuess = [1.0, 1.0]

# Curve fitting
popt, pcov = curve_fit(exp_fit, x, y, [100, 400, 0.001, 0])
print(popt)

decel_param = 1 - (1 / 0.10439849)
print(decel_param)

# x Values for fitted function
xFit = x

# Graph fitted function
plt.plot(
    xFit, exp_fit(xFit, *popt), "r", label="fit params: r=%5.3f, m=%5.3f" % tuple(popt)
)

plt.xlabel("Time (in Days)")
plt.ylabel("Number of Cases")
plt.legend()
plt.show()
