"""
Kolmogorov-Smirnov tests for Boltenhagen DWD data.
"""
import numpy as np
import pandas as pd
from kolmogorov_smirnov import kolmogorov_smirnov_multi

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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0678, p-value=9.767473104391658e-34
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0771, p-value=2.929461347460807e-48
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0973, p-value=1.3933983422819363e-85
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0678, p-value=9.767473104391658e-34
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0148, p-value=1.0427296032135527e-05
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0354, p-value=1.6908743657158513e-44
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0771, p-value=2.929461347460807e-48
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0148, p-value=1.0427296032135527e-05
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0225, p-value=4.2251714431820167e-35
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0973, p-value=1.3933983422819363e-85
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0354, p-value=1.6908743657158513e-44
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0225, p-value=4.2251714431820167e-35
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('daily', 'daily'): statistic=0.0000, p-value=1.0
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0648, p-value=7.140961202934325e-31
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0651, p-value=1.7156006025944347e-34
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0652, p-value=1.0861076330334901e-38
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0648, p-value=7.140961202934325e-31
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0039, p-value=0.7837570302338003
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0046, p-value=0.35875274391934486
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0651, p-value=1.7156006025944347e-34
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0039, p-value=0.7837570302338003
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0011, p-value=0.9999643727062124
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0652, p-value=1.0861076330334901e-38
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0046, p-value=0.35875274391934486
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0011, p-value=0.9999643727062124
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
