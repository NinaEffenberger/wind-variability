import numpy as np
import pandas as pd
from src.kolmogorov_smirnov import kolmogorov_smirnov_multi

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
 Kolmogorov-Smirnov Test ('daily', 'daily'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0589, p-value=0.003004377743818124
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0660, p-value=0.0002247125086310759
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0713, p-value=1.4043290042199237e-05
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0589, p-value=0.003004377743818124
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0125, p-value=0.7116031243881392
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0184, p-value=0.0919906259577209
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0660, p-value=0.0002247125086310759
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0125, p-value=0.7116031243881392
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0088, p-value=0.49496567472482444
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0713, p-value=1.4043290042199237e-05
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0184, p-value=0.0919906259577209
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0088, p-value=0.49496567472482444
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0345, p-value=0.21415599353344622
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0325, p-value=0.2180868046326111
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0342, p-value=0.12944894622346792
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0345, p-value=0.21415599353344622
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0046, p-value=0.9999999161769726
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0070, p-value=0.9784358472156229
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0325, p-value=0.2180868046326111
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0046, p-value=0.9999999161769726
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0050, p-value=0.9774689239729787
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0342, p-value=0.12944894622346792
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0070, p-value=0.9784358472156229
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0050, p-value=0.9774689239729787
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
