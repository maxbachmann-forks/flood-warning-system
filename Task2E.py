# Copyright (C) 2020 Ghifari Pradana & Weixuan Zhang
#
# SPDX-License-Identifier: MIT

from datetime import timedelta

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)
    high_risk_stations = stations_highest_rel_level(stations, 5)
    dt = 10

    for station in high_risk_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
        plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
