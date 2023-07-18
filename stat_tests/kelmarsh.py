import numpy as np
import pandas as pd
from distributions import compute_instantenous_windspeeds
from kolmogorov_smirnov import (kolmogorov_smirnov_multi,
                                plot_cumulative_densities_day)
from windspeed_averages_wp import (compute_average_windspeeds, drop_nans,
                                   load_data, set_date)

# load data
average_daily = np.load("data/Pickles/Kelmarsh/average_daily.npy")
average_hourly = np.load("data/Pickles/Kelmarsh/average_hourly.npy")
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
average_monthly = np.load("data/Pickles/Kelmarsh/average_monthly.npy")
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0498, p-value=1.6423710725827929e-09
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0589, p-value=2.5358878251973288e-23
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0758, p-value=0.0
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0498, p-value=1.6423710725827929e-09
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0124, p-value=0.08824540253242008
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0304, p-value=5.580328164903298e-94
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0589, p-value=2.5358878251973288e-23
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0124, p-value=0.08824540253242008
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0186, p-value=1.1608901526254417e-36
 """
# load data
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
day = np.load("data/Pickles/Kelmarsh/day.npy")
six_hour = np.load("data/Pickles/Kelmarsh/six_hour.npy")
three_hour = np.load("data/Pickles/Kelmarsh/three_hour.npy")
hour = np.load("data/Pickles/Kelmarsh/hour.npy")

data = [day, six_hour, three_hour, average_10min]
labels = ["daily", "six hourly", "three hourly", "10min"]
# plot_cumulative_densities(data, labels, "plots/open-source/Kelmarsh/1/cumulative_densities")
data = [
    pd.Series(day),
    pd.Series(six_hour),
    pd.Series(three_hour),
    pd.Series(average_10min),
]

kolmogorov_smirnov_multi(data, labels)

"""
 Kolmogorov-Smirnov Test ('daily', 'daily'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0410, p-value=1.5336442165813965e-06
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0432, p-value=1.5099775189714566e-12
 Kolmogorov-Smirnov Test ('daily', 'hourly'): statistic=0.0437, p-value=3.629088855375539e-34
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0447, p-value=1.5154700401739405e-198
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0410, p-value=1.5336442165813965e-06
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0044, p-value=0.9895941070997902
 Kolmogorov-Smirnov Test ('six hourly', 'hourly'): statistic=0.0061, p-value=0.35642097970320874
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0058, p-value=0.0007278475269286892
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0432, p-value=1.5099775189714566e-12
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0044, p-value=0.9895941070997902
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', 'hourly'): statistic=0.0026, p-value=0.9942497937215704
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0028, p-value=0.3045494682213328
"""
