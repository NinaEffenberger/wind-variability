"""
Generate QQ-plots for averaged data and its Gamma parametrizations.
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import gamma

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)
from tueplots import fonts


matplotlib.rcParams.update({"font.size": 12})
matplotlib.rcParams.update({"axes.labelsize": 12})
matplotlib.rcParams.update({"legend.fontsize": 12})
matplotlib.rcParams.update({"xtick.labelsize": 12})
matplotlib.rcParams.update({"ytick.labelsize": 12})
matplotlib.rcParams.update({"axes.titlesize": 12})
plt.rcParams.update(fonts.neurips2021())

# load data
average_daily = np.load("wind-variability/data/Pickles/Kelmarsh/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Kelmarsh/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Kelmarsh/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Kelmarsh/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("wind-variability/data/gamma_params/3_param/cs_kelmarsh.npy")
scales = np.load("wind-variability/data/gamma_params/3_param/scales_kelmarsh.npy")
locs = np.load("wind-variability/data/gamma_params/3_param/locs_kelmarsh.npy")


fig, ax = plt.subplots(8, 4, sharex=True, sharey=True, figsize=(8.27, 11.69), constrained_layout=True)
stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[0, 0])
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[0, 1],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[0, 2],
)
stats.probplot(average_daily, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[0, 3])

# load data
average_daily = np.load("wind-variability/data/Pickles/Penmanshiel/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Penmanshiel/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Penmanshiel/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Penmanshiel/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)


cs = np.load("wind-variability/data/gamma_params/3_param/cs_penmanshiel.npy")
scales = np.load("wind-variability/data/gamma_params/3_param/scales_penmanshiel.npy")
locs = np.load("wind-variability/data/gamma_params/3_param/locs_penmanshiel.npy")

stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[1, 0])

stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[1, 1],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[1, 2],
)
stats.probplot(average_daily, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[1, 3])

# load data
average_daily = np.load("wind-variability/data/Pickles/NWTC/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/NWTC/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/NWTC/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/NWTC/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("wind-variability/data/gamma_params/3_param/cs_nwtc5.npy")
scales = np.load("wind-variability/data/gamma_params/3_param/scales_nwtc5.npy")
locs = np.load("wind-variability/data/gamma_params/3_param/locs_nwtc5.npy")

stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[2, 0])
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[2, 1],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[2, 2],
)
stats.probplot(average_daily, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[2, 3])

# load data
average_daily = np.load("wind-variability/data/Pickles/Owez/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Owez/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Owez/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Owez/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("wind-variability/data/gamma_params/3_param/cs_owez.npy")
scales = np.load("wind-variability/data/gamma_params/3_param/scales_owez.npy")
locs = np.load("wind-variability/data/gamma_params/3_param/locs_owez.npy")

stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[3, 0])

stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[3, 1],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[3, 2],
)
stats.probplot(average_daily, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[3, 3])

# load data
average_daily = np.load("wind-variability/data/Pickles/Aachen/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Aachen/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Aachen/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Aachen/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("wind-variability/data/gamma_params/3_param/cs_aachen.npy")
scales = np.load("wind-variability/data/gamma_params/3_param/scales_aachen.npy")
locs = np.load("wind-variability/data/gamma_params/3_param/locs_aachen.npy")

stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[4, 0])
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[4, 1],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[4, 2],
)
stats.probplot(average_daily, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[4, 3])

# load data
average_daily = np.load("wind-variability/data/Pickles/Zugspitze/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Zugspitze/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Zugspitze/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Zugspitze/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)


cs = np.load("wind-variability/data/gamma_params/3_param/cs_zugspitze.npy")
scales = np.load("wind-variability/data/gamma_params/3_param/scales_zugspitze.npy")
locs = np.load("wind-variability/data/gamma_params/3_param/locs_zugspitze.npy")

stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[5, 0])
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[5, 1],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[5, 2],
)
stats.probplot(average_daily, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[5, 3])

# load data
average_daily = np.load("wind-variability/data/Pickles/Boltenhagen/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Boltenhagen/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Boltenhagen/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Boltenhagen/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)


cs = np.load("wind-variability/data/gamma_params/3_param/cs_boltenhagen.npy")
scales = np.load("wind-variability/data/gamma_params/3_param/scales_boltenhagen.npy")
locs = np.load("wind-variability/data/gamma_params/3_param/locs_boltenhagen.npy")

set = 6
stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[set, 0])
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[set, 1],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[set, 2],
)
stats.probplot(average_daily, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[set, 3])

# load data
average_daily = np.load("wind-variability/data/Pickles/Fichtelberg/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Fichtelberg/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Fichtelberg/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Fichtelberg/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs = np.load("wind-variability/data/gamma_params/3_param/cs_fichtelberg.npy")
scales = np.load("wind-variability/data/gamma_params/3_param/scales_fichtelberg.npy")
locs = np.load("wind-variability/data/gamma_params/3_param/locs_fichtelberg.npy")

set = 7
stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[set, 0])
stats.probplot(
    np.array(average_three_hourly).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[set, 1],
)
stats.probplot(
    np.array(average_six_hourly).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[set, 2],
)
stats.probplot(average_daily, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[set, 3])

num = ["1", "2", "3", "4", "5", "6", "7", "8"]
letter = ["a", "b", "c", "d", "e", "f", "g", "h"]
for i in range(8):
    for j in range(4):
        ax[i, j].set_title("")
        ax[i, j].set_ylabel("")
        ax[i, j].set_xlabel("")
        ax[i, j].get_lines()[0].set_markerfacecolor("#E69F00")
        ax[i, j].get_lines()[0].set_markeredgecolor("#E69F00")
        ax[i, j].get_lines()[0].set_markersize(1.0)
        ax[i, j].get_lines()[1].set_linewidth(1.0)
        ax[i, j].get_lines()[1].set_color("#56B4E9")
        ax[i, j].text(0.03, 0.9, "(" + num[j]+letter[i] + ")", transform=ax[i, j].transAxes)

cols = ["10min", "3h", "6h", "day"]
for c, ax in zip(cols, ax[0]):
    ax.set_title(c, size="large")

fig.supxlabel(r"Gamma Quantiles")
fig.supylabel(r"Empirical Quantiles")

fig.savefig("wind-variability/plots_eps/appendix/qq_plot_gamma.jpg", dpi=1000)
