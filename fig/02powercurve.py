"""
Generate wind turbine power curve plot. Power curve used is E-92/2350.
"""
import matplotlib.pyplot as plt
import numpy as np
from tueplots import fonts

import matplotlib
import matplotlib.pyplot as plt
from windspeed_averages_wp import compute_windpower


matplotlib.rcParams.update({"font.size": 10})
matplotlib.rcParams.update({"axes.labelsize": 10})
matplotlib.rcParams.update({"legend.fontsize": 10})
matplotlib.rcParams.update({"xtick.labelsize": 10})
matplotlib.rcParams.update({"ytick.labelsize": 10})
matplotlib.rcParams.update({"axes.titlesize": 10})
plt.rcParams.update(fonts.neurips2021())

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)

speed = np.arange(0, 30, 0.01)

cut_in = 2
rated = 14
cut_out = 25

fig, ax = plt.subplots(1, 1, layout="constrained", figsize=(5.5, 3))
ax.set_xlabel(r"Wind speed ($\frac{m}{s}$)")
ax.set_ylabel(r"Power output (MW)")

plt.axvspan(0, 2, facecolor="#E69F00", alpha=0.2)
plt.axvspan(2, 14, facecolor="#56B4E9", alpha=0.2)
plt.axvspan(14, 25, facecolor="#009E73", alpha=0.2)
plt.axvspan(25, 30, facecolor="#E69F00", alpha=0.2)

#ax.set_xticks([0, 2, 5, 10, 14, 20, 25, 30])
ax.set_xticklabels(["0", f"2 \n(cut-in)", "5", "10", f"14 \n(rated)", "20", f"25 \n(cut-out)", "30"])

plt.plot(speed, compute_windpower(speed) / 1e6, color="black", linewidth=1)

plt.savefig("wind-variability/plots_eps/power_curve2.pdf")
plt.show()