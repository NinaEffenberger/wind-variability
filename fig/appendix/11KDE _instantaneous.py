"""
Generate KDEs for instantaneous data.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#CC79A7", "#D55E00"]
)
fig, ax = plt.subplots(2, 4, sharex=True, figsize=(8.27, 4), constrained_layout=True)


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
sns.kdeplot(ax=ax[0, 0], data=r, label="10min", linewidth=1)
sns.kdeplot(ax=ax[0, 0], data=u, label="3h", linewidth=1)
sns.kdeplot(ax=ax[0, 0], data=p, label="6h", linewidth=1)
sns.kdeplot(ax=ax[0, 0], data=w, label="day", linewidth=1)


# load data
average_10min = np.load("data/Pickles/Penmanshiel/average_10min.npy")
day = np.load("data/Pickles/Penmanshiel/day.npy")
six_hour = np.load("data/Pickles/Penmanshiel/six_hour.npy")
three_hour = np.load("data/Pickles/Penmanshiel/three_hour.npy")
hour = np.load("data/Pickles/Penmanshiel/hour.npy")

u = pd.Series(np.array(three_hour).flatten())
p = pd.Series(np.array(six_hour).flatten())
w = pd.Series(day)
t = pd.Series(hour)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[0, 1], data=r, linewidth=1)
sns.kdeplot(ax=ax[0, 1], data=u, linewidth=1)
sns.kdeplot(ax=ax[0, 1], data=p, linewidth=1)
sns.kdeplot(ax=ax[0, 1], data=w, linewidth=1)

# load data
average_10min = np.load("data/Pickles/NWTC/average_10min.npy")
day = np.load("data/Pickles/NWTC/day.npy")
six_hour = np.load("data/Pickles/NWTC/six_hour.npy")
three_hour = np.load("data/Pickles/NWTC/three_hour.npy")
hour = np.load("data/Pickles/NWTC/hour.npy")

u = pd.Series(np.array(three_hour).flatten())
p = pd.Series(np.array(six_hour).flatten())
w = pd.Series(day)
t = pd.Series(hour)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[0, 2], data=r, linewidth=1)
sns.kdeplot(ax=ax[0, 2], data=u, linewidth=1)
sns.kdeplot(ax=ax[0, 2], data=p, linewidth=1)
sns.kdeplot(ax=ax[0, 2], data=w, linewidth=1)

# load data
average_10min = np.load("data/Pickles/Owez/average_10min.npy")
day = np.load("data/Pickles/Owez/day.npy")
six_hour = np.load("data/Pickles/Owez/six_hour.npy")
three_hour = np.load("data/Pickles/Owez/three_hour.npy")
hour = np.load("data/Pickles/Owez/hour.npy")

u = pd.Series(np.array(three_hour).flatten())
p = pd.Series(np.array(six_hour).flatten())
w = pd.Series(day)
t = pd.Series(hour)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[0, 3], data=r, linewidth=1)
sns.kdeplot(ax=ax[0, 3], data=u, linewidth=1)
sns.kdeplot(ax=ax[0, 3], data=p, linewidth=1)
sns.kdeplot(ax=ax[0, 3], data=w, linewidth=1)

# load data
average_10min = np.load("data/Pickles/Aachen/average_10min.npy")
day = np.load("data/Pickles/Aachen/day.npy")
six_hour = np.load("data/Pickles/Aachen/six_hour.npy")
three_hour = np.load("data/Pickles/Aachen/three_hour.npy")
hour = np.load("data/Pickles/Aachen/hour.npy")

u = pd.Series(np.array(three_hour).flatten())
p = pd.Series(np.array(six_hour).flatten())
w = pd.Series(day)
t = pd.Series(hour)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[1, 0], data=r, linewidth=1)
sns.kdeplot(ax=ax[1, 0], data=u, linewidth=1)
sns.kdeplot(ax=ax[1, 0], data=p, linewidth=1)
sns.kdeplot(ax=ax[1, 0], data=w, linewidth=1)

# load data
average_10min = np.load("data/Pickles/Zugspitze/average_10min.npy")
day = np.load("data/Pickles/Zugspitze/day.npy")
six_hour = np.load("data/Pickles/Zugspitze/six_hour.npy")
three_hour = np.load("data/Pickles/Zugspitze/three_hour.npy")
hour = np.load("data/Pickles/Zugspitze/hour.npy")

u = pd.Series(np.array(three_hour).flatten())
p = pd.Series(np.array(six_hour).flatten())
w = pd.Series(day)
t = pd.Series(hour)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[1, 1], data=r, linewidth=1)
sns.kdeplot(ax=ax[1, 1], data=u, linewidth=1)
sns.kdeplot(ax=ax[1, 1], data=p, linewidth=1)
sns.kdeplot(ax=ax[1, 1], data=w, linewidth=1)

# load data
average_10min = np.load("data/Pickles/Boltenhagen/average_10min.npy")
day = np.load("data/Pickles/Boltenhagen/day.npy")
six_hour = np.load("data/Pickles/Boltenhagen/six_hour.npy")
three_hour = np.load("data/Pickles/Boltenhagen/three_hour.npy")
hour = np.load("data/Pickles/Boltenhagen/hour.npy")

u = pd.Series(np.array(three_hour).flatten())
p = pd.Series(np.array(six_hour).flatten())
w = pd.Series(day)
t = pd.Series(hour)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[1, 2], data=r, linewidth=1)
sns.kdeplot(ax=ax[1, 2], data=u, linewidth=1)
sns.kdeplot(ax=ax[1, 2], data=p, linewidth=1)
sns.kdeplot(ax=ax[1, 2], data=w, linewidth=1)

# load data
average_10min = np.load("data/Pickles/Fichtelberg/average_10min.npy")
day = np.load("data/Pickles/Fichtelberg/day.npy")
six_hour = np.load("data/Pickles/Fichtelberg/six_hour.npy")
three_hour = np.load("data/Pickles/Fichtelberg/three_hour.npy")
hour = np.load("data/Pickles/Fichtelberg/hour.npy")

u = pd.Series(np.array(three_hour).flatten())
p = pd.Series(np.array(six_hour).flatten())
w = pd.Series(day)
t = pd.Series(hour)
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[1, 3], data=r, linewidth=1)
sns.kdeplot(ax=ax[1, 3], data=u, linewidth=1)
sns.kdeplot(ax=ax[1, 3], data=p, linewidth=1)
sns.kdeplot(ax=ax[1, 3], data=w, linewidth=1)
plt.xlim([-2, 25])

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

fig.supxlabel(r"Wind speed ($\frac{m}{s}$)")
fig.supylabel(r"Density")
fig.legend(loc="outside right center")

plt.savefig("plots_eps/appendix/KDE_instantaneous.eps")
