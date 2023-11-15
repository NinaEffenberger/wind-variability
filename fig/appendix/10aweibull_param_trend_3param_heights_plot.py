"""
Generate plot for Weibull parameters of averaged data of different heights. 
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
from tueplots import fonts


plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)
matplotlib.rcParams.update({"font.size": 14})
matplotlib.rcParams.update({"axes.labelsize": 14})
matplotlib.rcParams.update({"legend.fontsize": 13})
matplotlib.rcParams.update({"xtick.labelsize": 14})
matplotlib.rcParams.update({"ytick.labelsize": 14})
matplotlib.rcParams.update({"axes.titlesize": 14})
plt.rcParams.update(fonts.neurips2021())
savepath = "wind-variability/plots_eps/appendix/weibull_param_trend_3param_heights.pdf"

fig, ax = plt.subplots(2, 3, sharex="col", figsize=(6, 3.5), constrained_layout=True)
cs = np.load("wind-variability/data/weibull_params/3_param/10m/cs_nwtc5.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/10m/scales_nwtc5.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/10m/locs_nwtc5.npy")

ax[0, 0].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[0, 0].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[0, 0].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2, 3])
ax[0, 0].set_xticklabels(["10min", "3h", "6h", "day"])
ax[0, 0].legend()

cs = np.load("wind-variability/data/weibull_params/3_param/41m/cs_nwtc5.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/41m/scales_nwtc5.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/41m/locs_nwtc5.npy")

ax[0, 1].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[0, 1].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[0, 1].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[0, 1].set_xticks([0, 1, 2, 3])
ax[0, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/130m/cs_nwtc5.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/130m/scales_nwtc5.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/130m/locs_nwtc5.npy")

ax[0, 2].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[0, 2].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[0, 2].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[0, 2].set_xticks([0, 1, 2, 3])
ax[0, 2].set_xticklabels(["10min", "3h", "6h", "day"])


cs = np.load("wind-variability/data/weibull_params/3_param/21m/cs_owez.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/21m/scales_owez.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/21m/locs_owez.npy")

ax[1, 0].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[1, 0].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[1, 0].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[1, 0].set_xticks([0, 1, 2, 3])
ax[1, 0].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/70m/cs_owez.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/70m/scales_owez.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/70m/locs_owez.npy")

ax[1, 1].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[1, 1].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[1, 1].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[1, 1].set_xticks([0, 1, 2, 3])
ax[1, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/116m/cs_owez.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/116m/scales_owez.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/116m/locs_owez.npy")

ax[1, 2].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[1, 2].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[1, 2].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[1, 2].set_xticks([0, 1, 2, 3])
ax[1, 2].set_xticklabels(["10min", "3h", "6h", "day"])



fig.supxlabel(r"Resolution")
fig.supylabel(r"Fitted parameter")
plt.savefig(savepath)


savepath = "wind-variability/plots_eps/appendix/weibull_param_trend_3param_heights_abs.pdf"

fig, ax = plt.subplots(2, 3, sharex="col", figsize=(6, 4), sharey=True, constrained_layout=True)
cs = np.load("wind-variability/data/weibull_params/3_param/21m/cs_owez.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/21m/scales_owez.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/21m/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 0].plot(cs[:-1], label=r"$\beta$")
ax[1, 0].plot(scales[:-1], label=r"$\lambda$")
ax[1, 0].plot(locs[:-1], label=r"$\theta$")
ax[1, 0].set_xticks([0, 1, 2, 3])
ax[1, 0].set_xticklabels(["10min", "3h", "6h", "day"])


cs = np.load("wind-variability/data/weibull_params/3_param/70m/cs_owez.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/70m/scales_owez.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/70m/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 1].plot(cs[:-1], label=r"$\beta$")
ax[1, 1].plot(scales[:-1], label=r"$\lambda$")
ax[1, 1].plot(locs[:-1], label=r"$\theta$")
ax[1, 1].set_xticks([0, 1, 2, 3])
ax[1, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/116m/cs_owez.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/116m/scales_owez.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/116m/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 2].plot(cs[:-1], label=r"$\beta$")
ax[1, 2].plot(scales[:-1], label=r"$\lambda$")
ax[1, 2].plot(locs[:-1], label=r"$\theta$")
ax[1, 2].set_xticks([0, 1, 2, 3])
ax[1, 2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/10m/cs_nwtc5.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/10m/scales_nwtc5.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/10m/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 0].plot(cs[:-1], label=r"$\beta$")
ax[0, 0].plot(scales[:-1], label=r"$\lambda$")
ax[0, 0].plot(locs[:-1], label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2, 3])
ax[0, 0].set_xticklabels(["10min", "3h", "6h", "day"])
ax[0, 0].legend()

cs = np.load("wind-variability/data/weibull_params/3_param/41m/cs_nwtc5.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/41m/scales_nwtc5.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/41m/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 1].plot(cs[:-1], label=r"$\beta$")
ax[0, 1].plot(scales[:-1], label=r"$\lambda$")
ax[0, 1].plot(locs[:-1], label=r"$\theta$")
ax[0, 1].set_xticks([0, 1, 2, 3])
ax[0, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/130m/cs_nwtc5.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/130m/scales_nwtc5.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/130m/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 2].plot(cs[:-1], label=r"$\beta$")
ax[0, 2].plot(scales[:-1], label=r"$\lambda$")
ax[0, 2].plot(locs[:-1], label=r"$\theta$")
ax[0, 2].set_xticks([0, 1, 2, 3])
ax[0, 2].set_xticklabels(["10min", "3h", "6h", "day"])


custom_ylim = (-1, 11)
plt.setp(ax, ylim=custom_ylim)

ax[0, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))

ax[0, 0].text(0.03, 0.85, "Owez 10m", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.85, "Owez 41m", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.85, "Owez 130m", transform=ax[0, 2].transAxes)

ax[1, 0].text(0.03, 0.85, "NWTC 21m", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.85, "NWTC 70m", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.85, "NWTC 116m", transform=ax[1, 2].transAxes)

plt.setp(ax[0, 0].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1, 0].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[0, 2].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[0, 1].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1, 1].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1, 2].get_xticklabels(), rotation=90, ha="center")

fig.supxlabel(r"Resolution")
fig.supylabel(r"Fitted parameter")

plt.savefig(savepath)
plt.show()
