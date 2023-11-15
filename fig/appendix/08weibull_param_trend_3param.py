"""
Generate plot for Weibull parameters of averaged data. 
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

savepath = "wind-variability/plots_eps/appendix/weibull_param_trend_3param.pdf"

fig, ax = plt.subplots(2, 4, sharex=True, figsize=(6, 3.5), constrained_layout=True)
cs = np.load("wind-variability/data/weibull_params/3_param/cs_kelmarsh.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_kelmarsh.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_kelmarsh.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 0].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[0, 0].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[0, 0].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2, 3])
ax[0, 0].set_xticklabels(["10min", "3h", "6h", "day"])
ax[0, 0].legend(loc="center left")

cs = np.load("wind-variability/data/weibull_params/3_param/cs_penmanshiel.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_penmanshiel.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_penmanshiel.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 1].plot(cs[:-1] / cs[0])
ax[0, 1].plot(scales[:-1] / scales[0])
ax[0, 1].plot(locs[:-1] / locs[0])
ax[0, 1].set_xticks([0, 1, 2, 3])
ax[0, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_nwtc5.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_nwtc5.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 2].plot(cs[:-1] / cs[0])
ax[0, 2].plot(scales[:-1] / scales[0])
ax[0, 2].plot(locs[:-1] / locs[0])
ax[0, 2].set_xticks([0, 1, 2, 3])
ax[0, 2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_owez.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_owez.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 3].plot(cs[:-1] / cs[0])
ax[0, 3].plot(scales[:-1] / scales[0])
ax[0, 3].plot(locs[:-1] / locs[0])
ax[0, 3].set_xticks([0, 1, 2, 3])
ax[0, 3].set_xticklabels(["10min", "3h", "6h", "day"])


cs = np.load("wind-variability/data/weibull_params/3_param/cs_aachen.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_aachen.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_aachen.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)


ax[1, 0].plot(cs[:-1] / cs[0])
ax[1, 0].plot(scales[:-1] / scales[0])
ax[1, 0].plot(locs[:-1] / locs[0])
ax[1, 0].set_xticks([0, 1, 2, 3])
ax[1, 0].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_zugspitze.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_zugspitze.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_zugspitze.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)


ax[1, 1].plot(cs[:-1] / cs[0])
ax[1, 1].plot(scales[:-1] / scales[0])
ax[1, 1].plot(locs[:-1] / locs[0])
ax[1, 1].set_xticks([0, 1, 2, 3, 4, 5])
ax[1, 1].set_xticklabels(["10min", "1h", "3h", "6h", "day", "month"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_boltenhagen.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_boltenhagen.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_boltenhagen.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)


ax[1, 2].plot(cs[:-1] / cs[0])
ax[1, 2].plot(scales[:-1] / scales[0])
ax[1, 2].plot(locs[:-1] / locs[0])
ax[1, 2].set_xticks([0, 1, 2, 3])
ax[1, 2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_fichtelberg.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_fichtelberg.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_fichtelberg.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)


ax[1, 3].plot(cs[:-1] / cs[0])
ax[1, 3].plot(scales[:-1] / scales[0])
ax[1, 3].plot(locs[:-1] / locs[0])
ax[1, 3].set_xticks([0, 1, 2, 3])
ax[1, 3].set_xticklabels(["10min", "3h", "6h", "day"])

ax[0, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 3].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 3].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))

fig.supxlabel(r"Resolution")
fig.supylabel(r"Relative parameter change")


ax[0, 0].text(0.03, 0.85, "(a)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.85, "(b)", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.85, "(c)", transform=ax[0, 2].transAxes)
ax[0, 3].text(0.03, 0.85, "(d)", transform=ax[0, 3].transAxes)
ax[1, 0].text(0.03, 0.85, "(e)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.85, "(f)", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.85, "(g)", transform=ax[1, 2].transAxes)
ax[1, 3].text(0.03, 0.85, "(h)", transform=ax[1, 3].transAxes)


plt.setp(ax[0, 0].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1, 0].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[0, 2].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[0, 3].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[0, 1].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1, 1].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1, 2].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1, 3].get_xticklabels(), rotation=90, ha="center")

plt.savefig(savepath)

savepath = "wind-variability/plots_eps/appendix/weibull_param_trend_3param_abs.pdf"

fig, ax = plt.subplots(2, 4, figsize=(6, 3.5), sharex=True, sharey=True, constrained_layout=True)
cs = np.load("wind-variability/data/weibull_params/3_param/cs_kelmarsh.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_kelmarsh.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_kelmarsh.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 0].plot(cs[:-1], label=r"$\beta$")
ax[0, 0].plot(scales[:-1], label=r"$\lambda$")
ax[0, 0].plot(locs[:-1], label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2, 3])
ax[0, 0].set_xticklabels(["10min", "3h", "6h", "day"])
cs = np.load("wind-variability/data/weibull_params/3_param/cs_penmanshiel.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_penmanshiel.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_penmanshiel.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 1].plot(cs[:-1])
ax[0, 1].plot(scales[:-1])
ax[0, 1].plot(locs[:-1])
ax[0, 1].set_xticks([0, 1, 2, 3])
ax[0, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_nwtc5.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_nwtc5.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 2].plot(cs[:-1])
ax[0, 2].plot(scales[:-1])
ax[0, 2].plot(locs[:-1])
ax[0, 2].set_xticks([0, 1, 2, 3])
ax[0, 2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_owez.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_owez.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 3].plot(cs[:-1])
ax[0, 3].plot(scales[:-1])
ax[0, 3].plot(locs[:-1])
ax[0, 3].set_xticks([0, 1, 2, 3])
ax[0, 3].set_xticklabels(["10min", "3h", "6h", "day"])


cs = np.load("wind-variability/data/weibull_params/3_param/cs_aachen.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_aachen.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_aachen.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 0].plot(cs[:-1], label=r"$\beta$")
ax[1, 0].plot(scales[:-1], label=r"$\lambda$")
ax[1, 0].plot(locs[:-1], label=r"$\theta$")
ax[1, 0].set_xticklabels(["10min", "3h", "6h", "day"])
ax[1, 0].legend(loc="upper right")

cs = np.load("wind-variability/data/weibull_params/3_param/cs_zugspitze.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_zugspitze.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_zugspitze.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 1].plot(cs[:-1])
ax[1, 1].plot(scales[:-1])
ax[1, 1].plot(locs[:-1])
ax[1, 1].set_xticks([0, 1, 2, 3])
ax[1, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_boltenhagen.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_boltenhagen.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_boltenhagen.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 2].plot(cs[:-1])
ax[1, 2].plot(scales[:-1])
ax[1, 2].plot(locs[:-1])
ax[1, 2].set_xticks([0, 1, 2, 3])
ax[1, 2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_fichtelberg.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_fichtelberg.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_fichtelberg.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 3].plot(cs[:-1])
ax[1, 3].plot(scales[:-1])
ax[1, 3].plot(locs[:-1])
ax[1, 3].set_xticks([0, 1, 2, 3])
ax[1, 3].set_xticklabels(["10min", "3h", "6h", "day"])

ax[0, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 3].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 3].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))

ax[0, 0].set_ylim([0, 8])
ax[0, 1].set_ylim([0, 10])
ax[0, 2].set_ylim([0, 8])
ax[0, 3].set_ylim([0, 11])
ax[1, 0].set_ylim([0, 5])
ax[1, 1].set_ylim([0, 10])
ax[1, 2].set_ylim([0, 8])
ax[1, 3].set_ylim([0, 4])

fig.supxlabel(r"Resolution")
fig.supylabel(r"Fitted parmeter")

custom_ylim = (-1, 13)
plt.setp(ax, ylim=custom_ylim)

ax[0, 0].text(0.03, 0.85, "(a)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.85, "(b)", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.85, "(c)", transform=ax[0, 2].transAxes)
ax[0, 3].text(0.03, 0.85, "(d)", transform=ax[0, 3].transAxes)
ax[1, 0].text(0.03, 0.85, "(e)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.85, "(f)", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.85, "(g)", transform=ax[1, 2].transAxes)
ax[1, 3].text(0.03, 0.85, "(h)", transform=ax[1, 3].transAxes)

plt.setp(ax[0, 0].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1, 0].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[0, 2].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[0, 3].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[0, 1].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1, 1].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1, 2].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1, 3].get_xticklabels(), rotation=90, ha="center")


plt.savefig(savepath)
plt.show()
