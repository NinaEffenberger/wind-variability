"""
Generate plot that shows evolvement of Weibull parameters when data is averaged.
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from tueplots import fonts

matplotlib.rcParams.update({"font.size": 13})
matplotlib.rcParams.update({"axes.labelsize": 14})
matplotlib.rcParams.update({"legend.fontsize": 14})
matplotlib.rcParams.update({"xtick.labelsize": 14})
matplotlib.rcParams.update({"ytick.labelsize": 14})
matplotlib.rcParams.update({"axes.titlesize": 14})
plt.rcParams.update(fonts.neurips2021())

savepath = "wind-variability/plots_eps/weibull_avrg_inst_abs.pdf"
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73","#E69F00", "#56B4E9", "#009E73"]
)

fig, ax = plt.subplots(1, 4, sharex=True, sharey=True, figsize=(6, 2.5), layout="constrained")
cs = np.load("wind-variability/data/weibull_params/3_param/cs_kelmarsh.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_kelmarsh.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_kelmarsh.npy")

cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0].plot(cs[:-1], linestyle="dashed")
ax[0].plot(scales[:-1], linestyle="dashed")
ax[0].plot(locs[:-1], linestyle="dashed")
ax[0].set_xticks([0, 1, 2, 3])
ax[0].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_penmanshiel.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_penmanshiel.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_penmanshiel.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1].plot(cs[:-1], linestyle="dashed")
ax[1].plot(scales[:-1], linestyle="dashed")
ax[1].plot(locs[:-1], linestyle="dashed")
ax[1].set_xticks([0, 1, 2, 3])
ax[1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_nwtc5.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_nwtc5.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[2].plot(cs[:-1], linestyle="dashed")
ax[2].plot(scales[:-1], linestyle="dashed")
ax[2].plot(locs[:-1], linestyle="dashed")
ax[2].set_xticks([0, 1, 2, 3])
ax[2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param/cs_owez.npy")
scales = np.load("wind-variability/data/weibull_params/3_param/scales_owez.npy")
locs = np.load("wind-variability/data/weibull_params/3_param/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[3].plot(cs[:-1], linestyle="dashed")
ax[3].plot(scales[:-1], linestyle="dashed")
ax[3].plot(locs[:-1], linestyle="dashed")
ax[3].set_xticks([0, 1, 2, 3])
ax[3].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param_instantaneous/cs_kelmarsh.npy")
scales = np.load("wind-variability/data/weibull_params/3_param_instantaneous/scales_kelmarsh.npy")
locs = np.load("wind-variability/data/weibull_params/3_param_instantaneous/locs_kelmarsh.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[0].plot(cs)
ax[0].plot(scales)
ax[0].plot(locs)
ax[0].set_xticks([0, 1, 2, 3])
ax[0].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param_instantaneous/cs_penmanshiel.npy")
scales = np.load("wind-variability/data/weibull_params/3_param_instantaneous/scales_penmanshiel.npy")
locs = np.load("wind-variability/data/weibull_params/3_param_instantaneous/locs_penmanshiel.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[1].plot(cs, label=r"$\beta$")
ax[1].plot(scales, label=r"$\lambda$")
ax[1].plot(locs, label=r"$\theta$")
ax[1].set_xticks([0, 1, 2, 3])
ax[1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param_instantaneous/cs_nwtc5.npy")
scales = np.load("wind-variability/data/weibull_params/3_param_instantaneous/scales_nwtc5.npy")
locs = np.load("wind-variability/data/weibull_params/3_param_instantaneous/locs_nwtc5.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[2].plot(cs)
ax[2].plot(scales)
ax[2].plot(locs)
ax[2].set_xticks([0, 1, 2, 3])
ax[2].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("wind-variability/data/weibull_params/3_param_instantaneous/cs_owez.npy")
scales = np.load("wind-variability/data/weibull_params/3_param_instantaneous/scales_owez.npy")
locs = np.load("wind-variability/data/weibull_params/3_param_instantaneous/locs_owez.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)

ax[3].plot(cs)
ax[3].plot(scales)
ax[3].plot(locs)
ax[3].set_xticks([0, 1, 2, 3])
ax[3].set_xticklabels(["10min", "3h", "6h", "day"])

custom_ylim = (-1, 16)
"""
ax[0, 0].text(0, 13.5, "(1a)")
ax[1, 0].text(0, 13.5, "(2a)")
ax[0, 2].text(0, 13.5, "(3a)")
ax[0, 3].text(0, 13.5, "(4a)")
ax[1, 0].text(0, 13.5, "(1b)")
ax[1, 1].text(0, 13.5, "(2b)")
ax[1, 2].text(0, 13.5, "(3b)")
ax[1, 3].text(0, 13.5, "(4b)")
"""
ax[0].text(0.03, 0.9, "Kelmarsh", transform=ax[0].transAxes)
ax[1].text(0.03, 0.9, "Penmanshiel", transform=ax[1].transAxes)
ax[2].text(0.03, 0.9, "Owez", transform=ax[2].transAxes)
ax[3].text(0.03, 0.9, "NWTC", transform=ax[3].transAxes)



plt.setp(ax[0].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[0].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[2].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[3].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[1].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[2].get_xticklabels(), rotation=90, ha="center")
plt.setp(ax[3].get_xticklabels(), rotation=90, ha="center")

# Setting the values for all axes.
plt.setp(ax, ylim=custom_ylim)
fig.supxlabel("Resolution")
fig.supylabel("Fitted parameter")
fig.legend(loc="outside right center")
plt.savefig(savepath)
plt.show()
