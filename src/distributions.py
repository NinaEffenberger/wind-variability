import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


def plot_windspeed_hist(average_daily, average_three_hourly, average_hourly, average_10min, savepath=None):
    speeds = [
        average_daily.to_numpy().flatten(),
        np.array(average_three_hourly).flatten(),
        average_hourly.to_numpy().flatten(),
        average_10min.to_numpy().flatten(),
    ]
    bins = np.linspace(0, 15, 15)
    """
    plt.hist(average_daily, bins, alpha=0.5)
    plt.hist(average_hourly, bins, alpha=0.5)
    plt.hist(average_three_hourly, bins, alpha=0.5)
    plt.hist(ten_min_windspeed, bins, alpha=0.5)
    """
    plt.hist(speeds, bins, label=["day", "3h", "1h", "10min"], density=True)
    plt.legend()
    plt.xlabel(r"$\frac{m}{s}$")
    plt.ylabel("relative frequency")
    plt.savefig(savepath)
    # plt.show()


def plot_weibull_fit(
    average_monthly,
    average_daily,
    average_three_hourly,
    average_hourly,
    average_10min,
    savepath=None,
    bounds=[(0, 15), (0, 15), (0, 15)],
):
    speeds = [
        average_monthly.to_numpy().flatten(),
        average_daily.to_numpy().flatten(),
        np.array(average_three_hourly).flatten(),
        average_hourly.to_numpy().flatten(),
        average_10min.to_numpy().flatten(),
    ]

    def weibull(x, c, loc, scale):
        y = (x - loc) / scale
        return c * y ** (c - 1) * np.exp(-(y**c)) / scale

    dist = stats.weibull_min
    bounds = bounds
    x_vals = np.linspace(0, bounds[2][1], 1000)

    # fit Weibull once for each
    fit = stats.fit(dist, average_monthly.to_numpy().flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="purple", label="month")
    fit = stats.fit(dist, average_daily.to_numpy().flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="blue", label="day")
    print(fit.params)
    fit = stats.fit(dist, np.array(average_three_hourly).flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="orange", label="3h")
    print(fit.params)
    fit = stats.fit(dist, average_hourly.to_numpy().flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="green", label="1h")
    print(fit.params)
    fit = stats.fit(dist, average_10min.to_numpy().flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="red", label="10min")
    print(fit.params)

    bins = np.linspace(0, bounds[2][1], bounds[2][1])
    plt.hist(
        speeds,
        bins,
        color=["purple", "blue", "orange", "green", "red"],
        alpha=0.3,
        density=True,
    )
    plt.xlabel(r"$\frac{m}{s}$")
    plt.ylabel("relative frequency")
    plt.legend()
    plt.savefig(savepath)
    # plt.show()


def plot_weibull_fit_KDE(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
    savepath=None,
    bounds=[(0, 15), (0, 15), (0, 15)],
):
    """
    speeds = [
        average_monthly.to_numpy().flatten(),
        average_daily.to_numpy().flatten(),
        np.array(average_three_hourly).flatten(),
        np.array(average_six_hourly).flatten(),
        average_hourly.to_numpy().flatten(),
        average_10min.to_numpy().flatten(),
    ]
    """

    def weibull(x, c, loc, scale):
        y = (x - loc) / scale
        return c * y ** (c - 1) * np.exp(-(y**c)) / scale

    dist = stats.weibull_min
    bounds = bounds
    x_vals = np.linspace(0, bounds[2][1], 1000)

    # fit Weibull once for each
    fit = stats.fit(dist, average_monthly.to_numpy().flatten(), bounds)
    # plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="purple", label="month")
    fit = stats.fit(dist, average_daily.to_numpy().flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="blue", label="day")
    print(fit.params)
    fit = stats.fit(dist, np.array(average_six_hourly).flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="brown", label="6h")
    print(fit.params)
    fit = stats.fit(dist, np.array(average_three_hourly).flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="orange", label="3h")
    print(fit.params)
    fit = stats.fit(dist, average_hourly.to_numpy().flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="green", label="1h")
    print(fit.params)
    fit = stats.fit(dist, average_10min.to_numpy().flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="red", label="10min")
    print(fit.params)
    plt.legend()
    bins = np.linspace(0, bounds[2][1], bounds[2][1])
    """
    plt.hist(
        speeds,
        bins,
        color=["purple", "blue", "orange", "green", "red", "brown"],
        alpha=0.3,
        density=True,
    )
    """
    # month = pd.Series(average_monthly)
    three = pd.Series(np.array(average_three_hourly).flatten())
    six = pd.Series(np.array(average_six_hourly).flatten())
    day = pd.Series(average_daily)
    hour = pd.Series(average_hourly)
    ten_min = pd.Series(average_10min)
    ten_min.plot.kde(color="red", linestyle="--")
    hour.plot.kde(color="green", linestyle="--")
    # month.plot.kde(color="purple", linestyle="--")
    day.plot.kde(color="blue", linestyle="--")
    three.plot.kde(color="orange", linestyle="--")
    six.plot.kde(color="brown", linestyle="--")

    plt.xlabel(r"$\frac{m}{s}$")
    plt.ylabel("relative frequency")
    plt.savefig(savepath)
    # plt.show()


def weibull_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
    bounds=[(0, 15), (0, 15), (0, 15)],
):

    dist = stats.weibull_min
    bounds = bounds
    cs = []
    locs = []
    scales = []
    # fit Weibull once for each
    bounds = bounds

    # fit Weibull once for each
    fit = stats.fit(dist, average_10min, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    fit = stats.fit(dist, average_hourly, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    fit = stats.fit(dist, average_three_hourly, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    fit = stats.fit(dist, average_six_hourly, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    fit = stats.fit(dist, average_daily, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    fit = stats.fit(dist, average_monthly, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    return cs, locs, scales


def gamma_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
    bounds=[(0, 15), (0, 15), (0, 15)],
):

    cs = []
    locs = []
    scales = []
    # fit Weibull once for each

    # fit Weibull once for each
    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(average_10min)
    cs.append(fit_alpha)
    locs.append(fit_loc)
    scales.append(fit_beta)
    print("10min: " + str(fit_alpha) + ", " + str(fit_loc) + ", " + str(fit_beta))
    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(average_hourly)
    cs.append(fit_alpha)
    locs.append(fit_loc)
    scales.append(fit_beta)
    print("Hourly: " + str(fit_alpha) + ", " + str(fit_loc) + ", " + str(fit_beta))
    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(average_three_hourly)
    cs.append(fit_alpha)
    locs.append(fit_loc)
    scales.append(fit_beta)
    print("3h: " + str(fit_alpha) + ", " + str(fit_loc) + ", " + str(fit_beta))
    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(average_six_hourly)
    cs.append(fit_alpha)
    locs.append(fit_loc)
    scales.append(fit_beta)
    print("6h: " + str(fit_alpha) + ", " + str(fit_loc) + ", " + str(fit_beta))
    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(average_daily)
    cs.append(fit_alpha)
    locs.append(fit_loc)
    scales.append(fit_beta)
    print("Daily: " + str(fit_alpha) + ", " + str(fit_loc) + ", " + str(fit_beta))
    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(average_monthly)
    cs.append(fit_alpha)
    locs.append(fit_loc)
    scales.append(fit_beta)
    print("Monthly: " + str(fit_alpha) + ", " + str(fit_loc) + ", " + str(fit_beta))
    return cs, locs, scales


def plot_param_trend(cs, locs, scales, savepath):
    fig, ax = plt.subplots(1, 1)
    ax.plot(cs, label="c")
    ax.plot(locs, label="loc")
    ax.plot(scales, label="scale")
    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xticklabels(["10min", "hour", "3h", "6h", "day", "month"])
    plt.legend()
    plt.savefig(savepath)
    # plt.show()


def plot_param_trend_precentage(cs, locs, scales, savepath):
    fig, ax = plt.subplots(1, 1)
    ax.plot(cs / cs[0], label="c")
    ax.plot(locs / locs[0], label="loc")
    ax.plot(scales / scales[0], label="scale")
    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xticklabels(["10min", "hour", "3h", "6h", "day", "month"])
    plt.legend()
    plt.savefig(savepath)
    # plt.show()


def plot_param_trend_both(cs, locs, scales, cs_loc0, scales_loc0, savepath):
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(cs_loc0 / cs_loc0[0], label="k")
    ax[0].plot(scales_loc0 / scales_loc0[0], label="scale")
    ax[0].set_xticks([0, 1, 2, 3, 4, 5])
    ax[0].set_xticklabels(["10min", "hour", "3h", "6h", "day", "month"])
    ax[1].plot(cs / cs[0], label="k")
    ax[1].plot(locs / locs[0], label="loc")
    ax[1].plot(scales / scales[0], label="scale")
    ax[1].set_xticks([0, 1, 2, 3, 4, 5])
    ax[1].set_xticklabels(["10min", "hour", "3h", "6h", "day", "month"])
    ax[0].legend()
    ax[1].legend()
    plt.savefig(savepath)
    # plt.show()


def plot_param_trend_both_CMIP6(cs, locs, scales, cs_loc0, scales_loc0, savepath):
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(cs_loc0 / cs_loc0[0], label="k")
    ax[0].plot(scales_loc0 / scales_loc0[0], label="scale")
    ax[0].set_xticks([0, 1, 2, 3])
    ax[0].set_xticklabels(["3h", "6h", "day", "month"])
    ax[1].plot(cs / cs[0], label="k")
    ax[1].plot(locs / locs[0], label="loc")
    ax[1].plot(scales / scales[0], label="scale")
    ax[1].set_xticks([0, 1, 2, 3])
    ax[1].set_xticklabels(["3h", "6h", "day", "month"])
    ax[0].legend()
    ax[1].legend()
    plt.savefig(savepath)
    # plt.show()


def compute_instantenous_windspeeds(data, windspeeds="Wind speed (m/s)"):
    day = data[windspeeds][:: 24 * 6].values
    six_hour = data[windspeeds][:: 6 * 6].values
    three_hour = data[windspeeds][:: 3 * 6].values
    hour = data[windspeeds][::6].values
    return day, six_hour, three_hour, hour


from scipy import stats


def plot_weibull_fit_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_daily,
    average_three_hourly,
    average_hourly,
    average_10min,
    savepath=None,
    bounds=[(0, 15), (0, 15), (0, 15)],
):
    speeds = [
        hour,
        three_hour,
        six_hour,
        day,
        average_daily.to_numpy().flatten(),
        np.array(average_three_hourly).flatten(),
        average_hourly.to_numpy().flatten(),
        average_10min.to_numpy().flatten(),
    ]

    def weibull(x, c, loc, scale):
        y = (x - loc) / scale
        return c * y ** (c - 1) * np.exp(-(y**c)) / scale

    dist = stats.weibull_min
    bounds = bounds
    x_vals = np.linspace(0, bounds[2][1], 1000)

    # fit Weibull once for each
    fit = stats.fit(dist, hour, bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="purple", label="1h inst")
    fit = stats.fit(dist, three_hour, bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="blue", label="3h inst")
    print(fit.params)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="black", label="6h inst")
    print(fit.params)
    fit = stats.fit(dist, day, bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="pink", label="day inst")
    fit = stats.fit(dist, np.array(average_daily).flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="grey", label="day")
    fit = stats.fit(dist, np.array(average_three_hourly).flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="orange", label="3h")
    print(fit.params)
    fit = stats.fit(dist, average_hourly.to_numpy().flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="green", label="1h")
    print(fit.params)
    fit = stats.fit(dist, average_10min.to_numpy().flatten(), bounds)
    plt.plot(x_vals, weibull(x_vals, fit.params.c, fit.params.loc, fit.params.scale), color="red", label="10min")
    print(fit.params)

    bins = np.linspace(0, bounds[2][1], bounds[2][1])
    plt.hist(
        speeds,
        bins,
        color=["purple", "blue", "black", "pink", "grey", "orange", "green", "red"],
        alpha=0.3,
        density=True,
    )
    plt.xlabel(r"$\frac{m}{s}$")
    plt.ylabel("relative frequency")
    plt.legend()
    plt.savefig(savepath)
    # plt.show()


def weibull_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    ten_min,
    bounds=[(0, 15), (0, 15), (0, 15)],
):

    dist = stats.weibull_min
    bounds = bounds
    cs = []
    locs = []
    scales = []
    # fit Weibull once for each
    bounds = bounds

    # fit Weibull once for each
    fit = stats.fit(dist, ten_min, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    print("10min: " + str(fit.params))
    fit = stats.fit(dist, hour, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    print("Hourly: " + str(fit.params))
    fit = stats.fit(dist, three_hour, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    print("3h: " + str(fit.params))
    fit = stats.fit(dist, six_hour, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    print("6h: " + str(fit.params))
    fit = stats.fit(dist, day, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    print("Day: " + str(fit.params))
    return cs, locs, scales


def gamma_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    ten_min,
):

    cs = []
    locs = []
    scales = []
    # fit Weibull once for each

    # fit Weibull once for each
    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(ten_min)
    cs.append(fit_alpha)
    locs.append(fit_loc)
    scales.append(fit_beta)
    print("10min: " + str(fit_alpha) + ", " + str(fit_loc) + ", " + str(fit_beta))
    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(hour)
    cs.append(fit_alpha)
    locs.append(fit_loc)
    scales.append(fit_beta)
    print("1h: " + str(fit_alpha) + ", " + str(fit_loc) + ", " + str(fit_beta))
    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(three_hour)
    cs.append(fit_alpha)
    locs.append(fit_loc)
    scales.append(fit_beta)
    print("3h: " + str(fit_alpha) + ", " + str(fit_loc) + ", " + str(fit_beta))
    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(six_hour)
    cs.append(fit_alpha)
    locs.append(fit_loc)
    scales.append(fit_beta)
    print("6h: " + str(fit_alpha) + ", " + str(fit_loc) + ", " + str(fit_beta))
    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(day)
    cs.append(fit_alpha)
    locs.append(fit_loc)
    scales.append(fit_beta)
    print("day: " + str(fit_alpha) + ", " + str(fit_loc) + ", " + str(fit_beta))
    return cs, locs, scales


def plot_param_trend_instanteous(cs, locs, scales, savepath):
    fig, ax = plt.subplots(1, 1)
    ax.plot(cs, label="c")
    ax.plot(locs, label="loc")
    ax.plot(scales, label="scale")
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(["10min", "hour", "3h", "6h", "day"])
    plt.legend()
    plt.savefig(savepath)
    # plt.show()


def weibull_paramsdef_cmip6(
    month,
    day,
    six_hour,
    three_hour,
    bounds=[(0, 15), (0, 15), (0, 15)],
):

    dist = stats.weibull_min
    bounds = bounds
    cs = []
    locs = []
    scales = []
    # fit Weibull once for each
    bounds = bounds

    # fit Weibull once for each
    fit = stats.fit(dist, three_hour, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    print("3h: " + str(fit.params))
    fit = stats.fit(dist, six_hour, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    print("6h: " + str(fit.params))
    fit = stats.fit(dist, day, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    print("Day: " + str(fit.params))
    fit = stats.fit(dist, month, bounds)
    cs.append(fit.params.c)
    locs.append(fit.params.loc)
    scales.append(fit.params.scale)
    print("Month: " + str(fit.params))
    return cs, locs, scales


def plot_param_trend_instanteous(cs, locs, scales, savepath):
    fig, ax = plt.subplots(1, 1)
    ax.plot(cs, label="c")
    ax.plot(locs, label="loc")
    ax.plot(scales, label="scale")
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(["10min", "hour", "3h", "6h", "day"])
    plt.legend()
    plt.savefig(savepath)


def plot_param_trend_precentage_instanteous(cs, locs, scales, savepath):
    fig, ax = plt.subplots(1, 1)
    ax.plot(cs / cs[0], label="c")
    ax.plot(locs / locs[0], label="loc")
    ax.plot(scales / scales[0], label="scale")
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(["10min", "hour", "3h", "6h", "day"])
    plt.legend()
    plt.savefig(savepath)
    # plt.show()


def plot_param_trend_precentage_cmip6(cs, locs, scales, savepath):
    fig, ax = plt.subplots(1, 1)
    ax.plot(cs / cs[0], label="c")
    ax.plot(locs / locs[0], label="loc")
    ax.plot(scales / scales[0], label="scale")
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(["3h", "6h", "day", "month"])
    plt.legend()
    plt.savefig(savepath)
    # plt.show()
