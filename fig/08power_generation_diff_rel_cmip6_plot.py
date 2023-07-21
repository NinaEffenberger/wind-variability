import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from windspeed_averages_wp import compute_windpower_generation_cmip, drop_nans_DWD, set_date_DWD

matplotlib.rcParams.update({"font.size": 12})

savepath = "plots_paper/plots/power_gen_diff_30yrs.svg"
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)
fig, ax = plt.subplots(2, 4, sharex="col", figsize=(6, 4), constrained_layout=True, sharey=True)

dates_avergage = np.load("data/cmip6/data/Aachen/times_averages_three.npy")

# load data
time_series_day = np.load("data/cmip6/data/Kelmarsh/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Kelmarsh/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Kelmarsh/time_series_three.npy")
time_series_three_pt = np.load("data/cmip6/data/Kelmarsh/time_series_three_pt.npy")
time_series_six_pt = np.load("data/cmip6/data/Kelmarsh/time_series_six_pt.npy")

(power_day, power_six_avrg, power_three_avr, power_six_pt, power_three_pt,) = compute_windpower_generation_cmip(
    time_series_day,
    time_series_six,
    time_series_three,
    time_series_six_pt,
    time_series_three_pt,
)


ax[0, 0].plot(
    dates_avergage[::8],
    (np.cumsum(power_day)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
# ax[1, 0].plot(days, (np.cumsum(hourly_winds)- np.cumsum(ten_min_winds)), label="hourly", linewidth=1)
ax[0, 0].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_avrg)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
ax[0, 0].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_pt)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

ax[0, 0].plot(
    dates_avergage[::8],
    (np.cumsum(power_three_avr)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)


# ax[1, 0].plot(days, (np.cumsum(ten_min_winds)- np.cumsum(ten_min_winds)), label="ten min", linewidth=1)
# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[0, 0].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[0, 0].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[0, 0].get_xticklabels(), rotation=90, ha="center")

# load data
time_series_day = np.load("data/cmip6/data/Penmanshiel/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Penmanshiel/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Penmanshiel/time_series_three.npy")
time_series_three_pt = np.load("data/cmip6/data/Penmanshiel/time_series_three_pt.npy")
time_series_six_pt = np.load("data/cmip6/data/Penmanshiel/time_series_six_pt.npy")

(power_day, power_six_avrg, power_three_avr, power_six_pt, power_three_pt,) = compute_windpower_generation_cmip(
    time_series_day,
    time_series_six,
    time_series_three,
    time_series_six_pt,
    time_series_three_pt,
)


ax[0, 1].plot(
    dates_avergage[::8],
    (np.cumsum(power_day)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
# ax[1, 0].plot(days, (np.cumsum(hourly_winds)- np.cumsum(ten_min_winds)), label="hourly", linewidth=1)
ax[0, 1].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_avrg)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
ax[0, 1].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_pt)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

ax[0, 1].plot(
    dates_avergage[::8],
    (np.cumsum(power_three_avr)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[0, 1].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[0, 1].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[0, 1].get_xticklabels(), rotation=90, ha="center")

# load data
time_series_day = np.load("data/cmip6/data/NWTC/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/NWTC/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/NWTC/time_series_three.npy")
time_series_three_pt = np.load("data/cmip6/data/NWTC/time_series_three_pt.npy")
time_series_six_pt = np.load("data/cmip6/data/NWTC/time_series_six_pt.npy")

(power_day, power_six_avrg, power_three_avr, power_six_pt, power_three_pt,) = compute_windpower_generation_cmip(
    time_series_day,
    time_series_six,
    time_series_three,
    time_series_six_pt,
    time_series_three_pt,
)


ax[0, 2].plot(
    dates_avergage[::8],
    (np.cumsum(power_day)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
ax[0, 2].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_avrg)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
ax[0, 2].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_pt)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

ax[0, 2].plot(
    dates_avergage[::8],
    (np.cumsum(power_three_avr)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[0, 2].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[0, 2].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[0, 2].get_xticklabels(), rotation=90, ha="center")

# load data
time_series_day = np.load("data/cmip6/data/Owez/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Owez/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Owez/time_series_three.npy")
time_series_three_pt = np.load("data/cmip6/data/Owez/time_series_three_pt.npy")
time_series_six_pt = np.load("data/cmip6/data/Owez/time_series_six_pt.npy")

(power_day, power_six_avrg, power_three_avr, power_six_pt, power_three_pt,) = compute_windpower_generation_cmip(
    time_series_day,
    time_series_six,
    time_series_three,
    time_series_six_pt,
    time_series_three_pt,
)


ax[0, 3].plot(
    dates_avergage[::8],
    (np.cumsum(power_day)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
# ax[1, 0].plot(dates_avergage[::8],days, (np.cumsum(hourly_winds)- np.cumsum(ten_min_winds)), label="hourly", linewidth=1)
ax[0, 3].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_avrg)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
ax[0, 3].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_pt)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

ax[0, 3].plot(
    dates_avergage[::8],
    (np.cumsum(power_three_avr)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

# ax[1, 0].plot(dates_avergage[::8],days, (np.cumsum(ten_min_winds)- np.cumsum(ten_min_winds)), label="ten min", linewidth=1)
# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[0, 3].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[0, 3].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[0, 3].get_xticklabels(), rotation=90, ha="center")

# load data
time_series_day = np.load("data/cmip6/data/Aachen/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Aachen/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Aachen/time_series_three.npy")
time_series_three_pt = np.load("data/cmip6/data/Aachen/time_series_three_pt.npy")
time_series_six_pt = np.load("data/cmip6/data/Aachen/time_series_six_pt.npy")

(power_day, power_six_avrg, power_three_avr, power_six_pt, power_three_pt,) = compute_windpower_generation_cmip(
    time_series_day,
    time_series_six,
    time_series_three,
    time_series_six_pt,
    time_series_three_pt,
)


ax[1, 0].plot(
    dates_avergage[::8],
    (np.cumsum(power_day)) / np.cumsum(power_three_pt)[-1],
    label="day",
    linewidth=1,
)
# ax[1, 0].plot(days, (np.cumsum(hourly_winds)- np.cumsum(ten_min_winds)), label="hourly", linewidth=1)
ax[1, 0].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_avrg)) / np.cumsum(power_three_pt)[-1],
    label=r"$6h _{avrg}$",
    linewidth=1,
)
ax[1, 0].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_pt)) / np.cumsum(power_three_pt)[-1],
    label=r"$6h _{inst}$",
    linewidth=1,
)

ax[1, 0].plot(
    dates_avergage[::8],
    (np.cumsum(power_three_avr)) / np.cumsum(power_three_pt)[-1],
    label=r"$3h _{avrg}$",
    linewidth=1,
)

# ax[1, 0].plot(days, (np.cumsum(ten_min_winds)- np.cumsum(ten_min_winds)), label="ten min", linewidth=1)
# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[1, 0].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[1, 0].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[1, 0].get_xticklabels(), rotation=90, ha="center")

# load data
time_series_day = np.load("data/cmip6/data/Zugspitze/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Zugspitze/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Zugspitze/time_series_three.npy")
time_series_three_pt = np.load("data/cmip6/data/Zugspitze/time_series_three_pt.npy")
time_series_six_pt = np.load("data/cmip6/data/Zugspitze/time_series_six_pt.npy")

(power_day, power_six_avrg, power_three_avr, power_six_pt, power_three_pt,) = compute_windpower_generation_cmip(
    time_series_day,
    time_series_six,
    time_series_three,
    time_series_six_pt,
    time_series_three_pt,
)


ax[1, 1].plot(
    dates_avergage[::8],
    (np.cumsum(power_day)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
# ax[1, 0].plot(dates_avergage[::8],days, (np.cumsum(hourly_winds)- np.cumsum(ten_min_winds)), label="hourly", linewidth=1)
ax[1, 1].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_avrg)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
ax[1, 1].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_pt)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

ax[1, 1].plot(
    dates_avergage[::8],
    (np.cumsum(power_three_avr)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

# ax[1, 0].plot(days, (np.cumsum(ten_min_winds)- np.cumsum(ten_min_winds)), label="ten min", linewidth=1)
# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[1, 1].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[1, 1].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[1, 1].get_xticklabels(), rotation=90, ha="center")

# load data
time_series_day = np.load("data/cmip6/data/Boltenhagen/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Boltenhagen/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Boltenhagen/time_series_three.npy")
time_series_three_pt = np.load("data/cmip6/data/Boltenhagen/time_series_three_pt.npy")
time_series_six_pt = np.load("data/cmip6/data/Boltenhagen/time_series_six_pt.npy")

(power_day, power_six_avrg, power_three_avr, power_six_pt, power_three_pt,) = compute_windpower_generation_cmip(
    time_series_day,
    time_series_six,
    time_series_three,
    time_series_six_pt,
    time_series_three_pt,
)


ax[1, 2].plot(
    dates_avergage[::8],
    (np.cumsum(power_day)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
# ax[1, 0].plot(dates_avergage[::8],days, (np.cumsum(hourly_winds)- np.cumsum(ten_min_winds)), label="hourly", linewidth=1)
ax[1, 2].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_avrg)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
ax[1, 2].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_pt)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

ax[1, 2].plot(
    dates_avergage[::8],
    (np.cumsum(power_three_avr)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

# ax[1, 0].plot(days, (np.cumsum(ten_min_winds)- np.cumsum(ten_min_winds)), label="ten min", linewidth=1)
# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[1, 2].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[1, 2].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[1, 2].get_xticklabels(), rotation=90, ha="center")

# load data
time_series_day = np.load("data/cmip6/data/Fichtelberg/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Fichtelberg/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Fichtelberg/time_series_three.npy")
time_series_three_pt = np.load("data/cmip6/data/Fichtelberg/time_series_three_pt.npy")
time_series_six_pt = np.load("data/cmip6/data/Fichtelberg/time_series_six_pt.npy")

(power_day, power_six_avrg, power_three_avr, power_six_pt, power_three_pt,) = compute_windpower_generation_cmip(
    time_series_day,
    time_series_six,
    time_series_three,
    time_series_six_pt,
    time_series_three_pt,
)


ax[1, 3].plot(
    dates_avergage[::8],
    (np.cumsum(power_day)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
# ax[1, 0].plot(dates_avergage[::8],days, (np.cumsum(hourly_winds)- np.cumsum(ten_min_winds)), label="hourly", linewidth=1)
ax[1, 3].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_avrg)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)
ax[1, 3].plot(
    dates_avergage[::8],
    (np.cumsum(power_six_pt)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

ax[1, 3].plot(
    dates_avergage[::8],
    (np.cumsum(power_three_avr)) / np.cumsum(power_three_pt)[-1],
    linewidth=1,
)

print(((np.cumsum(power_day)) / np.cumsum(power_three_pt)[-1])[-1])
print(((np.cumsum(power_six_avrg)) / np.cumsum(power_three_pt)[-1])[-1])
print(((np.cumsum(power_six_pt)) / np.cumsum(power_three_pt)[-1])[-1])
print(((np.cumsum(power_three_avr)) / np.cumsum(power_three_pt)[-1])[-1])
custom_ylim = (0, 1.3)
plt.setp(ax, ylim=custom_ylim)

# ax[1, 0].plot(days, (np.cumsum(ten_min_winds)- np.cumsum(ten_min_winds)), label="ten min", linewidth=1)
# ax[1].set_xlim(data['date'].dt.year.iloc[0], data['date'].dt.year.iloc[-1])
ax[1, 3].xaxis.set_major_locator(matplotlib.dates.YearLocator(base=10))
ax[1, 3].xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
plt.setp(ax[1, 3].get_xticklabels(), rotation=90, ha="center")
fig.legend(loc="outside right center")
ax[0, 0].text(0.03, 0.9, "(a)", transform=ax[0, 0].transAxes)
ax[0, 1].text(0.03, 0.9, "(b)", transform=ax[0, 1].transAxes)
ax[0, 2].text(0.03, 0.9, "(c)", transform=ax[0, 2].transAxes)
ax[0, 3].text(0.03, 0.9, "(d)", transform=ax[0, 3].transAxes)
ax[1, 0].text(0.03, 0.9, "(e)", transform=ax[1, 0].transAxes)
ax[1, 1].text(0.03, 0.9, "(f)", transform=ax[1, 1].transAxes)
ax[1, 2].text(0.03, 0.9, "(g)", transform=ax[1, 2].transAxes)
ax[1, 3].text(0.03, 0.9, "(h)", transform=ax[1, 3].transAxes)

ax[0, 0].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[0, 1].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[0, 2].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[0, 3].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[1, 0].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[1, 1].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[1, 2].axhline(y=1, color="grey", linestyle="--", linewidth=1)
ax[1, 3].axhline(y=1, color="grey", linestyle="--", linewidth=1)
fig.supxlabel("Time (years)")
fig.supylabel("Relative electricity generation")

plt.savefig("plots_eps/power_generation_diff_real_cmip6.eps")
plt.show()
