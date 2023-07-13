import glob
import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import xarray as xr
from distributions import compute_instantenous_windspeeds
from windspeed_averages_wp import compute_average_windspeeds, drop_nans, load_data, set_date

matplotlib.rcParams.update({"font.size": 12})

savepath = "plots_eps/cum_dens_avrg_inst_4sites_diff.svg"
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)
fig, ax = plt.subplots(4, 2, sharex=True, sharey=True, figsize=(6, 6), layout="constrained")

# load data
average_daily = np.load("data/Pickles/Kelmarsh/average_daily.npy")
average_hourly = np.load("data/Pickles/Kelmarsh/average_hourly.npy")
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
average_monthly = np.load("data/Pickles/Kelmarsh/average_monthly.npy")
day = np.load("data/Pickles/Kelmarsh/day.npy")
six_hour = np.load("data/Pickles/Kelmarsh/six_hour.npy")
three_hour = np.load("data/Pickles/Kelmarsh/three_hour.npy")
hour = np.load("data/Pickles/Kelmarsh/hour.npy")

average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

data = [
    pd.Series(average_daily),
    pd.Series(average_six_hourly),
    pd.Series(average_three_hourly),
    pd.Series(average_hourly),
    pd.Series(average_10min),
]
labels = ["day", "6h", "3h", "hourly", "10min"]
dist1, dist2, dist3, dist4, dist5 = data
label1, label2, label3, label4, label5 = labels
data = pd.DataFrame()
data["windspeeds"] = np.sort(np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist5.unique())))
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]

ax[0, 0].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
ax[0, 0].plot("windspeeds", "dist7", data=data, linewidth=1, label=label2)
ax[0, 0].plot("windspeeds", "dist8", data=data, linewidth=1, label=label3)
ax[0, 0].legend()

labels = ["daily", "six hourly", "three hourly", "hourly", "10min"]
data = [
    pd.Series(day),
    pd.Series(six_hour),
    pd.Series(three_hour),
    pd.Series(hour),
    pd.Series(average_10min),
]
dist1, dist2, dist3, dist4, dist5 = data
label1, label2, label3, label4, label5 = labels
data = pd.DataFrame()
data["windspeeds"] = np.sort(np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist5.unique())))
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[0, 1].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
ax[0, 1].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
ax[0, 1].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)

# load data
average_daily = np.load("data/Pickles/Penmanshiel/average_daily.npy")
average_hourly = np.load("data/Pickles/Penmanshiel/average_hourly.npy")
average_10min = np.load("data/Pickles/Penmanshiel/average_10min.npy")
average_monthly = np.load("data/Pickles/Penmanshiel/average_monthly.npy")
day = np.load("data/Pickles/Penmanshiel/day.npy")
six_hour = np.load("data/Pickles/Penmanshiel/six_hour.npy")
three_hour = np.load("data/Pickles/Penmanshiel/three_hour.npy")
hour = np.load("data/Pickles/Penmanshiel/hour.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

data = [
    pd.Series(average_daily),
    pd.Series(average_six_hourly),
    pd.Series(average_three_hourly),
    pd.Series(average_hourly),
    pd.Series(average_10min),
]
labels = ["daily", "six hourly", "three hourly", "hourly", "10min"]
dist1, dist2, dist3, dist4, dist5 = data
label1, label2, label3, label4, label5 = labels
data = pd.DataFrame()
data["windspeeds"] = np.sort(np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist5.unique())))
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[1, 0].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
ax[1, 0].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
ax[1, 0].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)

labels = ["daily", "six hourly", "three hourly", "hourly", "10min"]
data = [
    pd.Series(day),
    pd.Series(six_hour),
    pd.Series(three_hour),
    pd.Series(hour),
    pd.Series(average_10min),
]
dist1, dist2, dist3, dist4, dist5 = data
label1, label2, label3, label4, label5 = labels
data = pd.DataFrame()
data["windspeeds"] = np.sort(np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist5.unique())))
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[1, 1].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
ax[1, 1].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
ax[1, 1].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)

# load data
average_daily = np.load("data/Pickles/NWTC/average_daily.npy")
average_hourly = np.load("data/Pickles/NWTC/average_hourly.npy")
average_10min = np.load("data/Pickles/NWTC/average_10min.npy")
average_monthly = np.load("data/Pickles/NWTC/average_monthly.npy")
day = np.load("data/Pickles/NWTC/day.npy")
six_hour = np.load("data/Pickles/NWTC/six_hour.npy")
three_hour = np.load("data/Pickles/NWTC/three_hour.npy")
hour = np.load("data/Pickles/NWTC/hour.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)
data = [
    pd.Series(average_daily),
    pd.Series(average_six_hourly),
    pd.Series(average_three_hourly),
    pd.Series(average_hourly),
    pd.Series(average_10min),
]
labels = ["daily", "six hourly", "three hourly", "hourly", "10min"]
dist1, dist2, dist3, dist4, dist5 = data
label1, label2, label3, label4, label5 = labels
data = pd.DataFrame()
data["windspeeds"] = np.sort(np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist5.unique())))
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[2, 0].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
ax[2, 0].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
ax[2, 0].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)

labels = ["daily", "six hourly", "three hourly", "hourly", "10min"]
data = [
    pd.Series(day),
    pd.Series(six_hour),
    pd.Series(three_hour),
    pd.Series(hour),
    pd.Series(average_10min),
]
dist1, dist2, dist3, dist4, dist5 = data
label1, label2, label3, label4, label5 = labels
data = pd.DataFrame()
data["windspeeds"] = np.sort(np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist5.unique())))
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[2, 1].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
ax[2, 1].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
ax[2, 1].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)

# load data
average_daily = np.load("data/Pickles/Owez/average_daily.npy")
average_hourly = np.load("data/Pickles/Owez/average_hourly.npy")
average_10min = np.load("data/Pickles/Owez/average_10min.npy")
average_monthly = np.load("data/Pickles/Owez/average_monthly.npy")
day = np.load("data/Pickles/Owez/day.npy")
six_hour = np.load("data/Pickles/Owez/six_hour.npy")
three_hour = np.load("data/Pickles/Owez/three_hour.npy")
hour = np.load("data/Pickles/Owez/hour.npy")
days = np.load("data/Pickles/Owez/days.npy", allow_pickle=True)
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

data = [
    pd.Series(average_daily),
    pd.Series(average_six_hourly),
    pd.Series(average_three_hourly),
    pd.Series(average_hourly),
    pd.Series(average_10min),
]
labels = ["daily", "six hourly", "three hourly", "hourly", "10min"]
dist1, dist2, dist3, dist4, dist5 = data
label1, label2, label3, label4, label5 = labels
data = pd.DataFrame()
data["windspeeds"] = np.sort(np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist5.unique())))
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[3, 0].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
ax[3, 0].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
ax[3, 0].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)

labels = ["daily", "six hourly", "three hourly", "hourly", "10min"]
data = [
    pd.Series(day),
    pd.Series(six_hour),
    pd.Series(three_hour),
    pd.Series(hour),
    pd.Series(average_10min),
]
dist1, dist2, dist3, dist4, dist5 = data
label1, label2, label3, label4, label5 = labels
data = pd.DataFrame()
data["windspeeds"] = np.sort(np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist5.unique())))
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[3, 1].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
ax[3, 1].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
ax[3, 1].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)


plt.xlim([0, 25])

ax[0, 0].text(0.03, 0.85, "(1a)", transform=ax[0, 0].transAxes)
ax[1, 0].text(0.03, 0.85, "(2a)", transform=ax[1, 0].transAxes)
ax[2, 0].text(0.03, 0.85, "(3a)", transform=ax[2, 0].transAxes)
ax[3, 0].text(0.03, 0.85, "(4a)", transform=ax[3, 0].transAxes)
ax[0, 1].text(0.03, 0.85, "(1b)", transform=ax[0, 1].transAxes)
ax[1, 1].text(0.03, 0.85, "(2b)", transform=ax[1, 1].transAxes)
ax[2, 1].text(0.03, 0.85, "(3b)", transform=ax[2, 1].transAxes)
ax[3, 1].text(0.03, 0.85, "(4b)", transform=ax[3, 1].transAxes)

custom_ylim = (-0.1, 0.3)
plt.setp(ax, ylim=custom_ylim)

# Setting the values for all axes.
fig.supxlabel(r"Wind speed ($\frac{m}{s}$)")
fig.supylabel(r"Cumulative density")
plt.savefig(savepath)
plt.show()
