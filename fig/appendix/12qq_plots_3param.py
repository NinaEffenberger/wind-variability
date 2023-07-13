import glob
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn
import xarray as xr
from scipy import stats
from scipy.stats import weibull_min
from windspeed_averages_wp import (
    compute_average_windspeeds,
    drop_nans,
    drop_nans_DWD,
    load_data,
    set_date,
    set_date_DWD,
)

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)

# load data
average_daily = np.load("data/Pickles/Kelmarsh/average_daily.npy")
average_hourly = np.load("data/Pickles/Kelmarsh/average_hourly.npy")
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
average_monthly = np.load("data/Pickles/Kelmarsh/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("data/weibull_params/3_param/cs_kelmarsh.npy")
scales = np.load("data/weibull_params/3_param/scales_kelmarsh.npy")
locs = np.load("data/weibull_params/3_param/locs_kelmarsh.npy")


fig, ax = plt.subplots(8, 5, sharex=True, sharey=True, figsize=(8.27, 11.69), constrained_layout=True)
stats.probplot(average_10min, dist=weibull_min(c=cs[0], loc=locs[0], scale=scales[0]), plot=ax[0, 0])
stats.probplot(
    average_hourly,
    dist=weibull_min(c=cs[1], loc=locs[1], scale=scales[1]),
    plot=ax[0, 1],
)

stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=weibull_min(c=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[0, 2],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=weibull_min(c=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[0, 3],
)
stats.probplot(average_daily, dist=weibull_min(c=cs[4], loc=locs[4], scale=scales[4]), plot=ax[0, 4])


# load data
average_daily = np.load("data/Pickles/Penmanshiel/average_daily.npy")
average_hourly = np.load("data/Pickles/Penmanshiel/average_hourly.npy")
average_10min = np.load("data/Pickles/Penmanshiel/average_10min.npy")
average_monthly = np.load("data/Pickles/Penmanshiel/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("data/weibull_params/3_param/cs_penmanshiel.npy")
scales = np.load("data/weibull_params/3_param/scales_penmanshiel.npy")
locs = np.load("data/weibull_params/3_param/locs_penmanshiel.npy")

stats.probplot(average_10min, dist=weibull_min(c=cs[0], loc=locs[0], scale=scales[0]), plot=ax[1, 0])
stats.probplot(
    average_hourly,
    dist=weibull_min(c=cs[1], loc=locs[1], scale=scales[1]),
    plot=ax[1, 1],
)
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=weibull_min(c=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[1, 2],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=weibull_min(c=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[1, 3],
)
stats.probplot(average_daily, dist=weibull_min(c=cs[4], loc=locs[4], scale=scales[4]), plot=ax[1, 4])

# load data
average_daily = np.load("data/Pickles/NWTC/average_daily.npy")
average_hourly = np.load("data/Pickles/NWTC/average_hourly.npy")
average_10min = np.load("data/Pickles/NWTC/average_10min.npy")
average_monthly = np.load("data/Pickles/NWTC/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("data/weibull_params/3_param/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param/locs_nwtc5.npy")

stats.probplot(average_10min, dist=weibull_min(c=cs[0], loc=locs[0], scale=scales[0]), plot=ax[2, 0])
stats.probplot(
    average_hourly,
    dist=weibull_min(c=cs[1], loc=locs[1], scale=scales[1]),
    plot=ax[2, 1],
)
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=weibull_min(c=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[2, 2],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=weibull_min(c=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[2, 3],
)
stats.probplot(average_daily, dist=weibull_min(c=cs[4], loc=locs[4], scale=scales[4]), plot=ax[2, 4])

# load data
average_daily = np.load("data/Pickles/Owez/average_daily.npy")
average_hourly = np.load("data/Pickles/Owez/average_hourly.npy")
average_10min = np.load("data/Pickles/Owez/average_10min.npy")
average_monthly = np.load("data/Pickles/Owez/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("data/weibull_params/3_param/cs_owez.npy")
scales = np.load("data/weibull_params/3_param/scales_owez.npy")
locs = np.load("data/weibull_params/3_param/locs_owez.npy")

stats.probplot(average_10min, dist=weibull_min(c=cs[0], loc=locs[0], scale=scales[0]), plot=ax[3, 0])
stats.probplot(
    average_hourly,
    dist=weibull_min(c=cs[1], loc=locs[1], scale=scales[1]),
    plot=ax[3, 1],
)
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=weibull_min(c=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[3, 2],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=weibull_min(c=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[3, 3],
)
stats.probplot(average_daily, dist=weibull_min(c=cs[4], loc=locs[4], scale=scales[4]), plot=ax[3, 4])

# load data
average_daily = np.load("data/Pickles/Aachen/average_daily.npy")
average_hourly = np.load("data/Pickles/Aachen/average_hourly.npy")
average_10min = np.load("data/Pickles/Aachen/average_10min.npy")
average_monthly = np.load("data/Pickles/Aachen/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("data/weibull_params/3_param/cs_aachen.npy")
scales = np.load("data/weibull_params/3_param/scales_aachen.npy")
locs = np.load("data/weibull_params/3_param/locs_aachen.npy")

stats.probplot(average_10min, dist=weibull_min(c=cs[0], loc=locs[0], scale=scales[0]), plot=ax[4, 0])
stats.probplot(
    average_hourly,
    dist=weibull_min(c=cs[1], loc=locs[1], scale=scales[1]),
    plot=ax[4, 1],
)
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=weibull_min(c=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[4, 2],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=weibull_min(c=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[4, 3],
)
stats.probplot(average_daily, dist=weibull_min(c=cs[4], loc=locs[4], scale=scales[4]), plot=ax[4, 4])

# load data
average_daily = np.load("data/Pickles/Zugspitze/average_daily.npy")
average_hourly = np.load("data/Pickles/Zugspitze/average_hourly.npy")
average_10min = np.load("data/Pickles/Zugspitze/average_10min.npy")
average_monthly = np.load("data/Pickles/Zugspitze/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("data/weibull_params/3_param/cs_zugspitze.npy")
scales = np.load("data/weibull_params/3_param/scales_zugspitze.npy")
locs = np.load("data/weibull_params/3_param/locs_zugspitze.npy")

stats.probplot(average_10min, dist=weibull_min(c=cs[0], loc=locs[0], scale=scales[0]), plot=ax[5, 0])
stats.probplot(
    average_hourly,
    dist=weibull_min(c=cs[1], loc=locs[1], scale=scales[1]),
    plot=ax[5, 1],
)
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=weibull_min(c=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[5, 2],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=weibull_min(c=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[5, 3],
)
stats.probplot(average_daily, dist=weibull_min(c=cs[4], loc=locs[4], scale=scales[4]), plot=ax[5, 4])

# load data
average_daily = np.load("data/Pickles/Boltenhagen/average_daily.npy")
average_hourly = np.load("data/Pickles/Boltenhagen/average_hourly.npy")
average_10min = np.load("data/Pickles/Boltenhagen/average_10min.npy")
average_monthly = np.load("data/Pickles/Boltenhagen/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("data/weibull_params/3_param/cs_boltenhagen.npy")
scales = np.load("data/weibull_params/3_param/scales_boltenhagen.npy")
locs = np.load("data/weibull_params/3_param/locs_boltenhagen.npy")

set = 6
stats.probplot(average_10min, dist=weibull_min(c=cs[0], loc=locs[0], scale=scales[0]), plot=ax[set, 0])
stats.probplot(
    average_hourly,
    dist=weibull_min(c=cs[1], loc=locs[1], scale=scales[1]),
    plot=ax[set, 1],
)
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=weibull_min(c=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[set, 2],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=weibull_min(c=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[set, 3],
)
stats.probplot(average_daily, dist=weibull_min(c=cs[4], loc=locs[4], scale=scales[4]), plot=ax[set, 4])

# load data
average_daily = np.load("data/Pickles/Fichtelberg/average_daily.npy")
average_hourly = np.load("data/Pickles/Fichtelberg/average_hourly.npy")
average_10min = np.load("data/Pickles/Fichtelberg/average_10min.npy")
average_monthly = np.load("data/Pickles/Fichtelberg/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("data/weibull_params/3_param/cs_fichtelberg.npy")
scales = np.load("data/weibull_params/3_param/scales_fichtelberg.npy")
locs = np.load("data/weibull_params/3_param/locs_fichtelberg.npy")

set = 7
stats.probplot(average_10min, dist=weibull_min(c=cs[0], loc=locs[0], scale=scales[0]), plot=ax[set, 0])
stats.probplot(
    average_hourly,
    dist=weibull_min(c=cs[1], loc=locs[1], scale=scales[1]),
    plot=ax[set, 1],
)
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=weibull_min(c=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[set, 2],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=weibull_min(c=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[set, 3],
)
stats.probplot(average_daily, dist=weibull_min(c=cs[4], loc=locs[4], scale=scales[4]), plot=ax[set, 4])

num = ["1", "2", "3", "4", "5", "6", "7", "8"]
letter = ["a", "b", "c", "d", "e"]
for i in range(8):
    for j in range(5):
        ax[i, j].set_title("")
        ax[i, j].set_ylabel("")
        ax[i, j].set_xlabel("")
        ax[i, j].get_lines()[0].set_markerfacecolor("#E69F00")
        ax[i, j].get_lines()[0].set_markeredgecolor("#E69F00")
        ax[i, j].get_lines()[0].set_markersize(1.0)
        ax[i, j].get_lines()[1].set_linewidth(1.0)
        ax[i, j].get_lines()[1].set_color("#56B4E9")
        ax[i, j].text(0.03, 0.9, "(" + num[i] + letter[j] + ")", transform=ax[i, j].transAxes)


# fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axis
# plt.tick_params(labelcolor="none", which="both", top=False, bottom=False, left=False, right=False)
# plt.xlabel("Theoretical Quantiles")
# plt.ylabel("Empirical Quantiles")
# seaborn.despine()
fig.supxlabel(r"Weibull Quantiles")
fig.supylabel(r"Empirical Quantiles")

fig.savefig("plots_eps/appendix/qq_plot_weibull.eps")
fig.savefig("plots_eps/appendix/qq_plot_weibull.png")
