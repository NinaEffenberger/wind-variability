import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)
# load data
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
days = np.load("data/Pickles/Kelmarsh/days.npy", allow_pickle=True)

average_10min = average_10min[0 : 144 * 20]
days = days[0 : 144 * 20]

fig, ax = plt.subplots(2, 2, sharey=True, constrained_layout=True, figsize=(6, 4))
ax[0, 0].plot(average_10min)
ax[0, 1].plot(average_10min[::18])
ax[1, 0].plot(average_10min[::32])
ax[1, 1].plot(average_10min[::144])
ax[0, 0].set_xticklabels(["Day 1", "Day 10", "Day 20"])
ax[0, 1].set_xticklabels(["Day 1", "Day 10", "Day 20"])
ax[1, 0].set_xticklabels(["Day 1", "Day 10", "Day 20"])
ax[1, 1].set_xticklabels(["Day 1", "Day 10", "Day 20"])

ax[0, 0].set_xticks([0, 144 * 10, 144 * 20])
ax[0, 1].set_xticks([0, 8 * 10, 8 * 20])
ax[1, 0].set_xticks([0, 4 * 10, 4 * 20])
ax[1, 1].set_xticks([0, 10, 20])

plt.savefig("temporal_downscaling2.svg")
plt.show()
