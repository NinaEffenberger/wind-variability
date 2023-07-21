"""
Kolmogorov-Smirnov tests for Fichtelberg DWD data.
"""
import numpy as np
import pandas as pd
from src.kolmogorov_smirnov import kolmogorov_smirnov_multi

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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.1334, p-value=4.201698401838888e-108
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.1556, p-value=2.0442428851164282e-163
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.1874, p-value=3.6023667605555054e-265
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.1334, p-value=4.201698401838888e-108
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0292, p-value=1.4724610922025357e-17
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0798, p-value=1.6398440131048566e-187
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.1556, p-value=2.0442428851164282e-163
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0292, p-value=1.4724610922025357e-17
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0567, p-value=6.612480227934571e-184
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.1874, p-value=3.6023667605555054e-265
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0798, p-value=1.6398440131048566e-187
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0567, p-value=6.612480227934571e-184
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.1170, p-value=4.338951683268464e-83
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.1319, p-value=2.0591254870539382e-117
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.1342, p-value=1.2719367070964248e-135
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.1170, p-value=4.338951683268464e-83
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0163, p-value=9.018376305091602e-06
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0197, p-value=7.674496243858464e-12
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.1319, p-value=2.0591254870539382e-117
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0163, p-value=9.018376305091602e-06
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0034, p-value=0.42398819694389955
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.1342, p-value=1.2719367070964248e-135
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0197, p-value=7.674496243858464e-12
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0034, p-value=0.42398819694389955
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
