import numpy as np
import pandas as pd
from kolmogorov_smirnov import kolmogorov_smirnov_multi

# load data
average_daily = np.load("data/Pickles/Zugspitze/average_daily.npy")
average_hourly = np.load("data/Pickles/Zugspitze/average_hourly.npy")
average_10min = np.load("data/Pickles/Zugspitze/average_10min.npy")
average_monthly = np.load("data/Pickles/Zugspitze/average_monthly.npy")
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0574, p-value=4.4723106687206186e-23
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0708, p-value=9.694012838141793e-39
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0917, p-value=2.7125494354963383e-72
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0574, p-value=4.4723106687206186e-23
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0151, p-value=1.15910505379362e-05
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0366, p-value=3.010154119032921e-45
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0708, p-value=9.694012838141793e-39
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0151, p-value=1.15910505379362e-05
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0224, p-value=4.90212105271763e-33
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0917, p-value=2.7125494354963383e-72
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0366, p-value=3.010154119032921e-45
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0224, p-value=4.90212105271763e-33
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
 """
# load data
average_10min = np.load("data/Pickles/Zugspitze/average_10min.npy")
day = np.load("data/Pickles/Zugspitze/day.npy")
six_hour = np.load("data/Pickles/Zugspitze/six_hour.npy")
three_hour = np.load("data/Pickles/Zugspitze/three_hour.npy")
hour = np.load("data/Pickles/Zugspitze/hour.npy")

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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0559, p-value=5.684269721098362e-22
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0557, p-value=3.590598395548388e-24
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0559, p-value=3.841266266525353e-27
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0559, p-value=5.684269721098362e-22
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0043, p-value=0.7133104144971305
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0046, p-value=0.38881498348337273
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0557, p-value=3.590598395548388e-24
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0043, p-value=0.7133104144971305
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0012, p-value=0.9999107338070624
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0559, p-value=3.841266266525353e-27
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0046, p-value=0.38881498348337273
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0012, p-value=0.9999107338070624
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
