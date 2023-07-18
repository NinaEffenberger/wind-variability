import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#CC79A7", "#D55E00"]
)
fig, ax = plt.subplots(2, 2, sharex=True, figsize=(4.4, 4), constrained_layout=True)


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
sns.kdeplot(ax=ax[0, 0], data=t, label="1h", linewidth=1)
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
sns.kdeplot(ax=ax[0, 1], data=t, linewidth=1)
sns.kdeplot(ax=ax[0, 1], data=u, linewidth=1)
sns.kdeplot(ax=ax[0, 1], data=p, linewidth=1)
sns.kdeplot(ax=ax[0, 1], data=w, linewidth=1)


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
sns.kdeplot(ax=ax[1, 0], data=t, linewidth=1)
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
sns.kdeplot(ax=ax[1, 1], data=t, linewidth=1)
sns.kdeplot(ax=ax[1, 1], data=u, linewidth=1)
sns.kdeplot(ax=ax[1, 1], data=p, linewidth=1)
sns.kdeplot(ax=ax[1, 1], data=w, linewidth=1)


plt.xlim([-2, 25])

ax[0, 0].text(0.03, 0.9, "1)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.9, "2)", transform=ax[0, 1].transAxes)
ax[1, 0].text(0.03, 0.9, "3)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.9, "4)", transform=ax[1, 1].transAxes)

ax[0, 0].set(xlabel=None, ylabel=None)
ax[0, 1].set(xlabel=None, ylabel=None)
ax[1, 0].set(xlabel=None, ylabel=None)
ax[1, 1].set(xlabel=None, ylabel=None)

ax[0, 0].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[0, 1].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[1, 0].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
ax[1, 1].yaxis.set_major_formatter(FormatStrFormatter("%.1f"))

fig.supxlabel(r"Wind speed ($\frac{m}{s}$)")
fig.supylabel(r"Density")
fig.legend(loc="outside right center")
plt.savefig("other-figs/KDE_instantaneous.eps")
plt.show()
