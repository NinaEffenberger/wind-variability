import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from kolmogorov_smirnov import kolmogorov_smirnov_plot, kolmogorov_smirnov_stat, prepare_dataframe

matplotlib.rcParams.update({"font.size": 12})

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#CC79A7", "#D55E00"]
)
# load data
average_daily = np.load("data/Pickles/Kelmarsh/average_daily.npy")
average_hourly = np.load("data/Pickles/Kelmarsh/average_hourly.npy")
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
average_monthly = np.load("data/Pickles/Kelmarsh/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)
data = prepare_dataframe(average_daily, average_10min)

k, ks_stat, y = kolmogorov_smirnov_stat(data)

fig, ax = plt.subplots(1, 1, figsize=(4.4, 4), constrained_layout=True)
ax.plot("windspeeds", "dist1", data=data, label="day")
ax.plot("windspeeds", "dist2", data=data, label="10min")
ax.errorbar(x=data["windspeeds"][k], y=y, yerr=ks_stat / 2, color="black", capsize=5, mew=3)
ax.legend()
ax.set_xlabel(r"$\frac{m}{s}$")
ax.set_ylabel(r"cumulative density")
plt.savefig("other-figs/kolmogorov.eps")
plt.show()
