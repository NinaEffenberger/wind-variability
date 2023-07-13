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

savepath = "plots_eps/cum_dens_avrg_inst_4sites_diff.eps"
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
data["windspeeds"] = np.sort(
    np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist4.unique(), dist5.unique()))
)
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist4 = dist4.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist4"] = data["windspeeds"].apply(lambda x: np.mean(dist4 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]

ax[0, 0].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
# ax[0, 0].plot("windspeeds", "dist2", data=data, label=label2)
ax[0, 0].plot("windspeeds", "dist7", data=data, linewidth=1, label=label2)
# ax[0, 0].plot("windspeeds", "dist4", data=data, label=label4)
ax[0, 0].plot("windspeeds", "dist8", data=data, linewidth=1, label=label3)
ax[0, 0].legend()
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
data["windspeeds"] = np.sort(
    np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist4.unique(), dist5.unique()))
)
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist4 = dist4.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist4"] = data["windspeeds"].apply(lambda x: np.mean(dist4 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[1, 0].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
# ax[1, 0].plot("windspeeds", "dist2", data=data,  linewidth=1, label=label2)
ax[1, 0].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
# ax[1, 0].plot("windspeeds", "dist4", data=data,  linewidth=1, label=label4)
ax[1, 0].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)

# load data
average_daily = np.load("data/Pickles/NWTC/average_daily.npy")
average_hourly = np.load("data/Pickles/NWTC/average_hourly.npy")
average_10min = np.load("data/Pickles/NWTC/average_10min.npy")
average_monthly = np.load("data/Pickles/NWTC/average_monthly.npy")
day = np.load("data/Pickles/NWTC/day.npy")
six_hour = np.load("data/Pickles/NWTC/six_hour.npy")
three_hour = np.load("data/Pickles/NWTC/three_hour.npy")
hour = np.load("data/Pickles/NWTC/hour.npy")
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
data["windspeeds"] = np.sort(
    np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist4.unique(), dist5.unique()))
)
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist4 = dist4.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist4"] = data["windspeeds"].apply(lambda x: np.mean(dist4 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[2, 0].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
# ax[2, 0].plot("windspeeds", "dist2", data=data,  linewidth=1, label=label2)
ax[2, 0].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
# ax[2, 0].plot("windspeeds", "dist4", data=data,  linewidth=1, label=label4)
ax[2, 0].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)


# load data
average_daily = np.load("data/Pickles/Owez/average_daily.npy")
average_hourly = np.load("data/Pickles/Owez/average_hourly.npy")
average_10min = np.load("data/Pickles/Owez/average_10min.npy")
average_monthly = np.load("data/Pickles/Owez/average_monthly.npy")
day = np.load("data/Pickles/Owez/day.npy")
six_hour = np.load("data/Pickles/Owez/six_hour.npy")
three_hour = np.load("data/Pickles/Owez/three_hour.npy")
hour = np.load("data/Pickles/Owez/hour.npy")
days = np.load("data/power-gen/Owez/days.npy", allow_pickle=True)

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
data["windspeeds"] = np.sort(
    np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist4.unique(), dist5.unique()))
)
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist4 = dist4.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist4"] = data["windspeeds"].apply(lambda x: np.mean(dist4 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[3, 0].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
# ax[3, 0].plot("windspeeds", "dist2", data=data,  linewidth=1, label=label2)
ax[3, 0].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
# ax[3, 0].plot("windspeeds", "dist4", data=data,  linewidth=1, label=label4)
ax[3, 0].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)

# load data
paths = [
    "data/Kelmarsh/Turbine_Data_Kelmarsh_1_2016-01-03_-_2017-01-01_228.csv",
    "data/Kelmarsh/Turbine_Data_Kelmarsh_1_2017-01-01_-_2018-01-01_228.csv",
    "data/Kelmarsh/Turbine_Data_Kelmarsh_1_2018-01-01_-_2019-01-01_228.csv",
    "data/Kelmarsh/Turbine_Data_Kelmarsh_1_2019-01-01_-_2020-01-01_228.csv",
    "data/Kelmarsh/Turbine_Data_Kelmarsh_1_2020-01-01_-_2021-01-01_228.csv",
]
data = load_data(paths)
set_date(data, current_name="Date and time")
average_daily = compute_average_windspeeds(data, windspeeds="Wind speed (m/s)", only_daily=True)
data = drop_nans(data, average_daily)

# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="Wind speed (m/s)")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="Wind speed (m/s)")

labels = ["daily", "six hourly", "three hourly", "hourly", "10min"]
# plot_cumulative_densities(data, labels, "plots/open-source/Kelmarsh/1/cumulative_densities")
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
data["windspeeds"] = np.sort(
    np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist4.unique(), dist5.unique()))
)
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist4 = dist4.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist4"] = data["windspeeds"].apply(lambda x: np.mean(dist4 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[0, 1].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
# ax[0, 1].plot("windspeeds", "dist2", data=data,  linewidth=1, label=label2)
ax[0, 1].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
# ax[0, 1].plot("windspeeds", "dist4", data=data,  linewidth=1, label=label4)
ax[0, 1].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)

# load data
paths = [
    "data/Penmanshiel/Turbine_Data_Penmanshiel_11_2016-07-19_-_2017-01-01_1051.csv",
    "data/Penmanshiel/Turbine_Data_Penmanshiel_11_2017-01-01_-_2018-01-01_1051.csv",
    "data/Penmanshiel/Turbine_Data_Penmanshiel_11_2018-01-01_-_2019-01-01_1051.csv",
    "data/Penmanshiel/Turbine_Data_Penmanshiel_11_2019-01-01_-_2020-01-01_1051.csv",
    "data/Penmanshiel/Turbine_Data_Penmanshiel_11_2020-01-01_-_2021-01-01_1051.csv",
]
data = load_data(paths)
set_date(data, current_name="Date and time")
average_daily = compute_average_windspeeds(data, windspeeds="Wind speed (m/s)", only_daily=True)
data = drop_nans(data, average_daily)

# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="Wind speed (m/s)")
day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="Wind speed (m/s)")

labels = ["daily", "six hourly", "three hourly", "hourly", "10min"]
# plot_cumulative_densities(data, labels, "plots/open-source/Kelmarsh/1/cumulative_densities")
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
data["windspeeds"] = np.sort(
    np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist4.unique(), dist5.unique()))
)
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist4 = dist4.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist4"] = data["windspeeds"].apply(lambda x: np.mean(dist4 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[1, 1].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
# ax[1, 1].plot("windspeeds", "dist2", data=data,  linewidth=1, label=label2)
ax[1, 1].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
# ax[1, 1].plot("windspeeds", "dist4", data=data,  linewidth=1, label=label4)
ax[1, 1].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)


# load data
path = "data/tall_tower/nwtc_m5/huragl87S1/windagl87S1"
files = glob.glob(os.path.join(path, "*.nc"))

data = None
for f in files:
    # initialize dataframe
    if not isinstance(data, pd.DataFrame):
        ds = xr.open_dataset(f)
        data = ds.to_dataframe()
        data["date"] = data.index.get_level_values(0)
        data.set_index(["date"])
        average_daily = compute_average_windspeeds(data, windspeeds="windagl87S1", only_daily=True)
        data = drop_nans(data, average_daily)
    else:
        ds = xr.open_dataset(f)
        filedata = ds.to_dataframe()
        filedata["date"] = filedata.index.get_level_values(0)
        filedata.set_index(["date"])
        average_daily = compute_average_windspeeds(filedata, windspeeds="windagl87S1", only_daily=True)
        filedata = drop_nans(filedata, average_daily)
        data = pd.concat([data, filedata])


# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="windagl87S1")


day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="windagl87S1")

labels = ["daily", "six hourly", "three hourly", "hourly", "10min"]
# plot_cumulative_densities(data, labels, "plots/open-source/Kelmarsh/1/cumulative_densities")
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
data["windspeeds"] = np.sort(
    np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist4.unique(), dist5.unique()))
)
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist4 = dist4.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist4"] = data["windspeeds"].apply(lambda x: np.mean(dist4 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[2, 1].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
# ax[2, 1].plot("windspeeds", "dist2", data=data,  linewidth=1, label=label2)
ax[2, 1].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
# ax[2, 1].plot("windspeeds", "dist4", data=data,  linewidth=1, label=label4)
ax[2, 1].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)


# load data
path = "data/tall_tower/oweg/windagl116S1"
files = glob.glob(os.path.join(path, "*.nc"))

data = None
for f in files:
    # initialize dataframe
    if not isinstance(data, pd.DataFrame):
        ds = xr.open_dataset(f)
        data = ds.to_dataframe()
        data["date"] = data.index.get_level_values(0)
        data.set_index(["date"])
        average_daily = compute_average_windspeeds(data, windspeeds="windagl116S1", only_daily=True)
        data = drop_nans(data, average_daily)
    else:
        ds = xr.open_dataset(f)
        filedata = ds.to_dataframe()
        filedata["date"] = filedata.index.get_level_values(0)
        filedata.set_index(["date"])
        average_daily = compute_average_windspeeds(filedata, windspeeds="windagl116S1", only_daily=True)
        filedata = drop_nans(filedata, average_daily)
        data = pd.concat([data, filedata])


# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="windagl116S1")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="windagl116S1")

labels = ["daily", "six hourly", "three hourly", "hourly", "10min"]
# plot_cumulative_densities(data, labels, "plots/open-source/Kelmarsh/1/cumulative_densities")
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
data["windspeeds"] = np.sort(
    np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist4.unique(), dist5.unique()))
)
dist1 = dist1.values
dist2 = dist2.values
dist3 = dist3.values
dist4 = dist4.values
dist5 = dist5.values
data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
data["dist4"] = data["windspeeds"].apply(lambda x: np.mean(dist4 <= x))
data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
data["dist6"] = data["dist5"] - data["dist1"]
data["dist7"] = data["dist5"] - data["dist2"]
data["dist8"] = data["dist5"] - data["dist3"]
ax[3, 1].plot("windspeeds", "dist6", data=data, linewidth=1, label=label1)
# ax[3, 1].plot("windspeeds", "dist2", data=data,  linewidth=1, label=label2)
ax[3, 1].plot("windspeeds", "dist7", data=data, linewidth=1, label=label3)
# ax[3, 1].plot("windspeeds", "dist4", data=data,  linewidth=1, label=label4)
ax[3, 1].plot("windspeeds", "dist8", data=data, linewidth=1, label=label5)


plt.xlim([0, 25])

ax[0, 0].text(0.03, 0.9, "(1a)", transform=ax[0, 0].transAxes)
ax[1, 0].text(0.03, 0.9, "(2a)", transform=ax[1, 0].transAxes)
ax[2, 0].text(0.03, 0.9, "(3a)", transform=ax[2, 0].transAxes)
ax[3, 0].text(0.03, 0.9, "(4a)", transform=ax[3, 0].transAxes)
ax[0, 1].text(0.03, 0.9, "(1b)", transform=ax[0, 1].transAxes)
ax[1, 1].text(0.03, 0.9, "(2b)", transform=ax[1, 1].transAxes)
ax[2, 1].text(0.03, 0.9, "(3b)", transform=ax[2, 1].transAxes)
ax[3, 1].text(0.03, 0.9, "(4b)", transform=ax[3, 1].transAxes)

custom_ylim = (-0.1, 0.3)
plt.setp(ax, ylim=custom_ylim)

# Setting the values for all axes.
fig.supxlabel(r"Wind speed ($\frac{m}{s}$)")
fig.supylabel(r"Cumulative density")
plt.savefig(savepath)
