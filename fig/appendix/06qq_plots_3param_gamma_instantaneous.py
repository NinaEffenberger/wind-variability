"""
Generate QQ-plots for instantaneous data and its Gamma parametrizations.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import gamma

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)
# load data
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
day = np.load("data/Pickles/Kelmarsh/day.npy")
six_hour = np.load("data/Pickles/Kelmarsh/six_hour.npy")
three_hour = np.load("data/Pickles/Kelmarsh/three_hour.npy")
hour = np.load("data/Pickles/Kelmarsh/hour.npy")


cs = np.load("data/gamma_params/3_param_instantaneous/cs_kelmarsh.npy")
scales = np.load("data/gamma_params/3_param_instantaneous/scales_kelmarsh.npy")
locs = np.load("data/gamma_params/3_param_instantaneous/locs_kelmarsh.npy")


fig, ax = plt.subplots(8, 4, sharex=True, sharey=True, figsize=(8.27, 11.69), constrained_layout=True)
stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[0, 0])
stats.probplot(
    np.array(three_hour).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[0, 1],
)
stats.probplot(
    np.array(six_hour).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[0, 2],
)
stats.probplot(day, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[0, 3])


# load data
average_10min = np.load("data/Pickles/Penmanshiel/average_10min.npy")
day = np.load("data/Pickles/Penmanshiel/day.npy")
six_hour = np.load("data/Pickles/Penmanshiel/six_hour.npy")
three_hour = np.load("data/Pickles/Penmanshiel/three_hour.npy")
hour = np.load("data/Pickles/Penmanshiel/hour.npy")


cs = np.load("data/gamma_params/3_param_instantaneous/cs_penmanshiel.npy")
scales = np.load("data/gamma_params/3_param_instantaneous/scales_penmanshiel.npy")
locs = np.load("data/gamma_params/3_param_instantaneous/locs_penmanshiel.npy")

stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[1, 0])
stats.probplot(
    np.array(three_hour).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[1, 1],
)
stats.probplot(
    np.array(six_hour).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[1, 2],
)
stats.probplot(day, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[1, 3])

# load data
average_10min = np.load("data/Pickles/NWTC/average_10min.npy")
day = np.load("data/Pickles/NWTC/day.npy")
six_hour = np.load("data/Pickles/NWTC/six_hour.npy")
three_hour = np.load("data/Pickles/NWTC/three_hour.npy")
hour = np.load("data/Pickles/NWTC/hour.npy")

cs = np.load("data/gamma_params/3_param_instantaneous/cs_nwtc5.npy")
scales = np.load("data/gamma_params/3_param_instantaneous/scales_nwtc5.npy")
locs = np.load("data/gamma_params/3_param_instantaneous/locs_nwtc5.npy")

stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[2, 0])
stats.probplot(
    np.array(three_hour).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[2, 1],
)
stats.probplot(
    np.array(six_hour).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[2, 2],
)
stats.probplot(day, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[2, 3])

# load data
average_10min = np.load("data/Pickles/Owez/average_10min.npy")
day = np.load("data/Pickles/Owez/day.npy")
six_hour = np.load("data/Pickles/Owez/six_hour.npy")
three_hour = np.load("data/Pickles/Owez/three_hour.npy")
hour = np.load("data/Pickles/Owez/hour.npy")

cs = np.load("data/gamma_params/3_param_instantaneous/cs_owez.npy")
scales = np.load("data/gamma_params/3_param_instantaneous/scales_owez.npy")
locs = np.load("data/gamma_params/3_param_instantaneous/locs_owez.npy")

stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[3, 0])
stats.probplot(
    np.array(three_hour).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[3, 1],
)
stats.probplot(
    np.array(six_hour).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[3, 2],
)
stats.probplot(day, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[3, 3])

# load data
average_10min = np.load("data/Pickles/Aachen/average_10min.npy")
day = np.load("data/Pickles/Aachen/day.npy")
six_hour = np.load("data/Pickles/Aachen/six_hour.npy")
three_hour = np.load("data/Pickles/Aachen/three_hour.npy")
hour = np.load("data/Pickles/Aachen/hour.npy")

cs = np.load("data/gamma_params/3_param_instantaneous/cs_aachen.npy")
scales = np.load("data/gamma_params/3_param_instantaneous/scales_aachen.npy")
locs = np.load("data/gamma_params/3_param_instantaneous/locs_aachen.npy")

stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[4, 0])
stats.probplot(
    np.array(three_hour).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[4, 1],
)
stats.probplot(
    np.array(six_hour).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[4, 2],
)
stats.probplot(day, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[4, 3])

# load data
average_10min = np.load("data/Pickles/Zugspitze/average_10min.npy")
day = np.load("data/Pickles/Zugspitze/day.npy")
six_hour = np.load("data/Pickles/Zugspitze/six_hour.npy")
three_hour = np.load("data/Pickles/Zugspitze/three_hour.npy")
hour = np.load("data/Pickles/Zugspitze/hour.npy")

cs = np.load("data/gamma_params/3_param_instantaneous/cs_zugspitze.npy")
scales = np.load("data/gamma_params/3_param_instantaneous/scales_zugspitze.npy")
locs = np.load("data/gamma_params/3_param_instantaneous/locs_zugspitze.npy")

stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[5, 0])
stats.probplot(
    np.array(three_hour).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[5, 1],
)
stats.probplot(
    np.array(six_hour).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[5, 2],
)
stats.probplot(day, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[5, 3])

# load data
average_10min = np.load("data/Pickles/Boltenhagen/average_10min.npy")
day = np.load("data/Pickles/Boltenhagen/day.npy")
six_hour = np.load("data/Pickles/Boltenhagen/six_hour.npy")
three_hour = np.load("data/Pickles/Boltenhagen/three_hour.npy")
hour = np.load("data/Pickles/Boltenhagen/hour.npy")

cs = np.load("data/gamma_params/3_param_instantaneous/cs_boltenhagen.npy")
scales = np.load("data/gamma_params/3_param_instantaneous/scales_boltenhagen.npy")
locs = np.load("data/gamma_params/3_param_instantaneous/locs_boltenhagen.npy")

set = 6
stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[set, 0])
stats.probplot(
    np.array(three_hour).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[set, 1],
)
stats.probplot(
    np.array(six_hour).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[set, 2],
)
stats.probplot(day, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[set, 3])

# load data
average_10min = np.load("data/Pickles/Fichtelberg/average_10min.npy")
day = np.load("data/Pickles/Fichtelberg/day.npy")
six_hour = np.load("data/Pickles/Fichtelberg/six_hour.npy")
three_hour = np.load("data/Pickles/Fichtelberg/three_hour.npy")
hour = np.load("data/Pickles/Fichtelberg/hour.npy")

cs = np.load("data/gamma_params/3_param_instantaneous/cs_fichtelberg.npy")
scales = np.load("data/gamma_params/3_param_instantaneous/scales_fichtelberg.npy")
locs = np.load("data/gamma_params/3_param_instantaneous/locs_fichtelberg.npy")

set = 7
stats.probplot(average_10min, dist=gamma(a=cs[0], loc=locs[0], scale=scales[0]), plot=ax[set, 0])
stats.probplot(
    np.array(three_hour).flatten(),
    dist=gamma(a=cs[2], loc=locs[2], scale=scales[2]),
    plot=ax[set, 1],
)
stats.probplot(
    np.array(six_hour).flatten(),
    dist=gamma(a=cs[3], loc=locs[3], scale=scales[3]),
    plot=ax[set, 2],
)
stats.probplot(day, dist=gamma(a=cs[4], loc=locs[4], scale=scales[4]), plot=ax[set, 3])


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
        ax[i, j].text(0.03, 0.9, "(" + letter[i] + ")", transform=ax[i, j].transAxes)

cols = ["10min", "3h", "6h", "day"]
for c, ax in zip(cols, ax[0]):
    ax.set_title(c, size="large")

fig.supxlabel(r"Weibull Quantiles")
fig.supylabel(r"Empirical Quantiles")

fig.savefig("plots_eps/appendix/qq_plot_gamma_instantaneous.pdf")
fig.savefig("plots_eps/appendix/qq_plot_gamma_instantaneous.png")
fig.savefig("plots_eps/appendix/qq_plot_gamma_instantaneous.jpg", dpi=1000)
