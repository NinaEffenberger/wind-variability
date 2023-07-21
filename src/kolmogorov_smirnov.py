import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import ks_2samp


def prepare_dataframe(dist1, dist2):
    data = pd.DataFrame()
    dist1 = pd.Series(dist1)
    dist2 = pd.Series(dist2)
    data["windspeeds"] = np.sort(np.append(dist1.unique(), dist2.unique()))
    dist1 = dist1.values
    dist2 = dist2.values
    data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
    data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
    return data


def kolmogorov_smirnov_plot(data, k, y, ks_stat, label1, label2, savepath):
    fig, ax = plt.subplots(1, 1, figsize=(6, 4), constrained_layout=True)
    ax.plot("windspeeds", "dist1", data=data, label=label1)
    ax.plot("windspeeds", "dist2", data=data, label=label2)
    ax.errorbar(x=data["windspeeds"][k], y=y, yerr=ks_stat / 2, color="black", capsize=5, mew=3)
    ax.legend()
    ax.set_xlabel(r"$\frac{m}{s}$")
    ax.set_ylabel(r"cumulative density")
    plt.savefig(savepath)
    plt.show()


def kolmogorov_smirnov_multi(data, labels):
    for i in range(len(data)):
        for j in range(len(data)):
            stat, p_value = ks_2samp(data[i], data[j])
            print(f" Kolmogorov-Smirnov Test {labels[i], labels[j]}: statistic={stat:.4f}, p-value={p_value}")
