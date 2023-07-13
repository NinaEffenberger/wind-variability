import matplotlib.pyplot as plt
import numpy as np
from tueplots import figsizes, fonts
import tueplots
import matplotlib

matplotlib.rcParams.update({"font.size": 12})

fig, ax = plt.subplots(1, 1, constrained_layout=True, figsize=(6, 4.5))

variances_kelmarsh_avrg = [7.698189673676312, 6.972512, 6.577039, 5.052492032572519]
variances_kelmarsh_inst = [
    7.698189673676312,
    7.6858677769507215,
    7.772831265670806,
    6.45822465651136,
]

variances_penmanshiel_avrg = [
    15.297405604103371,
    14.063801,
    13.211675,
    9.528542828020033,
]
variances_penmanshiel_inst = [
    15.297405604103371,
    15.266578469227156,
    15.11583509241062,
    13.415223442840588,
]

variances_nwtc_avrg = [13.020374298095703, 10.228503, 8.792633, 5.492742538452148]
variances_nwtc_inst = [13.020374298095703, 13.142364, 13.23959, 13.441619]

variances_owez_avrg = [16.54876136779785, 15.840661, 15.150413, 11.754743576049805]
variances_owez_inst = [16.54876136779785, 16.504244, 16.488329, 15.908951]

ax.plot(variances_kelmarsh_avrg, label="Kelmarsh", color="#E69F00")
ax.plot(variances_kelmarsh_inst, color="#E69F00", linestyle="dashed")
ax.plot(variances_penmanshiel_avrg, label="Penmanshiel", color="#56B4E9")
ax.plot(variances_penmanshiel_inst, color="#56B4E9", linestyle="dashed")
ax.plot(variances_nwtc_avrg, label="NWTC", color="#009E73")
ax.plot(variances_nwtc_inst, color="#009E73", linestyle="dashed")
ax.plot(variances_owez_avrg, label="Owez", color="#F0E442")
ax.plot(variances_owez_inst, color="#F0E442", linestyle="dashed")
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(["10min", "3h", "6h", "day"])
ax.set_xlabel(r"Resolution")
ax.set_ylabel(r"Variance ($\frac{m}{s}$)")
fig.legend(loc="outside right center")
plt.savefig("plots_eps/variances.eps")
