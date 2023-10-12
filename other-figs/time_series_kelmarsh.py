import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

time_series = np.load("wind-variability/data/Pickles/NWTC/days.npy", allow_pickle=True)
plt.plot(time_series)
print(len(time_series))
#plt.show()

"""
days = np.load("wind-variability/data/power-gen/Fichtelberg/days.npy", allow_pickle=True)
days = pd.DataFrame(days, columns = ['date'])
days["date"] = pd.to_datetime(days['date'])
days.set_index(["date"])
print(days['date'].dt.year)
data = days[(days["date"].dt.month.isin((int(3), int(4), int(5))))]
print(data)
"""