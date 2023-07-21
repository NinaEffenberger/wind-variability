import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter

plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#E69F00", "#56B4E9", "#009E73", "#CC79A7", "#D55E00"])
fig, ax = plt.subplots(1, 2, sharey=True, figsize=(8.4, 4), constrained_layout=True)


# load data
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
day = np.load("data/Pickles/Kelmarsh/day.npy")
six_hour = np.load("data/Pickles/Kelmarsh/six_hour.npy")
three_hour = np.load("data/Pickles/Kelmarsh/three_hour.npy")
hour = np.load("data/Pickles/Kelmarsh/hour.npy")

u = pd.Series(np.array(three_hour).flatten())
p = pd.Series(np.array(six_hour).flatten())
w = pd.Series(day)
t = pd.Series(hour)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[0], data=r, label="10min", linewidth=1)
sns.kdeplot(ax=ax[0], data=u, label="3h", linewidth=1)
sns.kdeplot(ax=ax[0], data=p, label="6h", linewidth=1)
sns.kdeplot(ax=ax[0], data=w, label="day", linewidth=1)

average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
day = np.load("data/Pickles/Kelmarsh/average_daily.npy")
average_hourly = np.load("data/Pickles/Kelmarsh/average_hourly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

u = pd.Series(np.array(average_three_hourly).flatten())
p = pd.Series(np.array(average_six_hourly).flatten())
w = pd.Series(day)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[1], data=r, linewidth=1)
sns.kdeplot(ax=ax[1], data=u, linewidth=1)
sns.kdeplot(ax=ax[1], data=p, linewidth=1)
sns.kdeplot(ax=ax[1], data=w, linewidth=1)

cols = ["instantaneous", "average"]
for c, ax in zip(cols, ax):
    ax.set_title(c, size="large")

fig.supxlabel(r"Wind speed ($\frac{m}{s}$)")
fig.legend(loc="outside right center")
plt.savefig("other-figs/KDE_abs_inst.eps")
plt.show()
