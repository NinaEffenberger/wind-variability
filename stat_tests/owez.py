import numpy as np
import pandas as pd
from distributions import compute_instantenous_windspeeds
from kolmogorov_smirnov import kolmogorov_smirnov_multi, plot_cumulative_densities_day
from windspeed_averages_wp import compute_average_windspeeds, drop_nans, load_data, set_date

# load data
average_daily = np.load("data/Pickles/Owez/average_daily.npy")
average_hourly = np.load("data/Pickles/Owez/average_hourly.npy")
average_10min = np.load("data/Pickles/Owez/average_10min.npy")
average_monthly = np.load("data/Pickles/Owez/average_monthly.npy")
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0557, p-value=2.77197183470813e-08
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0646, p-value=1.6515376986277868e-19
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0719, p-value=0.0
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0557, p-value=2.77197183470813e-08
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0118, p-value=0.28365342911155134
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0185, p-value=2.1538057839340156e-25
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0646, p-value=1.6515376986277868e-19
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0118, p-value=0.28365342911155134
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0088, p-value=3.75684692390376e-06
 """
# load data
average_10min = np.load("data/Pickles/Owez/average_10min.npy")
day = np.load("data/Pickles/Owez/day.npy")
six_hour = np.load("data/Pickles/Owez/six_hour.npy")
three_hour = np.load("data/Pickles/Owez/three_hour.npy")
hour = np.load("data/Pickles/Owez/hour.npy")

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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0336, p-value=0.0027697749254361865
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0314, p-value=6.0854711829753186e-05
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0341, p-value=3.961224242835922e-83
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0336, p-value=0.0027697749254361865
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0043, p-value=0.999473598588019
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0070, p-value=0.0005918308666556564
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0314, p-value=6.0854711829753186e-05
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0043, p-value=0.999473598588019
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0050, p-value=0.0255158316036308
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0341, p-value=3.961224242835922e-83
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0070, p-value=0.0005918308666556564
"""
