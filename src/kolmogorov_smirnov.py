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


def compute_test(dist1, dist2):
    stat, p_value = kstest(dist1.values, dist2.values)
    print(f" Kolmogorov-Smirnov Test: statistic={stat:.4f}, p-value={p_value}")


def kolmogorov_smirnov_stat(data):
    k = np.argmax(np.abs(data["dist1"] - data["dist2"]))
    ks_stat = np.abs(data["dist2"][k] - data["dist1"][k])
    y = (data["dist2"][k] + data["dist1"][k]) / 2
    return k, ks_stat, y


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


def plot_cumulative_densities(distributions, labels, savepath):
    dist1, dist2, dist3, dist4, dist5, dist6 = distributions
    label1, label2, label3, label4, label5, label6 = labels
    data = pd.DataFrame()
    data["windspeeds"] = np.sort(
        np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist4.unique(), dist5.unique(), dist6.unique()))
    )
    dist1 = dist1.values
    dist2 = dist2.values
    dist3 = dist3.values
    dist4 = dist4.values
    dist5 = dist5.values
    dist6 = dist6.values
    data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
    data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
    data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
    data["dist4"] = data["windspeeds"].apply(lambda x: np.mean(dist4 <= x))
    data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
    data["dist6"] = data["windspeeds"].apply(lambda x: np.mean(dist6 <= x))
    plt.plot("windspeeds", "dist1", data=data, label=label1)
    plt.plot("windspeeds", "dist2", data=data, label=label2)
    plt.plot("windspeeds", "dist3", data=data, label=label3)
    plt.plot("windspeeds", "dist4", data=data, label=label4)
    plt.plot("windspeeds", "dist5", data=data, label=label5)
    plt.plot("windspeeds", "dist6", data=data, label=label6)
    plt.legend()
    plt.xlabel(r"$\frac{m}{s}$")
    plt.ylabel(r"cumulative density")
    plt.savefig(savepath)
    plt.show()


def plot_cumulative_densities_day(distributions, labels, savepath):
    dist1, dist2, dist3, dist4, dist5 = distributions
    label1, label2, label3, label4, label5 = labels
    data = pd.DataFrame()
    data["windspeeds"] = np.sort(
        np.concatenate((dist1.unique(), dist2.unique(), dist3.unique(), dist4.unique(), dist5.unique()))
    )
    dist1 = dist1.values
    dist2 = dist2.values
    dist3 = dist3.values
    dist4 = dist4.values
    dist5 = dist5.values
    data["dist1"] = data["windspeeds"].apply(lambda x: np.mean(dist1 <= x))
    data["dist2"] = data["windspeeds"].apply(lambda x: np.mean(dist2 <= x))
    data["dist3"] = data["windspeeds"].apply(lambda x: np.mean(dist3 <= x))
    data["dist4"] = data["windspeeds"].apply(lambda x: np.mean(dist4 <= x))
    data["dist5"] = data["windspeeds"].apply(lambda x: np.mean(dist5 <= x))
    plt.plot("windspeeds", "dist1", data=data, label=label1)
    plt.plot("windspeeds", "dist2", data=data, label=label2)
    plt.plot("windspeeds", "dist3", data=data, label=label3)
    plt.plot("windspeeds", "dist4", data=data, label=label4)
    plt.plot("windspeeds", "dist5", data=data, label=label5)
    plt.legend()
    plt.xlabel(r"$\frac{m}{s}$")
    plt.ylabel(r"cumulative density")
    plt.savefig(savepath)
    plt.show()


def kolmogorov_smirnov_multi(data, labels):
    for i in range(len(data)):
        for j in range(len(data)):
            stat, p_value = ks_2samp(data[i], data[j])
            print(f" Kolmogorov-Smirnov Test {labels[i], labels[j]}: statistic={stat:.4f}, p-value={p_value}")
