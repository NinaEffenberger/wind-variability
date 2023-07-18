import numpy as np
import pandas as pd
from distributions import compute_instantenous_windspeeds
from kolmogorov_smirnov import kolmogorov_smirnov_multi, plot_cumulative_densities_day
from windspeed_averages_wp import compute_average_windspeeds, drop_nans, load_data, set_date

# load data
average_daily = np.load("data/Pickles/Boltenhagen/average_daily.npy")
average_hourly = np.load("data/Pickles/Boltenhagen/average_hourly.npy")
average_10min = np.load("data/Pickles/Boltenhagen/average_10min.npy")
average_monthly = np.load("data/Pickles/Boltenhagen/average_monthly.npy")
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0513, p-value=2.6664552159478674e-19
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0582, p-value=9.292538511322408e-21
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0926, p-value=2.90734305132469e-30
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0513, p-value=2.6664552159478674e-19
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0168, p-value=0.029853733958078
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0386, p-value=3.0644423876934578e-06
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0582, p-value=9.292538511322408e-21
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0168, p-value=0.029853733958078
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0281, p-value=0.0138321517515406
"""
# load data
average_10min = np.load("data/Pickles/Boltenhagen/average_10min.npy")
day = np.load("data/Pickles/Boltenhagen/day.npy")
six_hour = np.load("data/Pickles/Boltenhagen/six_hour.npy")
three_hour = np.load("data/Pickles/Boltenhagen/three_hour.npy")
hour = np.load("data/Pickles/Boltenhagen/hour.npy")

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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0368, p-value=0.9591127984507057
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0309, p-value=0.9925973567833708
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0835, p-value=0.09887116885861157
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0368, p-value=0.9591127984507057
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0097, p-value=0.9999999999999999
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0481, p-value=0.6653446610682076
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0309, p-value=0.9925973567833708
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0097, p-value=0.9999999999999999
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0473, p-value=0.6759313829221498
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0835, p-value=0.09887116885861157
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0481, p-value=0.6653446610682076
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0473, p-value=0.6759313829221498
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
