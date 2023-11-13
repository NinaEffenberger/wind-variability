import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


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
    cs = []
    locs = []
    scales = []

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
):

    cs = []
    locs = []
    scales = []

    # fit Gamma once for each
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


def compute_instantenous_windspeeds(data, windspeeds="Wind speed (m/s)"):
    day = data[windspeeds][:: 24 * 6].values
    six_hour = data[windspeeds][:: 6 * 6].values
    three_hour = data[windspeeds][:: 3 * 6].values
    hour = data[windspeeds][::6].values
    return day, six_hour, three_hour, hour


def weibull_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    ten_min,
    bounds=[(0, 15), (0, 15), (0, 15)],
):

    dist = stats.weibull_min
    cs = []
    locs = []
    scales = []

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
