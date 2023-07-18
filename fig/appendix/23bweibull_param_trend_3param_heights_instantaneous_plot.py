import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)
"""
savepath = plots_eps/appendix/weibull_param_trend_3param_heights_instantaneous.eps"

fig, ax = plt.subplots(2, 4, sharex="col", figsize=(8.27, 4), constrained_layout=True)
cs = np.load("data/weibull_params/3_param_instantaneous/10m/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/10m/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/10m/locs_nwtc5.npy")

ax[1, 0].plot(cs / cs[0], label=r"$\beta$")
ax[1, 0].plot(scales / scales[0], label=r"$\lambda$")
ax[1, 0].plot(locs / locs[0], label=r"$\theta$")
ax[1, 0].set_xticks([0, 1, 2, 3])
ax[1, 0].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/41m/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/41m/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/41m/locs_nwtc5.npy")

ax[1, 1].plot(cs / cs[0], label=r"$\beta$")
ax[1, 1].plot(scales / scales[0], label=r"$\lambda$")
ax[1, 1].plot(locs / locs[0], label=r"$\theta$")
ax[1, 1].set_xticks([0, 1, 2, 3])
ax[1, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/cs_owez.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/scales_owez.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/locs_owez.npy")

ax[1, 2].plot(cs / cs[0], label=r"$\beta$")
ax[1, 2].plot(scales / scales[0], label=r"$\lambda$")
ax[1, 2].plot(locs / locs[0], label=r"$\theta$")
ax[1, 2].set_xticks([0, 1, 2, 3])
ax[1, 2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/130m/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/130m/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/130m/locs_nwtc5.npy")

ax[1, 3].plot(cs / cs[0], label=r"$\beta$")
ax[1, 3].plot(scales / scales[0], label=r"$\lambda$")
ax[1, 3].plot(locs / locs[0], label=r"$\theta$")
ax[1, 3].set_xticks([0, 1, 2, 3])
ax[1, 3].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/21m/cs_owez.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/21m/scales_owez.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/21m/locs_owez.npy")

ax[0, 0].plot(cs / cs[0], label=r"$\beta$")
ax[0, 0].plot(scales / scales[0], label=r"$\lambda$")
ax[0, 0].plot(locs / locs[0], label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2, 3])
ax[0, 0].set_xticklabels(["10min", "3h", "6h", "day"])
ax[0, 0].legend()

cs = np.load("data/weibull_params/3_param_instantaneous/70m/cs_owez.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/70m/scales_owez.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/70m/locs_owez.npy")

ax[0, 1].plot(cs / cs[0], label=r"$\beta$")
ax[0, 1].plot(scales / scales[0], label=r"$\lambda$")
ax[0, 1].plot(locs / locs[0], label=r"$\theta$")
ax[0, 1].set_xticks([0, 1, 2, 3])
ax[0, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/116m/cs_owez.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/116m/scales_owez.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/116m/locs_owez.npy")

ax[0, 2].plot(cs / cs[0], label=r"$\beta$")
ax[0, 2].plot(scales / scales[0], label=r"$\lambda$")
ax[0, 2].plot(locs / locs[0], label=r"$\theta$")
ax[0, 2].set_xticks([0, 1, 2, 3])
ax[0, 2].set_xticklabels(["10min", "3h", "6h", "day"])


cs = np.load("data/weibull_params/3_param_instantaneous/cs_fichtelberg.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/scales_fichtelberg.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/locs_fichtelberg.npy")

ax[1, 3].plot(cs  / cs[0], label=r"$\beta$")
ax[1, 3].plot(scales  / scales[0], label=r"$\lambda$")
ax[1, 3].plot(locs  / locs[0], label=r"$\theta$")
ax[1, 3].set_xticks([0, 1, 2, 3])
ax[1, 3].set_xticklabels(["10min", "3h", "6h", "day"])
ax[1, 3].legend()

ax[0, 0].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[0, 1].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[0, 2].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[0, 3].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[1, 0].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[1, 1].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[1, 2].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[1, 3].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))

fig.supxlabel(r"Resolution")
fig.supylabel(r"Parameter value")
fig.delaxes(ax[0, 3])
plt.savefig(savepath)

"""
savepath = "plots_eps/appendix/weibull_param_trend_3param_heights_instantaneous_abs.eps"

fig, ax = plt.subplots(2, 3, sharex="col", figsize=(8.27, 4), constrained_layout=True)
cs = np.load("data/weibull_params/3_param_instantaneous/10m/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/10m/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/10m/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 0].plot(cs, label=r"$\beta$")
ax[0, 0].plot(scales, label=r"$\lambda$")
ax[0, 0].plot(locs, label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2, 3])
ax[0, 0].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/41m/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/41m/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/41m/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 1].plot(cs, label=r"$\beta$")
ax[0, 1].plot(scales, label=r"$\lambda$")
ax[0, 1].plot(locs, label=r"$\theta$")
ax[0, 1].set_xticks([0, 1, 2, 3])
ax[0, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/130m/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/130m/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/130m/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0, 2].plot(cs, label=r"$\beta$")
ax[0, 2].plot(scales, label=r"$\lambda$")
ax[0, 2].plot(locs, label=r"$\theta$")
ax[0, 2].set_xticks([0, 1, 2, 3])
ax[0, 2].set_xticklabels(["10min", "3h", "6h", "day"])


cs = np.load("data/weibull_params/3_param_instantaneous/21m/cs_owez.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/21m/scales_owez.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/21m/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 0].plot(cs, label=r"$\beta$")
ax[1, 0].plot(scales, label=r"$\lambda$")
ax[1, 0].plot(locs, label=r"$\theta$")
ax[1, 0].set_xticks([0, 1, 2, 3])
ax[1, 0].set_xticklabels(["10min", "3h", "6h", "day"])
ax[1, 0].legend(loc="center left")

cs = np.load("data/weibull_params/3_param_instantaneous/70m/cs_owez.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/70m/scales_owez.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/70m/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 1].plot(cs, label=r"$\beta$")
ax[1, 1].plot(scales, label=r"$\lambda$")
ax[1, 1].plot(locs, label=r"$\theta$")
ax[1, 1].set_xticks([0, 1, 2, 3])
ax[1, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/116m/cs_owez.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/116m/scales_owez.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/116m/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1, 2].plot(cs, label=r"$\beta$")
ax[1, 2].plot(scales, label=r"$\lambda$")
ax[1, 2].plot(locs, label=r"$\theta$")
ax[1, 2].set_xticks([0, 1, 2, 3])
ax[1, 2].set_xticklabels(["10min", "3h", "6h", "day"])

custom_ylim = (-1, 11.5)
plt.setp(ax, ylim=custom_ylim)

ax[0, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))

ax[0, 0].text(0.03, 0.9, "(c)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.9, "(c)", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.9, "(c)", transform=ax[0, 2].transAxes)

ax[1, 0].text(0.03, 0.9, "(d)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.9, "(d)", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.9, "(d)", transform=ax[1, 2].transAxes)

fig.supxlabel(r"Resolution")
fig.supylabel(r"Parameter value")
plt.savefig(savepath)
plt.show()
