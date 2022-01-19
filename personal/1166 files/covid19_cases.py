# Import packages
import time
import pandas as pd
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# CSV Import
data = pd.read_csv("covid19_global.csv")
x = data["Time Elapsed (Days)"]
y = data["Total Cases"]

# Curve Fit
def exp_fit(x, r, m):
    return r * np.exp(m * x)


# Plot Unfitted Data
plt.scatter(x, y, label="Cases")
# plt.show()

# Initial parameter
# initialGuess = [1.0,1.0]

# Curve fitting
popt, pcov = curve_fit(exp_fit, x, y)
print(popt)

decel_param = 1 - (1 / (1.065 ** -13))
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
