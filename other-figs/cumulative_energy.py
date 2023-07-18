import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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

fig, ax = plt.subplots(2, 1, sharex="col", figsize=(6, 4), sharey=True, constrained_layout=True)
print(((np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])
print(((np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1])[-1])

ax[0].plot(
    days,
    (np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1],
    label="day",
    linewidth=1,
)
# ax[0].plot(days, (np.cumsum(hourly_winds))/np.cumsum(ten_min_winds), label="hourly", linewidth=1)
ax[0].plot(
    days,
    (np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    label="6h",
    linewidth=1,
)
ax[0].plot(
    days,
    (np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    label="3h",
    linewidth=1,
)
ax[0].plot(
    days,
    (np.cumsum(ten_min_winds)) / np.cumsum(ten_min_winds)[-1],
    label="10min",
    linewidth=1,
)

# ax[0].plot(days, (np.cumsum(ten_min_winds))/np.cumsum(ten_min_winds), label="ten min", linewidth=1)
# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[0].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[0].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[0].get_xticklabels(), rotation=90, ha="center")


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
ax[1].plot(
    days,
    (np.cumsum(daily_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
# ax[1].plot(days, (np.cumsum(hourly_winds))/np.cumsum(ten_min_winds), label="hourly", linewidth=1)
ax[1].plot(
    days,
    (np.cumsum(three_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[1].plot(
    days,
    (np.cumsum(six_hourly_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)
ax[1].plot(
    days,
    (np.cumsum(ten_min_winds)) / np.cumsum(ten_min_winds)[-1],
    linewidth=1,
)

# ax[1].plot(days, (np.cumsum(ten_min_winds))/np.cumsum(ten_min_winds), label="ten min", linewidth=1)


# ax[1].legend()
ax[1].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[1].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[1].get_xticklabels(), rotation=90, ha="center")
fig.legend(loc="outside right center")
fig.supxlabel("Time (years)")
fig.supylabel("Electricity generation")
ax[0].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[1].axhline(y=1, color="grey", linestyle="--", linewidth=1)
plt.show()
