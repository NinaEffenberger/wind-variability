import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter
from scipy import stats
from scipy.stats import weibull_min
import matplotlib

matplotlib.rcParams.update({"font.size": 12})

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)

fig, ax = plt.subplots(
    2, 4, sharex=True, sharey=True, figsize=(6, 4), constrained_layout=True
)
time_series_day = np.load("data/cmip6/data/Aachen/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Aachen/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Aachen/time_series_three.npy")

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

ax[1, 0].plot(cs_avrg)
ax[1, 0].plot(scales_avrg)
ax[1, 0].plot(locs_avrg)
ax[1, 0].set_xticks([0, 1, 2])
ax[1, 0].set_xticklabels(["3h", "6h", "day"])

time_series_day = np.load("data/cmip6/data/Zugspitze/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Zugspitze/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Zugspitze/time_series_three.npy")

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

ax[1, 1].plot(cs_avrg)
ax[1, 1].plot(scales_avrg)
ax[1, 1].plot(locs_avrg)
ax[1, 1].set_xticks([0, 1, 2])
ax[1, 1].set_xticklabels(["3h", "6h", "day"])

time_series_day = np.load("data/cmip6/data/Boltenhagen/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Boltenhagen/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Boltenhagen/time_series_three.npy")

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

ax[1, 2].plot(cs_avrg)
ax[1, 2].plot(scales_avrg)
ax[1, 2].plot(locs_avrg)
ax[1, 2].set_xticks([0, 1, 2])
ax[1, 2].set_xticklabels(["3h", "6h", "day"])

time_series_day = np.load("data/cmip6/data/Fichtelberg/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Fichtelberg/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Fichtelberg/time_series_three.npy")

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

ax[1, 3].plot(cs_avrg)
ax[1, 3].plot(scales_avrg)
ax[1, 3].plot(locs_avrg)
ax[1, 3].set_xticks([0, 1, 2])
ax[1, 3].set_xticklabels(["3h", "6h", "day"])

time_series_day = np.load("data/cmip6/data/Penmanshiel/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Penmanshiel/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Penmanshiel/time_series_three.npy")

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

ax[0, 1].plot(cs_avrg)
ax[0, 1].plot(scales_avrg)
ax[0, 1].plot(locs_avrg)
ax[0, 1].set_xticks([0, 1, 2])
ax[0, 1].set_xticklabels(["3h", "6h", "day"])

time_series_day = np.load("data/cmip6/data/Kelmarsh/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Kelmarsh/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Kelmarsh/time_series_three.npy")

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

ax[0, 0].plot(cs_avrg, label=r"$\beta$")
ax[0, 0].plot(scales_avrg, label=r"$\lambda$")
ax[0, 0].plot(locs_avrg, label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2])
ax[0, 0].set_xticklabels(["3h", "6h", "day"])

time_series_day = np.load("data/cmip6/data/NWTC/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/NWTC/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/NWTC/time_series_three.npy")

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

ax[0, 2].plot(cs_avrg)
ax[0, 2].plot(scales_avrg)
ax[0, 2].plot(locs_avrg)
ax[0, 2].set_xticks([0, 1, 2])
ax[0, 2].set_xticklabels(["3h", "6h", "day"])

time_series_day = np.load("data/cmip6/data/Owez/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Owez/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Owez/time_series_three.npy")

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

ax[0, 3].plot(cs_avrg)
ax[0, 3].plot(scales_avrg)
ax[0, 3].plot(locs_avrg)
ax[0, 3].set_xticks([0, 1, 2])
ax[0, 3].set_xticklabels(["3h", "6h", "day"])

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)

cs = np.load("data/weibull_params/3_param/cs_kelmarsh.npy")
scales = np.load("data/weibull_params/3_param/scales_kelmarsh.npy")
locs = np.load("data/weibull_params/3_param/locs_kelmarsh.npy")

ax[0, 0].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[0, 0].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[0, 0].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[0, 0].set_xticks([0, 1, 2])
ax[0, 0].set_xticklabels(["3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_penmanshiel.npy")
scales = np.load("data/weibull_params/3_param/scales_penmanshiel.npy")
locs = np.load("data/weibull_params/3_param/locs_penmanshiel.npy")

ax[0, 1].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[0, 1].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[0, 1].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[0, 1].set_xticks([0, 1, 2])
ax[0, 1].set_xticklabels(["3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param/locs_nwtc5.npy")

ax[0, 2].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[0, 2].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[0, 2].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[0, 2].set_xticks([0, 1, 2])
ax[0, 2].set_xticklabels(["3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_owez.npy")
scales = np.load("data/weibull_params/3_param/scales_owez.npy")
locs = np.load("data/weibull_params/3_param/locs_owez.npy")

ax[0, 3].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[0, 3].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[0, 3].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[0, 3].set_xticks([0, 1, 2])
ax[0, 3].set_xticklabels(["3h", "6h", "day"])


cs = np.load("data/weibull_params/3_param/cs_aachen.npy")
scales = np.load("data/weibull_params/3_param/scales_aachen.npy")
locs = np.load("data/weibull_params/3_param/locs_aachen.npy")

ax[1, 0].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[1, 0].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[1, 0].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[1, 0].set_xticks([0, 1, 2])
ax[1, 0].set_xticklabels(["3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_zugspitze.npy")
scales = np.load("data/weibull_params/3_param/scales_zugspitze.npy")
locs = np.load("data/weibull_params/3_param/locs_zugspitze.npy")

ax[1, 1].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[1, 1].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[1, 1].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[1, 1].set_xticks([0, 1, 2])
ax[1, 1].set_xticklabels(["3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_boltenhagen.npy")
scales = np.load("data/weibull_params/3_param/scales_boltenhagen.npy")
locs = np.load("data/weibull_params/3_param/locs_boltenhagen.npy")

ax[1, 2].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[1, 2].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[1, 2].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[1, 2].set_xticks([0, 1, 2])
ax[1, 2].set_xticklabels(["3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_fichtelberg.npy")
scales = np.load("data/weibull_params/3_param/scales_fichtelberg.npy")
locs = np.load("data/weibull_params/3_param/locs_fichtelberg.npy")

ax[1, 3].plot(cs[2:-1], color="#E69F00", linestyle="dashed")
ax[1, 3].plot(scales[2:-1], color="#56B4E9", linestyle="dashed")
ax[1, 3].plot(locs[2:-1], color="#009E73", linestyle="dashed")
ax[1, 3].set_xticks([0, 1, 2])
ax[1, 3].set_xticklabels(["3h", "6h", "day"])
fig.supxlabel(r"Resolution")
fig.supylabel(r"Parameter value")

custom_ylim = (-1, 11)
plt.setp(ax, ylim=custom_ylim)

ax[0, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 3].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 3].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))

ax[0, 0].text(0.03, 0.9, "1)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.9, "2)", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.9, "3)", transform=ax[0, 2].transAxes)
ax[0, 3].text(0.03, 0.9, "4)", transform=ax[0, 3].transAxes)
ax[1, 0].text(0.03, 0.9, "5)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.9, "6)", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.9, "7)", transform=ax[1, 2].transAxes)
ax[1, 3].text(0.03, 0.9, "8)", transform=ax[1, 3].transAxes)
fig.legend(loc="outside right center")
plt.savefig("plots_eps/weibull_cmip6.eps")
