import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.rcParams.update({"font.size": 12})

savepath = "plots_eps/power_gen_diff_30yrs.eps"
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)
# load data
six_hourly_winds = np.load("data/power-gen/Aachen/six_hourly_avrg.npy")
three_hourly_winds = np.load("data/power-gen/Aachen/three_hourly_avrg.npy")
daily_winds = np.load("data/power-gen/Aachen/daily_avrg.npy")
ten_min_winds = np.load("data/power-gen/Aachen/ten_min.npy")
days = np.load("data/power-gen/Aachen/days.npy", allow_pickle=True)

fig, ax = plt.subplots(2, 4, sharex="col", figsize=(6, 4), sharey=True, constrained_layout=True)
print(((np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])

ax[0, 0].plot(
    days,
    (np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1],
    label="day",
    linewidth=1,
)
# ax[0, 0].plot(days, (np.cumsum(hourly_winds))/np.cumsum(ten_min_winds), label="hourly", linewidth=1)
ax[0, 0].plot(
    days,
    (np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    label="6h",
    linewidth=1,
)
ax[0, 0].plot(
    days,
    (np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    label="3h",
    linewidth=1,
)
ax[0, 0].plot(
    days,
    (np.cumsum(ten_min_winds)) / np.cumsum(ten_min_winds)[-1],
    label="10min",
    linewidth=1,
)

# ax[0, 0].plot(days, (np.cumsum(ten_min_winds))/np.cumsum(ten_min_winds), label="ten min", linewidth=1)
# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[0, 0].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[0, 0].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[0, 0].get_xticklabels(), rotation=90, ha="center")


six_hourly_winds = np.load("data/power-gen/Aachen/six_hourly_inst.npy")
three_hourly_winds = np.load("data/power-gen/Aachen/three_hourly_inst.npy")
daily_winds = np.load("data/power-gen/Aachen/daily_inst.npy")


print(((np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])

"""
avrg
-153.6635014583345
-40.279854444447324
-62.26066680555914

inst
-100.7719770833296
-3.472802083340639
1.9895404166620665
"""
ax[1, 0].plot(
    days,
    (np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
# ax[1, 0].plot(days, (np.cumsum(hourly_winds))/np.cumsum(ten_min_winds), label="hourly", linewidth=1)
ax[1, 0].plot(
    days,
    (np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[1, 0].plot(
    days,
    (np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[1, 0].plot(
    days,
    (np.cumsum(ten_min_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)

# ax[1, 0].plot(days, (np.cumsum(ten_min_winds))/np.cumsum(ten_min_winds), label="ten min", linewidth=1)


# ax[1, 0].legend()
ax[1, 0].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[1, 0].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[1, 0].get_xticklabels(), rotation=90, ha="center")

# load data
six_hourly_winds = np.load("data/power-gen/Zugspitze/six_hourly_avrg.npy")
three_hourly_winds = np.load("data/power-gen/Zugspitze/three_hourly_avrg.npy")
daily_winds = np.load("data/power-gen/Zugspitze/daily_avrg.npy")
ten_min_winds = np.load("data/power-gen/Zugspitze/ten_min.npy")
days = np.load("data/power-gen/Zugspitze/days.npy", allow_pickle=True)

print(((np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])

ax[0, 1].plot(
    days,
    (np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
# ax[0, 0].plot(days, (np.cumsum(hourly_winds))/np.cumsum(ten_min_winds), label="hourly", linewidth=1)
ax[0, 1].plot(
    days,
    (np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[0, 1].plot(
    days,
    (np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[0, 1].plot(
    days,
    (np.cumsum(ten_min_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)

# ax[0, 1].plot(days,(np.cumsum(ten_min_winds) )/np.cumsum(ten_min_winds),label="ten min",linewidth=1,)
# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
# ax[0, 1].legend()
ax[0, 1].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[0, 1].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[0, 1].get_xticklabels(), rotation=90, ha="center")

six_hourly_winds = np.load("data/power-gen/Zugspitze/six_hourly_inst.npy")
three_hourly_winds = np.load("data/power-gen/Zugspitze/three_hourly_inst.npy")
daily_winds = np.load("data/power-gen/Zugspitze/daily_inst.npy")

print(((np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])

"""
avrg
-159.893164930495
-39.162081874947035
-70.31662444440099

#inst
785.216445000051
4.7597075000057885
6.063275000008616
"""

ax[1, 1].plot(
    days,
    (np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
"""
ax[1, 1].plot(
    days,
    (np.cumsum(hourly_winds) )/np.cumsum(ten_min_winds),
    label="hourly",
    linewidth=1,
)
"""
ax[1, 1].plot(
    days,
    (np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[1, 1].plot(
    days,
    (np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[1, 1].plot(
    days,
    (np.cumsum(ten_min_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)

ax[1, 1].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[1, 1].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[1, 1].get_xticklabels(), rotation=90, ha="center")

# load data
six_hourly_winds = np.load("data/power-gen/Boltenhagen/six_hourly_avrg.npy")
three_hourly_winds = np.load("data/power-gen/Boltenhagen/three_hourly_avrg.npy")
daily_winds = np.load("data/power-gen/Boltenhagen/daily_avrg.npy")
ten_min_winds = np.load("data/power-gen/Boltenhagen/ten_min.npy")
days = np.load("data/power-gen/Boltenhagen/days.npy", allow_pickle=True)

print(((np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])

ax[0, 2].plot(
    days,
    (np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)


ax[0, 2].plot(
    days,
    (np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)

ax[0, 2].plot(
    days,
    (np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)

ax[0, 2].plot(
    days,
    (np.cumsum(ten_min_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[0, 2].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[0, 2].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[0, 2].get_xticklabels(), rotation=90, ha="center")

six_hourly_winds = np.load("data/power-gen/Boltenhagen/six_hourly_inst.npy")
three_hourly_winds = np.load("data/power-gen/Boltenhagen/three_hourly_inst.npy")
daily_winds = np.load("data/power-gen/Boltenhagen/daily_inst.npy")

print(((np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])

"""
avrg
-559.4000596528167
-111.22540333334473
-192.3090424305774

inst
-782.1292220139821
9.88516173608241
3.6882379860808214
"""

ax[1, 2].plot(
    days,
    (np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
"""
ax[1, 2].plot(
    days,
    (np.cumsum(hourly_winds) )/np.cumsum(ten_min_winds),
    label="hourly",
    linewidth=1,
)
"""
ax[1, 2].plot(
    days,
    (np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[1, 2].plot(
    days,
    (np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[1, 2].plot(
    days,
    (np.cumsum(ten_min_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)


ax[1, 2].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[1, 2].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[1, 2].get_xticklabels(), rotation=90, ha="center")

# load data
six_hourly_winds = np.load("data/power-gen/Fichtelberg/six_hourly_avrg.npy")
three_hourly_winds = np.load("data/power-gen/Fichtelberg/three_hourly_avrg.npy")
daily_winds = np.load("data/power-gen/Fichtelberg/daily_avrg.npy")
ten_min_winds = np.load("data/power-gen/Fichtelberg/ten_min.npy")
days = np.load("data/power-gen/Fichtelberg/days.npy", allow_pickle=True)

print(((np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])

ax[0, 3].plot(
    days,
    (np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)

ax[0, 3].plot(
    days,
    (np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)

ax[0, 3].plot(
    days,
    (np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[0, 3].plot(
    days,
    (np.cumsum(ten_min_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)

# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[0, 3].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[0, 3].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[0, 2].get_xticklabels(), rotation=90, ha="center")

six_hourly_winds = np.load("data/power-gen/Fichtelberg/six_hourly_inst.npy")
three_hourly_winds = np.load("data/power-gen/Fichtelberg/three_hourly_inst.npy")
daily_winds = np.load("data/power-gen/Fichtelberg/daily_inst.npy")

print(((np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])

"""
avrg
-214.98217694444548
-62.71411694444248

inst
-131.1548332638758
1.8341067361061505
-9.796615763885484
"""

ax[1, 3].plot(
    days,
    (np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)

ax[1, 3].plot(
    days,
    (np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[1, 3].plot(
    days,
    (np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[1, 3].plot(
    days,
    (np.cumsum(ten_min_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)


ax[1, 3].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[1, 3].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[1, 3].get_xticklabels(), rotation=90, ha="center")
custom_ylim = (0, 1.3)
plt.setp(ax, ylim=custom_ylim)

ax[0, 0].text(0.03, 0.9, "5a)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.9, "6a)", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.9, "7a)", transform=ax[0, 2].transAxes)
ax[0, 3].text(0.03, 0.9, "8a)", transform=ax[0, 3].transAxes)
ax[1, 0].text(0.03, 0.9, "5b)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.9, "6b)", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.9, "7b)", transform=ax[1, 2].transAxes)
ax[1, 3].text(0.03, 0.9, "8b)", transform=ax[1, 3].transAxes)

fig.legend(loc="outside right center")
fig.supxlabel("Time (years)")
fig.supylabel("Relative electricity generation")
ax[0, 0].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[0, 1].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[0, 2].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[0, 3].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[1, 0].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[1, 1].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[1, 2].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[1, 3].axhline(y=1, color="grey", linestyle="--", linewidth=1)

plt.savefig(savepath)
plt.show()
