"""
Generate plot for Weibull parameters of averaged data. 
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)

savepath = "plots_eps/appendix/weibull_param_trend_3param.eps"

fig, ax = plt.subplots(2, 4, sharex=True, figsize=(8.27, 4), constrained_layout=True)
cs = np.load("data/weibull_params/3_param/cs_kelmarsh.npy")
scales = np.load("data/weibull_params/3_param/scales_kelmarsh.npy")
locs = np.load("data/weibull_params/3_param/locs_kelmarsh.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 0].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[0, 0].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[0, 0].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2, 3])
ax[0, 0].set_xticklabels(["10min", "3h", "6h", "day"])
ax[0, 0].legend(loc="center left")

cs = np.load("data/weibull_params/3_param/cs_penmanshiel.npy")
scales = np.load("data/weibull_params/3_param/scales_penmanshiel.npy")
locs = np.load("data/weibull_params/3_param/locs_penmanshiel.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 1].plot(cs[:-1] / cs[0])
ax[0, 1].plot(scales[:-1] / scales[0])
ax[0, 1].plot(locs[:-1] / locs[0])
ax[0, 1].set_xticks([0, 1, 2, 3])
ax[0, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 2].plot(cs[:-1] / cs[0])
ax[0, 2].plot(scales[:-1] / scales[0])
ax[0, 2].plot(locs[:-1] / locs[0])
ax[0, 2].set_xticks([0, 1, 2, 3])
ax[0, 2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_owez.npy")
scales = np.load("data/weibull_params/3_param/scales_owez.npy")
locs = np.load("data/weibull_params/3_param/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 3].plot(cs[:-1] / cs[0])
ax[0, 3].plot(scales[:-1] / scales[0])
ax[0, 3].plot(locs[:-1] / locs[0])
ax[0, 3].set_xticks([0, 1, 2, 3])
ax[0, 3].set_xticklabels(["10min", "3h", "6h", "day"])


cs = np.load("data/weibull_params/3_param/cs_aachen.npy")
scales = np.load("data/weibull_params/3_param/scales_aachen.npy")
locs = np.load("data/weibull_params/3_param/locs_aachen.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)


ax[1, 0].plot(cs[:-1] / cs[0])
ax[1, 0].plot(scales[:-1] / scales[0])
ax[1, 0].plot(locs[:-1] / locs[0])
ax[1, 0].set_xticks([0, 1, 2, 3])
ax[1, 0].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_zugspitze.npy")
scales = np.load("data/weibull_params/3_param/scales_zugspitze.npy")
locs = np.load("data/weibull_params/3_param/locs_zugspitze.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)


ax[1, 1].plot(cs[:-1] / cs[0])
ax[1, 1].plot(scales[:-1] / scales[0])
ax[1, 1].plot(locs[:-1] / locs[0])
ax[1, 1].set_xticks([0, 1, 2, 3, 4, 5])
ax[1, 1].set_xticklabels(["10min", "1h", "3h", "6h", "day", "month"])

cs = np.load("data/weibull_params/3_param/cs_boltenhagen.npy")
scales = np.load("data/weibull_params/3_param/scales_boltenhagen.npy")
locs = np.load("data/weibull_params/3_param/locs_boltenhagen.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)


ax[1, 2].plot(cs[:-1] / cs[0])
ax[1, 2].plot(scales[:-1] / scales[0])
ax[1, 2].plot(locs[:-1] / locs[0])
ax[1, 2].set_xticks([0, 1, 2, 3])
ax[1, 2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_fichtelberg.npy")
scales = np.load("data/weibull_params/3_param/scales_fichtelberg.npy")
locs = np.load("data/weibull_params/3_param/locs_fichtelberg.npy")
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
fig.supylabel(r"Parameter value")


ax[0, 0].text(0.03, 0.9, "(a)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.9, "(b)", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.9, "(c)", transform=ax[0, 2].transAxes)
ax[0, 3].text(0.03, 0.9, "(d)", transform=ax[0, 3].transAxes)
ax[1, 0].text(0.03, 0.9, "(e)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.9, "(f)", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.9, "(g)", transform=ax[1, 2].transAxes)
ax[1, 3].text(0.03, 0.9, "(h)", transform=ax[1, 3].transAxes)

plt.savefig(savepath)

savepath = "plots_eps/appendix/weibull_param_trend_3param_abs.eps"

fig, ax = plt.subplots(2, 4, sharex=True, figsize=(8.27, 4), constrained_layout=True)
cs = np.load("data/weibull_params/3_param/cs_kelmarsh.npy")
scales = np.load("data/weibull_params/3_param/scales_kelmarsh.npy")
locs = np.load("data/weibull_params/3_param/locs_kelmarsh.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 0].plot(cs[:-1], label=r"$\beta$")
ax[0, 0].plot(scales[:-1], label=r"$\lambda$")
ax[0, 0].plot(locs[:-1], label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2, 3])
ax[0, 0].set_xticklabels(["10min", "3h", "6h", "day"])
ax[0, 0].legend(loc="upper right")
cs = np.load("data/weibull_params/3_param/cs_penmanshiel.npy")
scales = np.load("data/weibull_params/3_param/scales_penmanshiel.npy")
locs = np.load("data/weibull_params/3_param/locs_penmanshiel.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 1].plot(cs[:-1])
ax[0, 1].plot(scales[:-1])
ax[0, 1].plot(locs[:-1])
ax[0, 1].set_xticks([0, 1, 2, 3])
ax[0, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 2].plot(cs[:-1])
ax[0, 2].plot(scales[:-1])
ax[0, 2].plot(locs[:-1])
ax[0, 2].set_xticks([0, 1, 2, 3])
ax[0, 2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_owez.npy")
scales = np.load("data/weibull_params/3_param/scales_owez.npy")
locs = np.load("data/weibull_params/3_param/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 3].plot(cs[:-1])
ax[0, 3].plot(scales[:-1])
ax[0, 3].plot(locs[:-1])
ax[0, 3].set_xticks([0, 1, 2, 3])
ax[0, 3].set_xticklabels(["10min", "3h", "6h", "day"])


cs = np.load("data/weibull_params/3_param/cs_aachen.npy")
scales = np.load("data/weibull_params/3_param/scales_aachen.npy")
locs = np.load("data/weibull_params/3_param/locs_aachen.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 0].plot(cs[:-1])
ax[1, 0].plot(scales[:-1])
ax[1, 0].plot(locs[:-1])
ax[1, 0].set_xticks([0, 1, 2, 3])
ax[1, 0].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_zugspitze.npy")
scales = np.load("data/weibull_params/3_param/scales_zugspitze.npy")
locs = np.load("data/weibull_params/3_param/locs_zugspitze.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 1].plot(cs[:-1])
ax[1, 1].plot(scales[:-1])
ax[1, 1].plot(locs[:-1])
ax[1, 1].set_xticks([0, 1, 2, 3])
ax[1, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_boltenhagen.npy")
scales = np.load("data/weibull_params/3_param/scales_boltenhagen.npy")
locs = np.load("data/weibull_params/3_param/locs_boltenhagen.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 2].plot(cs[:-1])
ax[1, 2].plot(scales[:-1])
ax[1, 2].plot(locs[:-1])
ax[1, 2].set_xticks([0, 1, 2, 3])
ax[1, 2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_fichtelberg.npy")
scales = np.load("data/weibull_params/3_param/scales_fichtelberg.npy")
locs = np.load("data/weibull_params/3_param/locs_fichtelberg.npy")
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
fig.supylabel(r"Parameter value")

custom_ylim = (-1, 13)
plt.setp(ax, ylim=custom_ylim)

ax[0, 0].text(0.03, 0.9, "(a)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.9, "(b)", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.9, "(c)", transform=ax[0, 2].transAxes)
ax[0, 3].text(0.03, 0.9, "(d)", transform=ax[0, 3].transAxes)
ax[1, 0].text(0.03, 0.9, "(e)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.9, "(f)", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.9, "(g)", transform=ax[1, 2].transAxes)
ax[1, 3].text(0.03, 0.9, "(h)", transform=ax[1, 3].transAxes)
plt.savefig(savepath)
plt.show()
