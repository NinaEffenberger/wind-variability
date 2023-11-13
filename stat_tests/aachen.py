"""
Kolmogorov-Smirnov tests for Aachen DWD data.
"""
import numpy as np
import pandas as pd
from src.kolmogorov_smirnov import kolmogorov_smirnov_multi

# load data
average_daily = np.load("data/Pickles/Aachen/average_daily.npy")
average_hourly = np.load("data/Pickles/Aachen/average_hourly.npy")
average_10min = np.load("data/Pickles/Aachen/average_10min.npy")
average_monthly = np.load("data/Pickles/Aachen/average_monthly.npy")
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0574, p-value=3.828806522783282e-14
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0677, p-value=1.4268909520610782e-21
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.1001, p-value=3.2439345611092308e-52
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0574, p-value=3.828806522783282e-14
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0159, p-value=0.0006110089770112652
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0472, p-value=1.763796865043759e-45
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0677, p-value=1.4268909520610782e-21
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0159, p-value=0.0006110089770112652
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0335, p-value=1.733386763800741e-44
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.1001, p-value=3.2439345611092308e-52
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0472, p-value=1.763796865043759e-45
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0335, p-value=1.733386763800741e-44
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
 """
# load data
average_10min = np.load("data/Pickles/Aachen/average_10min.npy")
day = np.load("data/Pickles/Aachen/day.npy")
six_hour = np.load("data/Pickles/Aachen/six_hour.npy")
three_hour = np.load("data/Pickles/Aachen/three_hour.npy")
hour = np.load("data/Pickles/Aachen/hour.npy")

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
 Kolmogorov-Smirnov Test ('daily', 'daily'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0725, p-value=2.889907579891722e-22
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0737, p-value=1.5359054093088526e-25
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0736, p-value=2.1372688885394643e-28
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0725, p-value=2.889907579891722e-22
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0042, p-value=0.9347495735440684
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0043, p-value=0.7851487208905541
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0737, p-value=1.5359054093088526e-25
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0042, p-value=0.9347495735440684
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0018, p-value=0.9990260082210362
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0736, p-value=2.1372688885394643e-28
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0043, p-value=0.7851487208905541
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0018, p-value=0.9990260082210362
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
