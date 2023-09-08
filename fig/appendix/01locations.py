"""
Generate plot that shows locations of DWD data and CMIP6. 
"""

import cartopy
import cartopy.crs as ccrs
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
from matplotlib.lines import Line2D

matplotlib.rcParams.update({"font.size": 13})

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)

# Aachen
lon_aachen = 6.0941
lat_aachen = 50.7827

# Boltenhagen
lon_boltenhagen = 11.1908
lat_boltenhagen = 54.0027

# Zugspitze
lon_zugspitze = 10.9848
lat_zugspitze = 47.4210

# Fichtelberg
lon_fichtelberg = 11.8376
lat_fichtelberg = 49.9807

fig = plt.figure(figsize=(6, 4.5), layout="constrained")
ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax1.coastlines()
ax1.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())
ax1.set_extent([-1, 21, 40, 60], ccrs.PlateCarree())

plt.plot(
    [lon_aachen],
    [lat_aachen],
    marker="*",
    label="Aachen",
    color="#E69F00",
    markersize=8,
)
plt.plot(
    [lon_boltenhagen],
    [lat_boltenhagen],
    marker="o",
    label="Boltenhagen",
    color="#E69F00",
    markersize=6,
)
plt.plot(
    [lon_fichtelberg],
    [lat_fichtelberg],
    marker="^",
    label="Fichtelberg",
    color="#E69F00",
    markersize=8,
)
plt.plot(
    [lon_zugspitze],
    [lat_zugspitze],
    marker="s",
    label="Zugspitze",
    color="#E69F00",
    markersize=8,
)

# plt.legend()
legend_elements = [
    Line2D(
        [0],
        [0],
        marker="*",
        label="Aachen",
        color="w",
        markerfacecolor="#E69F00",
        markersize=15,
    ),
    Line2D(
        [0],
        [0],
        marker="o",
        label="Boltenhagen",
        markersize=12,
        markerfacecolor="#E69F00",
        color="w",
    ),
    Line2D(
        [0],
        [0],
        marker="^",
        label="Fichtelberg",
        markersize=12,
        markerfacecolor="#E69F00",
        color="w",
    ),
    Line2D(
        [0],
        [0],
        marker="s",
        label="Zugspitze",
        markersize=12,
        markerfacecolor="#E69F00",
        color="w",
    ),
    # Line2D([0], [0], marker="p", label="Boseong", markersize=12, markerfacecolor="darkred", color="w"),
]

# Aachen
lon_aachen_cmip = 5.63
lat_aachen_cmip = 51.29

# Boltenhagen
lon_boltenhagen_cmip = 11.25
lat_boltenhagen_cmip = 53.16

# Zugspitze
lon_zugspitze_cmip = 10.98
lat_zugspitze_cmip = 47.56

# Fichtelberg
lon_fichtelberg_cmip = 11.25
lat_fichtelberg_cmip = 49.43


plt.plot(
    [lon_aachen_cmip],
    [lat_aachen_cmip],
    marker="*",
    label="Aachen",
    color="#56B4E9",
    markersize=8,
)
plt.plot(
    [lon_boltenhagen_cmip],
    [lat_boltenhagen_cmip],
    marker="o",
    label="Boltenhagen",
    color="#56B4E9",
    markersize=6,
)
plt.plot(
    [lon_fichtelberg_cmip],
    [lat_fichtelberg_cmip],
    marker="^",
    label="Fichtelberg",
    color="#56B4E9",
    markersize=8,
)
plt.plot(
    [lon_zugspitze_cmip],
    [lat_zugspitze_cmip],
    marker="s",
    label="Zugspitze",
    color="#56B4E9",
    markersize=8,
)
# plt.plot([boseong_lon], [boseong_lat], marker="p", label="Boseong", color="darkred", markersize=8)

# plt.legend()
legend_elements = [
    Line2D(
        [0],
        [0],
        marker="*",
        label="Aachen",
        color="w",
        markerfacecolor="#56B4E9",
        markersize=15,
    ),
    Line2D(
        [0],
        [0],
        marker="o",
        label="Boltenhagen",
        markersize=12,
        markerfacecolor="#56B4E9",
        color="w",
    ),
    Line2D(
        [0],
        [0],
        marker="^",
        label="Fichtelberg",
        markersize=12,
        markerfacecolor="#56B4E9",
        color="w",
    ),
    Line2D(
        [0],
        [0],
        marker="s",
        label="Zugspitze",
        markersize=12,
        markerfacecolor="#56B4E9",
        color="w",
    ),
    # Line2D([0], [0], marker="p", label="Boseong", markersize=12, markerfacecolor="darkred", color="w"),
]

# ax1.add_feature(cartopy.feature.LAND)
# ax1.add_feature(cartopy.feature.OCEAN)
ax1.add_feature(cartopy.feature.COASTLINE, linewidth=0.3)
ax1.add_feature(cartopy.feature.BORDERS, linestyle=":", linewidth=0.3)
# ax1.add_feature(cartopy.feature.LAKES, alpha=0.5)
# ax1.add_feature(cartopy.feature.RIVERS)
ax1.legend(handles=legend_elements)
gl = ax1.gridlines(
    crs=ccrs.PlateCarree(),
    draw_labels=True,
    linewidth=2,
    color="gray",
    alpha=0.5,
    linestyle="--",
)
gl.xlabels_top = False
gl.ylabels_left = False
gl.xlines = False
gl.xlocator = mticker.FixedLocator([0, 10, 20])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {"size": 15, "color": "gray"}
gl.xlabel_style = {"color": "black", "weight": "bold"}
plt.savefig("plots_eps/locations_DWD.svg")
plt.show()
