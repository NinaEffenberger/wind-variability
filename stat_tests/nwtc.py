import numpy as np
import pandas as pd
from distributions import compute_instantenous_windspeeds
from kolmogorov_smirnov import kolmogorov_smirnov_multi, plot_cumulative_densities_day
from windspeed_averages_wp import compute_average_windspeeds, drop_nans, load_data, set_date

# load data
average_daily = np.load("data/Pickles/NWTC/average_daily.npy")
average_hourly = np.load("data/Pickles/NWTC/average_hourly.npy")
average_10min = np.load("data/Pickles/NWTC/average_10min.npy")
average_monthly = np.load("data/Pickles/NWTC/average_monthly.npy")
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.1122, p-value=8.678664786055666e-31
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.1382, p-value=1.8637369014042177e-83
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.1851, p-value=0.0
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.1122, p-value=8.678664786055666e-31
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0368, p-value=3.045310501607408e-08
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0962, p-value=0.0
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.1382, p-value=1.8637369014042177e-83
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0368, p-value=3.045310501607408e-08
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0608, p-value=1.5322520788427077e-267
"""
# load data
average_10min = np.load("data/Pickles/NWTC/average_10min.npy")
day = np.load("data/Pickles/NWTC/day.npy")
six_hour = np.load("data/Pickles/NWTC/six_hour.npy")
three_hour = np.load("data/Pickles/NWTC/three_hour.npy")
hour = np.load("data/Pickles/NWTC/hour.npy")

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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0363, p-value=0.001412988991145583
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0443, p-value=6.770467319791519e-09
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0427, p-value=3.24684190086108e-126
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0363, p-value=0.001412988991145583
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0127, p-value=0.23480751422830415
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0114, p-value=1.4524366747311557e-09
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0443, p-value=6.770467319791519e-09
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0127, p-value=0.23480751422830415
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0061, p-value=0.003982009401393227
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0427, p-value=3.24684190086108e-126
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0114, p-value=1.4524366747311557e-09
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0061, p-value=0.003982009401393227
"""
