import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)

savepath = "plots_eps/appendix/weibull_param_trend_3param_3years.eps"

fig, ax = plt.subplots(2, 4, sharex=True, figsize=(8.27, 4), constrained_layout=True)

cs = np.load("data/weibull_params/first_three_years/cs_aachen.npy")
scales = np.load("data/weibull_params/first_three_years/scales_aachen.npy")
locs = np.load("data/weibull_params/first_three_years/locs_aachen.npy")

ax[0, 0].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[0, 0].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[0, 0].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2, 3, 4])
ax[0, 0].set_xticklabels(["10min", "1h", "3h", "6h", "day"])
ax[0, 0].legend(loc="upper center")

cs = np.load("data/weibull_params/first_three_years/cs_zugspitze.npy")
scales = np.load("data/weibull_params/first_three_years/scales_zugspitze.npy")
locs = np.load("data/weibull_params/first_three_years/locs_zugspitze.npy")

ax[0, 1].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[0, 1].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[0, 1].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[0, 1].set_xticks([0, 1, 2, 3, 4, 5])
ax[0, 1].set_xticklabels(["10min", "1h", "3h", "6h", "day", "month"])

cs = np.load("data/weibull_params/first_three_years/cs_boltenhagen.npy")
scales = np.load("data/weibull_params/first_three_years/scales_boltenhagen.npy")
locs = np.load("data/weibull_params/first_three_years/locs_boltenhagen.npy")

ax[0, 2].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[0, 2].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[0, 2].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[0, 2].set_xticks([0, 1, 2, 3, 4])
ax[0, 2].set_xticklabels(["10min", "1h", "3h", "6h", "day"])

cs = np.load("data/weibull_params/first_three_years/cs_fichtelberg.npy")
scales = np.load("data/weibull_params/first_three_years/scales_fichtelberg.npy")
locs = np.load("data/weibull_params/first_three_years/locs_fichtelberg.npy")

ax[0, 3].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[0, 3].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[0, 3].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[0, 3].set_xticks([0, 1, 2, 3, 4])
ax[0, 3].set_xticklabels(["10min", "1h", "3h", "6h", "day"])

cs = np.load("data/weibull_params/last_three_years/cs_aachen.npy")
scales = np.load("data/weibull_params/last_three_years/scales_aachen.npy")
locs = np.load("data/weibull_params/last_three_years/locs_aachen.npy")

ax[1, 0].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[1, 0].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[1, 0].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[1, 0].set_xticks([0, 1, 2, 3, 4])
ax[1, 0].set_xticklabels(["10min", "1h", "3h", "6h", "day"])

cs = np.load("data/weibull_params/last_three_years/cs_zugspitze.npy")
scales = np.load("data/weibull_params/last_three_years/scales_zugspitze.npy")
locs = np.load("data/weibull_params/last_three_years/locs_zugspitze.npy")

ax[1, 1].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[1, 1].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[1, 1].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[1, 1].set_xticks([0, 1, 2, 3, 4, 5])
ax[1, 1].set_xticklabels(["10min", "1h", "3h", "6h", "day", "month"])

cs = np.load("data/weibull_params/last_three_years/cs_boltenhagen.npy")
scales = np.load("data/weibull_params/last_three_years/scales_boltenhagen.npy")
locs = np.load("data/weibull_params/last_three_years/locs_boltenhagen.npy")

ax[1, 2].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[1, 2].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[1, 2].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[1, 2].set_xticks([0, 1, 2, 3, 4])
ax[1, 2].set_xticklabels(["10min", "1h", "3h", "6h", "day"])

cs = np.load("data/weibull_params/last_three_years/cs_fichtelberg.npy")
scales = np.load("data/weibull_params/last_three_years/scales_fichtelberg.npy")
locs = np.load("data/weibull_params/last_three_years/locs_fichtelberg.npy")

ax[1, 3].plot(cs[:-1] / cs[0], label=r"$\beta$")
ax[1, 3].plot(scales[:-1] / scales[0], label=r"$\lambda$")
ax[1, 3].plot(locs[:-1] / locs[0], label=r"$\theta$")
ax[1, 3].set_xticks([0, 1, 2, 3, 4])
ax[1, 3].set_xticklabels(["10min", "1h", "3h", "6h", "day"])

ax[0, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 3].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 3].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))

ax[0, 0].text(0.03, 0.9, "(5a)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.9, "(6a)", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.9, "(7a)", transform=ax[0, 2].transAxes)
ax[0, 3].text(0.03, 0.9, "(8a)", transform=ax[0, 3].transAxes)
ax[1, 0].text(0.03, 0.9, "(5b)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.9, "(6b)", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.9, "(7b)", transform=ax[1, 2].transAxes)
ax[1, 3].text(0.03, 0.9, "(8b)", transform=ax[1, 3].transAxes)

fig.supxlabel(r"Resolution")
fig.supylabel(r"Parameter value")
plt.savefig(savepath)

savepath = "plots_eps/appendix/weibull_param_trend_3param_3years_abs.eps"

fig, ax = plt.subplots(2, 4, sharex=True, figsize=(8.27, 4), constrained_layout=True)

cs = np.load("data/weibull_params/first_three_years/cs_aachen.npy")
scales = np.load("data/weibull_params/first_three_years/scales_aachen.npy")
locs = np.load("data/weibull_params/first_three_years/locs_aachen.npy")

ax[0, 0].plot(cs[:-1], label=r"$\beta$")
ax[0, 0].plot(scales[:-1], label=r"$\lambda$")
ax[0, 0].plot(locs[:-1], label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2, 3, 4])
ax[0, 0].set_xticklabels(["10min", "1h", "3h", "6h", "day"])
ax[0, 0].legend(loc="upper right")

cs = np.load("data/weibull_params/first_three_years/cs_zugspitze.npy")
scales = np.load("data/weibull_params/first_three_years/scales_zugspitze.npy")
locs = np.load("data/weibull_params/first_three_years/locs_zugspitze.npy")

ax[0, 1].plot(cs[:-1], label=r"$\beta$")
ax[0, 1].plot(scales[:-1], label=r"$\lambda$")
ax[0, 1].plot(locs[:-1], label=r"$\theta$")
ax[0, 1].set_xticks([0, 1, 2, 3, 4, 5])
ax[0, 1].set_xticklabels(["10min", "1h", "3h", "6h", "day", "month"])

cs = np.load("data/weibull_params/first_three_years/cs_boltenhagen.npy")
scales = np.load("data/weibull_params/first_three_years/scales_boltenhagen.npy")
locs = np.load("data/weibull_params/first_three_years/locs_boltenhagen.npy")

ax[0, 2].plot(cs[:-1], label=r"$\beta$")
ax[0, 2].plot(scales[:-1], label=r"$\lambda$")
ax[0, 2].plot(locs[:-1], label=r"$\theta$")
ax[0, 2].set_xticks([0, 1, 2, 3, 4])
ax[0, 2].set_xticklabels(["10min", "1h", "3h", "6h", "day"])

cs = np.load("data/weibull_params/first_three_years/cs_fichtelberg.npy")
scales = np.load("data/weibull_params/first_three_years/scales_fichtelberg.npy")
locs = np.load("data/weibull_params/first_three_years/locs_fichtelberg.npy")

ax[0, 3].plot(cs[:-1], label=r"$\beta$")
ax[0, 3].plot(scales[:-1], label=r"$\lambda$")
ax[0, 3].plot(locs[:-1], label=r"$\theta$")
ax[0, 3].set_xticks([0, 1, 2, 3, 4])
ax[0, 3].set_xticklabels(["10min", "1h", "3h", "6h", "day"])

cs = np.load("data/weibull_params/last_three_years/cs_aachen.npy")
scales = np.load("data/weibull_params/last_three_years/scales_aachen.npy")
locs = np.load("data/weibull_params/last_three_years/locs_aachen.npy")

ax[1, 0].plot(cs[:-1], label=r"$\beta$")
ax[1, 0].plot(scales[:-1], label=r"$\lambda$")
ax[1, 0].plot(locs[:-1], label=r"$\theta$")
ax[1, 0].set_xticks([0, 1, 2, 3, 4])
ax[1, 0].set_xticklabels(["10min", "1h", "3h", "6h", "day"])

cs = np.load("data/weibull_params/last_three_years/cs_zugspitze.npy")
scales = np.load("data/weibull_params/last_three_years/scales_zugspitze.npy")
locs = np.load("data/weibull_params/last_three_years/locs_zugspitze.npy")

ax[1, 1].plot(cs[:-1], label=r"$\beta$")
ax[1, 1].plot(scales[:-1], label=r"$\lambda$")
ax[1, 1].plot(locs[:-1], label=r"$\theta$")
ax[1, 1].set_xticks([0, 1, 2, 3, 4, 5])
ax[1, 1].set_xticklabels(["10min", "1h", "3h", "6h", "day", "month"])

cs = np.load("data/weibull_params/last_three_years/cs_boltenhagen.npy")
scales = np.load("data/weibull_params/last_three_years/scales_boltenhagen.npy")
locs = np.load("data/weibull_params/last_three_years/locs_boltenhagen.npy")

ax[1, 2].plot(cs[:-1], label=r"$\beta$")
ax[1, 2].plot(scales[:-1], label=r"$\lambda$")
ax[1, 2].plot(locs[:-1], label=r"$\theta$")
ax[1, 2].set_xticks([0, 1, 2, 3, 4])
ax[1, 2].set_xticklabels(["10min", "1h", "3h", "6h", "day"])

cs = np.load("data/weibull_params/last_three_years/cs_fichtelberg.npy")
scales = np.load("data/weibull_params/last_three_years/scales_fichtelberg.npy")
locs = np.load("data/weibull_params/last_three_years/locs_fichtelberg.npy")

ax[1, 3].plot(cs[:-1], label=r"$\beta$")
ax[1, 3].plot(scales[:-1], label=r"$\lambda$")
ax[1, 3].plot(locs[:-1], label=r"$\theta$")
ax[1, 3].set_xticks([0, 1, 2, 3, 4])
ax[1, 3].set_xticklabels(["10min", "1h", "3h", "6h", "day"])

custom_ylim = (-1, 12)
plt.setp(ax, ylim=custom_ylim)
plt.show()

ax[0, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[0, 3].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 0].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 1].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 2].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
ax[1, 3].yaxis.set_major_formatter(FormatStrFormatter("%.0f"))

ax[0, 0].text(0.03, 0.9, "(5a)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.9, "(6a)", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.9, "(7a)", transform=ax[0, 2].transAxes)
ax[0, 3].text(0.03, 0.9, "(8a)", transform=ax[0, 3].transAxes)
ax[1, 0].text(0.03, 0.9, "(5b)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.9, "(6b)", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.9, "(7b)", transform=ax[1, 2].transAxes)
ax[1, 3].text(0.03, 0.9, "(8b)", transform=ax[1, 3].transAxes)

fig.supxlabel(r"Resolution")
fig.supylabel(r"Parameter value")
plt.savefig(savepath)
plt.show()
