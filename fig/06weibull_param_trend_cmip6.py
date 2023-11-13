"""
Generate plot that shows how Weibull parameters of CMIP6 evolve.
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
from scipy import stats
from tueplots import fonts
matplotlib.rcParams.update({"font.size": 13})
matplotlib.rcParams.update({"axes.labelsize": 14})
matplotlib.rcParams.update({"legend.fontsize": 14})
matplotlib.rcParams.update({"xtick.labelsize": 14})
matplotlib.rcParams.update({"ytick.labelsize": 14})
matplotlib.rcParams.update({"axes.titlesize": 14})
plt.rcParams.update(fonts.neurips2021())

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)

fig, ax = plt.subplots(1, 4, sharex=True, sharey=True, figsize=(6, 2.5), layout="constrained")
time_series_day = np.load("wind-variability/data/cmip6/data/Aachen/time_series_day.npy")
time_series_six = np.load("wind-variability/data/cmip6/data/Aachen/time_series_six.npy")
time_series_three = np.load("wind-variability/data/cmip6/data/Aachen/time_series_three.npy")

dist = stats.weibull_min
bounds = [(0, 15), (0, 15), (0, 15)]

cs_avrg = []
locs_avrg = []
scales_avrg = []

fit = stats.fit(dist, time_series_three, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

fit = stats.fit(dist, time_series_six, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

fit = stats.fit(dist, time_series_day, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

ax[0].plot(cs_avrg, label=r"$\beta$")
ax[0].plot(scales_avrg, label=r"$\lambda$")
ax[0].plot(locs_avrg, label=r"$\theta$")
ax[0].set_xticks([0, 1, 2])
ax[0].set_xticklabels(["3h", "6h", "day"])
plt.setp(ax[0].get_xticklabels(), rotation=90, ha="center")

time_series_day = np.load("wind-variability/data/cmip6/data/Zugspitze/time_series_day.npy")
time_series_six = np.load("wind-variability/data/cmip6/data/Zugspitze/time_series_six.npy")
time_series_three = np.load("wind-variability/data/cmip6/data/Zugspitze/time_series_three.npy")

dist = stats.weibull_min
bounds = [(0, 15), (0, 15), (0, 15)]

cs_avrg = []
locs_avrg = []
scales_avrg = []

fit = stats.fit(dist, time_series_three, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

fit = stats.fit(dist, time_series_six, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

fit = stats.fit(dist, time_series_day, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

ax[1].plot(cs_avrg)
ax[1].plot(scales_avrg)
ax[1].plot(locs_avrg)
ax[1].set_xticks([0, 1, 2])
ax[1].set_xticklabels(["3h", "6h", "day"])
plt.setp(ax[1].get_xticklabels(), rotation=90, ha="center")

time_series_day = np.load("wind-variability/data/cmip6/data/Boltenhagen/time_series_day.npy")
time_series_six = np.load("wind-variability/data/cmip6/data/Boltenhagen/time_series_six.npy")
time_series_three = np.load("wind-variability/data/cmip6/data/Boltenhagen/time_series_three.npy")

dist = stats.weibull_min
bounds = [(0, 15), (0, 15), (0, 15)]

cs_avrg = []
locs_avrg = []
scales_avrg = []

fit = stats.fit(dist, time_series_three, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

fit = stats.fit(dist, time_series_six, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

fit = stats.fit(dist, time_series_day, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

ax[2].plot(cs_avrg)
ax[2].plot(scales_avrg)
ax[2].plot(locs_avrg)
ax[2].set_xticks([0, 1, 2])
ax[2].set_xticklabels(["3h", "6h", "day"])
plt.setp(ax[2].get_xticklabels(), rotation=90, ha="center")

time_series_day = np.load("wind-variability/data/cmip6/data/Fichtelberg/time_series_day.npy")
time_series_six = np.load("wind-variability/data/cmip6/data/Fichtelberg/time_series_six.npy")
time_series_three = np.load("wind-variability/data/cmip6/data/Fichtelberg/time_series_three.npy")

dist = stats.weibull_min
bounds = [(0, 15), (0, 15), (0, 15)]

cs_avrg = []
locs_avrg = []
scales_avrg = []

fit = stats.fit(dist, time_series_three, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

fit = stats.fit(dist, time_series_six, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

fit = stats.fit(dist, time_series_day, bounds)
cs_avrg.append(fit.params.c)
locs_avrg.append(fit.params.loc)
scales_avrg.append(fit.params.scale)

ax[3].plot(cs_avrg)
ax[3].plot(scales_avrg)
ax[3].plot(locs_avrg)
ax[3].set_xticks([0, 1, 2])
ax[3].set_xticklabels(["3h", "6h", "day"])
plt.setp(ax[3].get_xticklabels(), rotation=90, ha="center")


cs = np.load("wind-variability/data/weibull_params/3_param/cs_aachen.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_aachen.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_aachen.npy")

ax[0].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[0].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[0].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[0].set_xticks([0, 1, 2])
ax[0].set_xticklabels(["3h", "6h", "day"])
plt.setp(ax[0].get_xticklabels(), rotation=90, ha="center")

cs = np.load("wind-variability/data/weibull_params/3_param/cs_zugspitze.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_zugspitze.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_zugspitze.npy")

ax[1].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[1].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[1].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[1].set_xticks([0, 1, 2])
ax[1].set_xticklabels(["3h", "6h", "day"])
plt.setp(ax[1].get_xticklabels(), rotation=90, ha="center")

cs = np.load("wind-variability/data/weibull_params/3_param/cs_boltenhagen.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_boltenhagen.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_boltenhagen.npy")

ax[2].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[2].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[2].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[2].set_xticks([0, 1, 2])
ax[2].set_xticklabels(["3h", "6h", "day"])
plt.setp(ax[2].get_xticklabels(), rotation=90, ha="center")

cs = np.load("wind-variability/data/weibull_params/3_param/cs_fichtelberg.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_fichtelberg.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_fichtelberg.npy")

ax[3].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[3].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[3].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[3].set_xticks([0, 1, 2])
ax[3].set_xticklabels(["3h", "6h", "day"])
plt.setp(ax[3].get_xticklabels(), rotation=90, ha="center")

fig.supxlabel(r"Resolution")
fig.supylabel(r"Fitted parameter")

custom_ylim = (-1, 11)
plt.setp(ax, ylim=custom_ylim)

ax[0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[3].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))

ax[0].text(0.03, 0.9, "Aachen", transform=ax[0].transAxes)
ax[1].text(0.03, 0.9, "Zugspitze", transform=ax[1].transAxes)
ax[2].text(0.03, 0.9, "Boltenhagen", transform=ax[2].transAxes)
ax[3].text(0.03, 0.9, "Fichtelberg", transform=ax[3].transAxes)
fig.legend(loc="outside right center")
plt.savefig("wind-variability/plots_eps/weibull_cmip6.pdf")
plt.show()