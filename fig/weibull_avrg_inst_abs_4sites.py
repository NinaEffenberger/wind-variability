import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams.update({"font.size": 12})
savepath = "plots_eps/weibull_avrg_inst_abs.eps"
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)

fig, ax = plt.subplots(4, 2, sharex=True, sharey=True, figsize=(6, 6), layout="constrained")
cs = np.load("data/weibull_params/3_param/cs_kelmarsh.npy")
scales = np.load("data/weibull_params/3_param/scales_kelmarsh.npy")
locs = np.load("data/weibull_params/3_param/locs_kelmarsh.npy")

ax[0, 0].plot(cs[:-1], label=r"$\beta$")
ax[0, 0].plot(scales[:-1], label=r"$\lambda$")
ax[0, 0].plot(locs[:-1], label=r"$\theta$")
ax[0, 0].set_xticks([0, 1, 2, 3, 4])
ax[0, 0].set_xticklabels(["10min", "hour", "3h", "6h", "day"])
ax[0, 0].legend(loc="upper right")

cs = np.load("data/weibull_params/3_param/cs_penmanshiel.npy")
scales = np.load("data/weibull_params/3_param/scales_penmanshiel.npy")
locs = np.load("data/weibull_params/3_param/locs_penmanshiel.npy")

ax[1, 0].plot(cs[:-1], label=r"$\beta$")
ax[1, 0].plot(scales[:-1], label=r"$\lambda$")
ax[1, 0].plot(locs[:-1], label=r"$\theta$")
ax[1, 0].set_xticks([0, 1, 2, 3, 4])
ax[1, 0].set_xticklabels(["10min", "hour", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param/locs_nwtc5.npy")

ax[2, 0].plot(cs[:-1], label=r"$\beta$")
ax[2, 0].plot(scales[:-1], label=r"$\lambda$")
ax[2, 0].plot(locs[:-1], label=r"$\theta$")
ax[2, 0].set_xticks([0, 1, 2, 3, 4])
ax[2, 0].set_xticklabels(["10min", "hour", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param/cs_owez.npy")
scales = np.load("data/weibull_params/3_param/scales_owez.npy")
locs = np.load("data/weibull_params/3_param/locs_owez.npy")

ax[3, 0].plot(cs[:-1], label=r"$\beta$")
ax[3, 0].plot(scales[:-1], label=r"$\lambda$")
ax[3, 0].plot(locs[:-1], label=r"$\theta$")
ax[3, 0].set_xticks([0, 1, 2, 3, 4])
ax[3, 0].set_xticklabels(["10min", "hour", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/cs_kelmarsh.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/scales_kelmarsh.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/locs_kelmarsh.npy")

ax[0, 1].plot(cs, label=r"$\beta$")
ax[0, 1].plot(scales, label=r"$\lambda$")
ax[0, 1].plot(locs, label=r"$\theta$")
ax[0, 1].set_xticks([0, 1, 2, 3, 4])
ax[0, 1].set_xticklabels(["10min", "hour", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/cs_penmanshiel.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/scales_penmanshiel.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/locs_penmanshiel.npy")

ax[1, 1].plot(cs, label=r"$\beta$")
ax[1, 1].plot(scales, label=r"$\lambda$")
ax[1, 1].plot(locs, label=r"$\theta$")
ax[1, 1].set_xticks([0, 1, 2, 3, 4])
ax[1, 1].set_xticklabels(["10min", "hour", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/cs_nwtc5.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/scales_nwtc5.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/locs_nwtc5.npy")

ax[2, 1].plot(cs, label=r"$\beta$")
ax[2, 1].plot(scales, label=r"$\lambda$")
ax[2, 1].plot(locs, label=r"$\theta$")
ax[2, 1].set_xticks([0, 1, 2, 3, 4])
ax[2, 1].set_xticklabels(["10min", "hour", "3h", "6h", "day"])

cs = np.load("data/weibull_params/3_param_instantaneous/cs_owez.npy")
scales = np.load("data/weibull_params/3_param_instantaneous/scales_owez.npy")
locs = np.load("data/weibull_params/3_param_instantaneous/locs_owez.npy")

ax[3, 1].plot(cs, label=r"$\beta$")
ax[3, 1].plot(scales, label=r"$\lambda$")
ax[3, 1].plot(locs, label=r"$\theta$")
ax[3, 1].set_xticks([0, 1, 2, 3, 4])
ax[3, 1].set_xticklabels(["10min", "hour", "3h", "6h", "day"])

custom_ylim = (-1, 16)

ax[0, 0].text(0, 13.5, "1a)")
ax[1, 0].text(0, 13.5, "2a)")
ax[2, 0].text(0, 13.5, "3a)")
ax[3, 0].text(0, 13.5, "4a)")
ax[0, 1].text(0, 13.5, "1b)")
ax[1, 1].text(0, 13.5, "2b)")
ax[2, 1].text(0, 13.5, "3b)")
ax[3, 1].text(0, 13.5, "4b)")

# Setting the values for all axes.
plt.setp(ax, ylim=custom_ylim)
fig.supxlabel("Resolution")
fig.supylabel("Fitted parameter")
plt.savefig(savepath)
plt.show()
