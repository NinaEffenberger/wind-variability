import numpy as np
import pandas as pd
from distributions import compute_instantenous_windspeeds
from kolmogorov_smirnov import (kolmogorov_smirnov_multi,
                                plot_cumulative_densities_day)
from windspeed_averages_wp import (compute_average_windspeeds, drop_nans,
                                   load_data, set_date)

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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.1159, p-value=8.154849868197042e-11
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.1419, p-value=9.12532189801082e-18
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.1854, p-value=1.3483897346143757e-33
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.1159, p-value=8.154849868197042e-11
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0372, p-value=0.0005533927552870619
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0964, p-value=2.5106383484414674e-35
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.1419, p-value=9.12532189801082e-18
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0372, p-value=0.0005533927552870619
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0607, p-value=2.447801712288526e-27
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.1854, p-value=1.3483897346143757e-33
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0964, p-value=2.5106383484414674e-35
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0607, p-value=2.447801712288526e-27
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0374, p-value=0.16412746432009076
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0446, p-value=0.038445458193930915
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0425, p-value=0.03605576774473984
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0374, p-value=0.16412746432009076
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0127, p-value=0.7218066811311489
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0114, p-value=0.6202395366905521
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0446, p-value=0.038445458193930915
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0127, p-value=0.7218066811311489
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0062, p-value=0.9011759344639219
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0425, p-value=0.03605576774473984
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0114, p-value=0.6202395366905521
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0062, p-value=0.9011759344639219
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
