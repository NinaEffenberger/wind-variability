import numpy as np
import pandas as pd
from distributions import compute_instantenous_windspeeds
from kolmogorov_smirnov import kolmogorov_smirnov_multi, plot_cumulative_densities_day
from windspeed_averages_wp import compute_average_windspeeds, drop_nans, load_data, set_date

# load data
average_daily = np.load("data/Pickles/Penmanshiel/average_daily.npy")
average_hourly = np.load("data/Pickles/Penmanshiel/average_hourly.npy")
average_10min = np.load("data/Pickles/Penmanshiel/average_10min.npy")
average_monthly = np.load("data/Pickles/Penmanshiel/average_monthly.npy")
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0544, p-value=3.238228091853968e-10
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0634, p-value=2.643133636829117e-24
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0781, p-value=0.0
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0544, p-value=3.238228091853968e-10
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0128, p-value=0.09822367252652076
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0300, p-value=6.233699979697762e-55
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0634, p-value=2.643133636829117e-24
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0128, p-value=0.09822367252652076
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0165, p-value=9.994445343802028e-18
 """
# load data
average_10min = np.load("data/Pickles/Penmanshiel/average_10min.npy")
day = np.load("data/Pickles/Penmanshiel/day.npy")
six_hour = np.load("data/Pickles/Penmanshiel/six_hour.npy")
three_hour = np.load("data/Pickles/Penmanshiel/three_hour.npy")
hour = np.load("data/Pickles/Penmanshiel/hour.npy")

data = [day, six_hour, three_hour, average_10min]
labels = ["daily", "six hourly", "three hourly", "10min"]
# plot_cumulative_densities(data, labels, "plots/open-source/Penmanshiel/1/cumulative_densities")
data = [
    pd.Series(day),
    pd.Series(six_hour),
    pd.Series(three_hour),
    pd.Series(average_10min),
]

kolmogorov_smirnov_multi(data, labels)

"""
 Kolmogorov-Smirnov Test ('daily', 'daily'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0378, p-value=0.00030182274176927283
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0379, p-value=8.935135100650947e-07
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0403, p-value=1.7333416525671926e-95
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0378, p-value=0.00030182274176927283
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0056, p-value=0.9826734181032695
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0071, p-value=0.0018986394858219722
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0379, p-value=8.935135100650947e-07
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0056, p-value=0.9826734181032695
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0061, p-value=0.009193847159301346
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0403, p-value=1.7333416525671926e-95
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0071, p-value=0.0018986394858219722
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0061, p-value=0.009193847159301346
"""
