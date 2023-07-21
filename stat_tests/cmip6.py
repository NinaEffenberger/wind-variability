import numpy as np
from kolmogorov_smirnov import kolmogorov_smirnov_multi


time_series_day = np.load("data/cmip6/data/Aachen/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Aachen/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Aachen/time_series_three.npy")
data = [time_series_day, time_series_six, time_series_three]
labels = ["day", "six hourly", " three hourly"]
kolmogorov_smirnov_multi(data, labels)
"""
 Kolmogorov-Smirnov Test ('day', 'day'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('day', 'six hourly'): statistic=0.0445, p-value=1.7249093949531443e-10
 Kolmogorov-Smirnov Test ('day', ' three hourly'): statistic=0.0490, p-value=5.6728283049345984e-14
 Kolmogorov-Smirnov Test ('six hourly', 'day'): statistic=0.0445, p-value=1.7249093949531443e-10
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 NSIG Kolmogorov-Smirnov Test ('six hourly', ' three hourly'): statistic=0.0052, p-value=0.6575096547853748
 Kolmogorov-Smirnov Test (' three hourly', 'day'): statistic=0.0490, p-value=5.6728283049345984e-14
 Kolmogorov-Smirnov Test (' three hourly', 'six hourly'): statistic=0.0052, p-value=0.6575096547853748
 Kolmogorov-Smirnov Test (' three hourly', ' three hourly'): statistic=0.0000, p-value=1.0
 """
time_series_day = np.load("data/cmip6/data/Zugspitze/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Zugspitze/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Zugspitze/time_series_three.npy")
data = [time_series_day, time_series_six, time_series_three]
labels = ["day", "six hourly", " three hourly"]
kolmogorov_smirnov_multi(data, labels)
"""
Kolmogorov-Smirnov Test ('day', 'day'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('day', 'six hourly'): statistic=0.0597, p-value=1.6158804300804818e-18
 Kolmogorov-Smirnov Test ('day', ' three hourly'): statistic=0.0661, p-value=4.130501434963952e-25
 Kolmogorov-Smirnov Test ('six hourly', 'day'): statistic=0.0597, p-value=1.6158804300804818e-18
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 NSIG Kolmogorov-Smirnov Test ('six hourly', ' three hourly'): statistic=0.0080, p-value=0.16344021510298734
 Kolmogorov-Smirnov Test (' three hourly', 'day'): statistic=0.0661, p-value=4.130501434963952e-25
 Kolmogorov-Smirnov Test (' three hourly', 'six hourly'): statistic=0.0080, p-value=0.16344021510298734
 Kolmogorov-Smirnov Test (' three hourly', ' three hourly'): statistic=0.0000, p-value=1.0
 """
time_series_day = np.load("data/cmip6/data/Boltenhagen/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Boltenhagen/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Boltenhagen/time_series_three.npy")
data = [time_series_day, time_series_six, time_series_three]
labels = ["day", "six hourly", " three hourly"]
kolmogorov_smirnov_multi(data, labels)
"""
Kolmogorov-Smirnov Test ('day', 'day'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('day', 'six hourly'): statistic=0.0472, p-value=9.123935887097292e-12
 Kolmogorov-Smirnov Test ('day', ' three hourly'): statistic=0.0514, p-value=2.2708426460783318e-15
 Kolmogorov-Smirnov Test ('six hourly', 'day'): statistic=0.0472, p-value=9.123935887097292e-12
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 NSIG Kolmogorov-Smirnov Test ('six hourly', ' three hourly'): statistic=0.0066, p-value=0.3554523229915444
 Kolmogorov-Smirnov Test (' three hourly', 'day'): statistic=0.0514, p-value=2.2708426460783318e-15
 Kolmogorov-Smirnov Test (' three hourly', 'six hourly'): statistic=0.0066, p-value=0.3554523229915444
 Kolmogorov-Smirnov Test (' three hourly', ' three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('day', 'day'): statistic=0.0000, p-value=1.0
 """
time_series_day = np.load("data/cmip6/data/Fichtelberg/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Fichtelberg/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Fichtelberg/time_series_three.npy")
data = [time_series_day, time_series_six, time_series_three]
labels = ["day", "six hourly", " three hourly"]
kolmogorov_smirnov_multi(data, labels)
"""
 Kolmogorov-Smirnov Test ('day', 'day'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('day', 'six hourly'): statistic=0.0561, p-value=2.1042034369021478e-16
 Kolmogorov-Smirnov Test ('day', ' three hourly'): statistic=0.0631, p-value=6.177171175491886e-23
 Kolmogorov-Smirnov Test ('six hourly', 'day'): statistic=0.0561, p-value=2.1042034369021478e-16
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 NSIG Kolmogorov-Smirnov Test ('six hourly', ' three hourly'): statistic=0.0077, p-value=0.2013793507915036
 Kolmogorov-Smirnov Test (' three hourly', 'day'): statistic=0.0631, p-value=6.177171175491886e-23
 Kolmogorov-Smirnov Test (' three hourly', 'six hourly'): statistic=0.0077, p-value=0.2013793507915036
 Kolmogorov-Smirnov Test (' three hourly', ' three hourly'): statistic=0.0000, p-value=1.0
 """
time_series_day = np.load("data/cmip6/data/Penmanshiel/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Penmanshiel/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Penmanshiel/time_series_three.npy")
data = [time_series_day, time_series_six, time_series_three]
labels = ["day", "six hourly", " three hourly"]
kolmogorov_smirnov_multi(data, labels)
"""
 Kolmogorov-Smirnov Test ('day', 'day'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('day', 'six hourly'): statistic=0.0484, p-value=2.5784452357315794e-12
 Kolmogorov-Smirnov Test ('day', ' three hourly'): statistic=0.0522, p-value=8.424038426836609e-16
 Kolmogorov-Smirnov Test ('six hourly', 'day'): statistic=0.0484, p-value=2.5784452357315794e-12
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 NSIG Kolmogorov-Smirnov Test ('six hourly', ' three hourly'): statistic=0.0055, p-value=0.5932694741321682
 Kolmogorov-Smirnov Test (' three hourly', 'day'): statistic=0.0522, p-value=8.424038426836609e-16
 Kolmogorov-Smirnov Test (' three hourly', 'six hourly'): statistic=0.0055, p-value=0.5932694741321682
 Kolmogorov-Smirnov Test (' three hourly', ' three hourly'): statistic=0.0000, p-value=1.0
 """
time_series_day = np.load("data/cmip6/data/Kelmarsh/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Kelmarsh/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Kelmarsh/time_series_three.npy")
data = [time_series_day, time_series_six, time_series_three]
labels = ["day", "six hourly", " three hourly"]
kolmogorov_smirnov_multi(data, labels)
""""
 Kolmogorov-Smirnov Test ('day', 'day'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('day', 'six hourly'): statistic=0.0491, p-value=1.0920920780815037e-12
 Kolmogorov-Smirnov Test ('day', ' three hourly'): statistic=0.0534, p-value=1.4791888229175729e-16
 Kolmogorov-Smirnov Test ('six hourly', 'day'): statistic=0.0491, p-value=1.0920920780815037e-12
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 NSIG Kolmogorov-Smirnov Test ('six hourly', ' three hourly'): statistic=0.0052, p-value=0.6736122574672213
 Kolmogorov-Smirnov Test (' three hourly', 'day'): statistic=0.0534, p-value=1.4791888229175729e-16
 Kolmogorov-Smirnov Test (' three hourly', 'six hourly'): statistic=0.0052, p-value=0.6736122574672213
 Kolmogorov-Smirnov Test (' three hourly', ' three hourly'): statistic=0.0000, p-value=1.0
 """
time_series_day = np.load("data/cmip6/data/NWTC/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/NWTC/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/NWTC/time_series_three.npy")
data = [time_series_day, time_series_six, time_series_three]
labels = ["day", "six hourly", " three hourly"]
kolmogorov_smirnov_multi(data, labels)
"""
 Kolmogorov-Smirnov Test ('day', 'day'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('day', 'six hourly'): statistic=0.1014, p-value=9.86787916864584e-53
 Kolmogorov-Smirnov Test ('day', ' three hourly'): statistic=0.1106, p-value=1.2121654527688842e-69
 Kolmogorov-Smirnov Test ('six hourly', 'day'): statistic=0.1014, p-value=9.86787916864584e-53
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', ' three hourly'): statistic=0.0115, p-value=0.011849031211049013
 Kolmogorov-Smirnov Test (' three hourly', 'day'): statistic=0.1106, p-value=1.2121654527688842e-69
 Kolmogorov-Smirnov Test (' three hourly', 'six hourly'): statistic=0.0115, p-value=0.011849031211049013
 Kolmogorov-Smirnov Test (' three hourly', ' three hourly'): statistic=0.0000, p-value=1.0
 """
time_series_day = np.load("data/cmip6/data/Owez/time_series_day.npy")
time_series_six = np.load("data/cmip6/data/Owez/time_series_six.npy")
time_series_three = np.load("data/cmip6/data/Owez/time_series_three.npy")
data = [time_series_day, time_series_six, time_series_three]
labels = ["day", "six hourly", " three hourly"]
kolmogorov_smirnov_multi(data, labels)
"""
 Kolmogorov-Smirnov Test ('day', 'day'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('day', 'six hourly'): statistic=0.0414, p-value=3.817033087492428e-09
 Kolmogorov-Smirnov Test ('day', ' three hourly'): statistic=0.0440, p-value=2.2462118871604664e-11
 Kolmogorov-Smirnov Test ('six hourly', 'day'): statistic=0.0414, p-value=3.817033087492428e-09
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 NSIG Kolmogorov-Smirnov Test ('six hourly', ' three hourly'): statistic=0.0056, p-value=0.5734276169198496
 Kolmogorov-Smirnov Test (' three hourly', 'day'): statistic=0.0440, p-value=2.2462118871604664e-11
 Kolmogorov-Smirnov Test (' three hourly', 'six hourly'): statistic=0.0056, p-value=0.5734276169198496
 Kolmogorov-Smirnov Test (' three hourly', ' three hourly'): statistic=0.0000, p-value=1.0
 """
