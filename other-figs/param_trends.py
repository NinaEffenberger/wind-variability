import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams.update({"font.size": 12})
savepath = "other-figs/weibull_avrg_inst_abs.eps"
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)

fig, ax = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(6, 6), layout="constrained")
cs = np.load("data/weibull_params/3_param/cs_kelmarsh.npy")
scales = np.load("data/weibull_params/3_param/scales_kelmarsh.npy")
locs = np.load("data/weibull_params/3_param/locs_kelmarsh.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)
ax[0, 1].plot(cs[:-1], label=r"$\beta$")
ax[0, 1].plot(scales[:-1], label=r"$\lambda$")
ax[0, 1].plot(locs[:-1], label=r"$\theta$")
ax[0, 1].set_xticks([0, 1, 2, 3])
ax[0, 1].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_penmanshiel.npy")
scales = np.load("data/weibull_params/3_param/scales_penmanshiel.npy")
locs = np.load("data/weibull_params/3_param/locs_penmanshiel.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)
ax[1, 1].plot(cs[:-1])
ax[1, 1].plot(scales[:-1])
ax[1, 1].plot(locs[:-1])
ax[1, 1].set_xticks([0, 1, 2, 3])
ax[1, 1].set_xticklabels(["10min", "3h", "6h", "day"])


cs = np.load("data/weibull_params/3_param_instantaneous/cs_kelmarsh.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/scales_kelmarsh.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/locs_kelmarsh.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)
ax[0, 0].plot(cs)
ax[0, 0].plot(scales)
ax[0, 0].plot(locs)
ax[0, 0].set_xticks([0, 1, 2, 3])
ax[0, 0].set_xticklabels(["10min", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/cs_penmanshiel.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/scales_penmanshiel.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/locs_penmanshiel.npy")
cs = np.delete(cs, 1, axis=0)
scales = np.delete(scales, 1, axis=0)
locs = np.delete(locs, 1, axis=0)
ax[1, 0].plot(cs)
ax[1, 0].plot(scales)
ax[1, 0].plot(locs)
ax[1, 0].set_xticks([0, 1, 2, 3])
ax[1, 0].set_xticklabels(["10min", "3h", "6h", "day"])


custom_ylim = (-1, 15)

ax[0, 0].text(0, 13.5, "(a)")
ax[1, 0].text(0, 13.5, "(b)")
ax[0, 1].text(0, 13.5, "(a)")
ax[1, 1].text(0, 13.5, "(b)")

# Setting the values for all axes.
plt.setp(ax, ylim=custom_ylim)
fig.supxlabel("Resolution")
fig.supylabel("Fitted parameter")
fig.legend(loc="outside right center")

cols = ["instantaneous", "average"]
for c, ax in zip(cols, ax[0]):
    ax.set_title(c, size="large")
plt.savefig(savepath)
plt.show()