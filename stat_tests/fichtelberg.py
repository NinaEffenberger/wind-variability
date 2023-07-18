import numpy as np
import pandas as pd
from distributions import compute_instantenous_windspeeds
from kolmogorov_smirnov import kolmogorov_smirnov_multi, plot_cumulative_densities_day
from windspeed_averages_wp import compute_average_windspeeds, drop_nans, load_data, set_date

# load data
average_daily = np.load("data/Pickles/Fichtelberg/average_daily.npy")
average_hourly = np.load("data/Pickles/Fichtelberg/average_hourly.npy")
average_10min = np.load("data/Pickles/Fichtelberg/average_10min.npy")
average_monthly = np.load("data/Pickles/Fichtelberg/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

data = [
    average_daily,
    average_six_hourly.squeeze(),
    average_three_hourly.squeeze(),
    average_10min,
]

labels = ["daily", "six hourly", "three hourly", "10min"]
kolmogorov_smirnov_multi(data, labels)
"""
 Kolmogorov-Smirnov Test ('daily', 'daily'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0809, p-value=1.8570209167686834e-31
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0982, p-value=3.846424842476809e-38
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.1503, p-value=9.789928736183885e-56
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0809, p-value=1.8570209167686834e-31
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0181, p-value=0.10891448862921478
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0613, p-value=1.859152302795251e-09
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0982, p-value=3.846424842476809e-38
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0181, p-value=0.10891448862921478
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0589, p-value=6.7392682166069685e-06
 """
# load data
average_10min = np.load("data/Pickles/Fichtelberg/average_10min.npy")
day = np.load("data/Pickles/Fichtelberg/day.npy")
six_hour = np.load("data/Pickles/Fichtelberg/six_hour.npy")
three_hour = np.load("data/Pickles/Fichtelberg/three_hour.npy")
hour = np.load("data/Pickles/Fichtelberg/hour.npy")

data = [day, six_hour, three_hour, average_10min]
labels = ["daily", "six hourly", "three hourly", "10min"]
data = [
    pd.Series(day),
    pd.Series(six_hour),
    pd.Series(three_hour),
    pd.Series(average_10min),
]

kolmogorov_smirnov_multi(data, labels)

"""
 Kolmogorov-Smirnov Test ('daily', 'daily'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0591, p-value=0.8713300903073408
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0676, p-value=0.7323153131779815
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0619, p-value=0.779923171960191
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0591, p-value=0.8713300903073408
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0278, p-value=0.9999972795294731
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0596, p-value=0.7996745625362648
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0676, p-value=0.7323153131779815
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0278, p-value=0.9999972795294731
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0586, p-value=0.8079199493016505
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0619, p-value=0.779923171960191
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0596, p-value=0.7996745625362648
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0586, p-value=0.8079199493016505
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
