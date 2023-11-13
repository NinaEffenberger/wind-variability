"""
Generate KDEs including monthly averages.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter

from tueplots import fonts

import matplotlib
import matplotlib.pyplot as plt


matplotlib.rcParams.update({"font.size": 14})
matplotlib.rcParams.update({"axes.labelsize": 14})
matplotlib.rcParams.update({"legend.fontsize": 14})
matplotlib.rcParams.update({"xtick.labelsize": 14})
matplotlib.rcParams.update({"ytick.labelsize": 14})
matplotlib.rcParams.update({"axes.titlesize": 14})
plt.rcParams.update(fonts.neurips2021())

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#CC79A7", "#D55E00"]
)
fig, ax = plt.subplots(2, 4, sharex=True, sharey=True, figsize=(6, 4), constrained_layout=True)

# load data
average_daily = np.load("wind-variability/data/Pickles/Kelmarsh/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Kelmarsh/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Kelmarsh/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Kelmarsh/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

s = pd.Series(average_monthly)
u = pd.Series(np.array(average_three_hourly).flatten())
p = pd.Series(np.array(average_six_hourly).flatten())
w = pd.Series(average_daily)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[0, 0], data=r, label="10min", linewidth=1)
sns.kdeplot(ax=ax[0, 0], data=u, label="3h", linewidth=1)
sns.kdeplot(ax=ax[0, 0], data=p, label="6h", linewidth=1)
sns.kdeplot(ax=ax[0, 0], data=w, label="day", linewidth=1)
sns.kdeplot(ax=ax[0, 0], data=s, label="month", linewidth=1)


# load data
average_daily = np.load("wind-variability/data/Pickles/Penmanshiel/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Penmanshiel/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Penmanshiel/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Penmanshiel/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)


s = pd.Series(average_monthly)
u = pd.Series(np.array(average_three_hourly).flatten())
p = pd.Series(np.array(average_six_hourly).flatten())
w = pd.Series(average_daily)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[0, 1], data=r, linewidth=1)
sns.kdeplot(ax=ax[0, 1], data=u, linewidth=1)
sns.kdeplot(ax=ax[0, 1], data=p, linewidth=1)
sns.kdeplot(ax=ax[0, 1], data=w, linewidth=1)
sns.kdeplot(ax=ax[0, 1], data=s, linewidth=1)

# load data
average_daily = np.load("wind-variability/data/Pickles/NWTC/average_daily.npy")
average_10min = np.load("wind-variability/data/Pickles/NWTC/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/NWTC/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

s = pd.Series(average_monthly)
u = pd.Series(np.array(average_three_hourly).flatten())
p = pd.Series(np.array(average_six_hourly).flatten())
w = pd.Series(average_daily)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[0, 2], data=r, linewidth=1)
sns.kdeplot(ax=ax[0, 2], data=u, linewidth=1)
sns.kdeplot(ax=ax[0, 2], data=p, linewidth=1)
sns.kdeplot(ax=ax[0, 2], data=w, linewidth=1)
sns.kdeplot(ax=ax[0, 2], data=s, linewidth=1)

# load data
average_daily = np.load("wind-variability/data/Pickles/Owez/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Owez/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Owez/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Owez/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

s = pd.Series(average_monthly)
u = pd.Series(np.array(average_three_hourly).flatten())
p = pd.Series(np.array(average_six_hourly).flatten())
w = pd.Series(average_daily)
t = pd.Series(average_hourly)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[0, 3], data=r, linewidth=1)
sns.kdeplot(ax=ax[0, 3], data=u, linewidth=1)
sns.kdeplot(ax=ax[0, 3], data=p, linewidth=1)
sns.kdeplot(ax=ax[0, 3], data=w, linewidth=1)
sns.kdeplot(ax=ax[0, 3], data=s, linewidth=1)

# load data
average_daily = np.load("wind-variability/data/Pickles/Aachen/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Aachen/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Aachen/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Aachen/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

s = pd.Series(average_monthly)
u = pd.Series(np.array(average_three_hourly).flatten())
p = pd.Series(np.array(average_six_hourly).flatten())
w = pd.Series(average_daily)
t = pd.Series(average_hourly)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[1, 0], data=r, linewidth=1)
sns.kdeplot(ax=ax[1, 0], data=u, linewidth=1)
sns.kdeplot(ax=ax[1, 0], data=p, linewidth=1)
sns.kdeplot(ax=ax[1, 0], data=w, linewidth=1)
sns.kdeplot(ax=ax[1, 0], data=s, linewidth=1)

# load data
average_daily = np.load("wind-variability/data/Pickles/Zugspitze/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Zugspitze/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Zugspitze/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Zugspitze/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

s = pd.Series(average_monthly)
u = pd.Series(np.array(average_three_hourly).flatten())
p = pd.Series(np.array(average_six_hourly).flatten())
w = pd.Series(average_daily)
t = pd.Series(average_hourly)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[1, 1], data=r, linewidth=1)
sns.kdeplot(ax=ax[1, 1], data=u, linewidth=1)
sns.kdeplot(ax=ax[1, 1], data=p, linewidth=1)
sns.kdeplot(ax=ax[1, 1], data=w, linewidth=1)
sns.kdeplot(ax=ax[1, 1], data=s, linewidth=1)

# load data
average_daily = np.load("wind-variability/data/Pickles/Boltenhagen/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Boltenhagen/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Boltenhagen/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Boltenhagen/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

s = pd.Series(average_monthly)
u = pd.Series(np.array(average_three_hourly).flatten())
p = pd.Series(np.array(average_six_hourly).flatten())
w = pd.Series(average_daily)
t = pd.Series(average_hourly)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[1, 2], data=r, linewidth=1)
sns.kdeplot(ax=ax[1, 2], data=u, linewidth=1)
sns.kdeplot(ax=ax[1, 2], data=p, linewidth=1)
sns.kdeplot(ax=ax[1, 2], data=w, linewidth=1)
sns.kdeplot(ax=ax[1, 2], data=s, linewidth=1)


# load data
average_daily = np.load("wind-variability/data/Pickles/Fichtelberg/average_daily.npy")
average_hourly = np.load("wind-variability/data/Pickles/Fichtelberg/average_hourly.npy")
average_10min = np.load("wind-variability/data/Pickles/Fichtelberg/average_10min.npy")
average_monthly = np.load("wind-variability/data/Pickles/Fichtelberg/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

s = pd.Series(average_monthly)
u = pd.Series(np.array(average_three_hourly).flatten())
p = pd.Series(np.array(average_six_hourly).flatten())
w = pd.Series(average_daily)
t = pd.Series(average_hourly)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[1, 3], data=r, linewidth=1)
sns.kdeplot(ax=ax[1, 3], data=u, linewidth=1)
sns.kdeplot(ax=ax[1, 3], data=p, linewidth=1)
sns.kdeplot(ax=ax[1, 3], data=w, linewidth=1)
sns.kdeplot(ax=ax[1, 3], data=s, linewidth=1)

plt.xlim([-2, 27])

ax[0, 0].text(0.03, 0.9, "(a)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.9, "(b)", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.9, "(c)", transform=ax[0, 2].transAxes)
ax[0, 3].text(0.03, 0.9, "(d)", transform=ax[0, 3].transAxes)
ax[1, 0].text(0.03, 0.9, "(e)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.9, "(f)", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.9, "(g)", transform=ax[1, 2].transAxes)
ax[1, 3].text(0.03, 0.9, "(h)", transform=ax[1, 3].transAxes)

ax[0, 0].set(xlabel=None, ylabel=None)
ax[0, 1].set(xlabel=None, ylabel=None)
ax[0, 2].set(xlabel=None, ylabel=None)
ax[0, 3].set(xlabel=None, ylabel=None)
ax[1, 0].set(xlabel=None, ylabel=None)
ax[1, 1].set(xlabel=None, ylabel=None)
ax[1, 2].set(xlabel=None, ylabel=None)
ax[1, 3].set(xlabel=None, ylabel=None)

ax[0, 0].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[0, 1].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[0, 2].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[0, 3].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[1, 0].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[1, 1].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[1, 2].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[1, 3].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))

# the legend is created for each graphical element that has a "label"
fig.legend(loc="outside right center")

fig.supxlabel(r"Wind speed ($\frac{m}{s}$)")
fig.supylabel(r"Density")
plt.savefig("wind-variability/plots_eps/appendix/KDE_plusmonth.pdf")
plt.show()