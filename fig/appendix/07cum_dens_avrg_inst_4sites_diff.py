"""
Generate cumulative wind speed difference plot of 10min DWD data and other resolutions. 
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from tueplots import fonts

matplotlib.rcParams.update({"font.size": 14})
matplotlib.rcParams.update({"axes.labelsize": 14})
matplotlib.rcParams.update({"legend.fontsize": 14})
matplotlib.rcParams.update({"xtick.labelsize": 14})
matplotlib.rcParams.update({"ytick.labelsize": 14})
matplotlib.rcParams.update({"axes.titlesize": 14})
plt.rcParams.update(fonts.neurips2021())

savepath = "wind-variability/plots_eps/appendix/cum_dens_avrg_inst_4sites_diff.pdf"
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)
fig, ax = plt.subplots(4, 2, sharex=True, sharey=True, figsize=(6, 4.5), layout="constrained")

# load data
average_daily = np.load("wind-variability/data/Pickles/Aachen/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Aachen/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Aachen/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Aachen/average_monthly.npy")
day = np.load("wind-variability/data/Pickles/Aachen/day.npy")
six_hour = np.load("wind-variability/data/Pickles/Aachen/six_hour.npy")
three_hour = np.load("wind-variability/data/Pickles/Aachen/three_hour.npy")
hour = np.load("wind-variability/data/Pickles/Aachen/hour.npy")

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
average_daily = np.load("wind-variability/data/Pickles/Zugspitze/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Zugspitze/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Zugspitze/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Zugspitze/average_monthly.npy")
day = np.load("wind-variability/data/Pickles/Zugspitze/day.npy")
six_hour = np.load("wind-variability/data/Pickles/Zugspitze/six_hour.npy")
three_hour = np.load("wind-variability/data/Pickles/Zugspitze/three_hour.npy")
hour = np.load("wind-variability/data/Pickles/Zugspitze/hour.npy")
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
average_daily = np.load("wind-variability/data/Pickles/Boltenhagen/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Boltenhagen/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Boltenhagen/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Boltenhagen/average_monthly.npy")
day = np.load("wind-variability/data/Pickles/Boltenhagen/day.npy")
six_hour = np.load("wind-variability/data/Pickles/Boltenhagen/six_hour.npy")
three_hour = np.load("wind-variability/data/Pickles/Boltenhagen/three_hour.npy")
hour = np.load("wind-variability/data/Pickles/Boltenhagen/hour.npy")
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
average_daily = np.load("wind-variability/data/Pickles/Fichtelberg/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Fichtelberg/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Fichtelberg/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Fichtelberg/average_monthly.npy")
day = np.load("wind-variability/data/Pickles/Fichtelberg/day.npy")
six_hour = np.load("wind-variability/data/Pickles/Fichtelberg/six_hour.npy")
three_hour = np.load("wind-variability/data/Pickles/Fichtelberg/three_hour.npy")
hour = np.load("wind-variability/data/Pickles/Fichtelberg/hour.npy")
days = np.load("wind-variability/data/Pickles/Fichtelberg/days.npy", allow_pickle=True)
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


plt.xlim([0, 20])

ax[0, 0].text(0.03, 0.8, "Aachen", transform=ax[0, 0].transAxes)
ax[1, 0].text(0.03, 0.8, "Zugspitze", transform=ax[1, 0].transAxes)
ax[2, 0].text(0.03, 0.8, "Boltenhagen", transform=ax[2, 0].transAxes)
ax[3, 0].text(0.03, 0.8, "Fichtelberg", transform=ax[3, 0].transAxes)
ax[0, 1].text(0.03, 0.8, "Aachen", transform=ax[0, 1].transAxes)
ax[1, 1].text(0.03, 0.8, "Zugspitze", transform=ax[1, 1].transAxes)
ax[2, 1].text(0.03, 0.8, "Boltenhagen", transform=ax[2, 1].transAxes)
ax[3, 1].text(0.03, 0.8, "Fichtelberg", transform=ax[3, 1].transAxes)

custom_ylim = (-0.2, 0.3)
plt.setp(ax, ylim=custom_ylim)

# Setting the values for all axes.
fig.supxlabel(r"Wind speed ($\frac{m}{s}$)")
fig.supylabel(r"Difference of cumulative densities")
fig.legend(*ax[0, 0].get_legend_handles_labels(), loc="outside right center")
cols = ["average", "instantaneous"]
for c, ax in zip(cols, ax[0]):
    ax.set_title(c, size="large")
plt.savefig(savepath)
plt.show()
