import calendar

# from readline import read_init_file
import json
from sqlite3 import Date
from typing import List


def read_data(filename):
    try:
        file = open(filename, "r")
        data = json.loads(file.readline())
        file.close()
        return data

    except FileNotFoundError:
        # raise Exception("File does not exist. Please try again.")
        print("File: " + filename + " not found. Please try again.")
        empty = dict()
        return empty


def write_data(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)


def max_temperature(data, date):
    if len(data) == 0:
        raise Exception("No weather data loaded")

    valid_info = [dict for key, dict in data.items() if key.startswith(date)]
    temps = []
    for dict in valid_info:
        temps.append(dict["t"])

    return max(temps)


def min_temperature(data, date):
    if len(data) == 0:
        raise Exception("No weather data loaded")

    valid_info = [dict for key, dict in data.items() if key.startswith(date)]
    temps = []
    for dict in valid_info:
        temps.append(dict["t"])

    return min(temps)


def max_humidity(data, date):
    if len(data) == 0:
        raise Exception("No weather data loaded")

    valid_info = [dict for key, dict in data.items() if key.startswith(date)]
    moists = []
    for dict in valid_info:
        moists.append(dict["h"])

    return max(moists)


def min_humidity(data, date):
    if len(data) == 0:
        raise Exception("No weather data loaded")

    valid_info = [dict for key, dict in data.items() if key.startswith(date)]
    moists = []
    for dict in valid_info:
        moists.append(dict["h"])

    return min(moists)


def tot_rain(data, date):
    if len(data) == 0:
        raise Exception("No weather data loaded")

    valid_info = [dict for key, dict in data.items() if key.startswith(date)]
    rains = []
    for dict in valid_info:
        rains.append(dict["r"])

    return sum(rains)


def report_daily(data, date):
    if len(data) == 0:
        raise Exception("No weather data available")

    # creates list of dictionaries containing weather info for specified date
    # dats = [val for key, val in data.items() if key.startswith(date)]

    report = "========================= DAILY REPORT ========================\n"
    report += "Date                      Time  Temperature  Humidity  Rainfall\n"
    report += "====================  ========  ===========  ========  ========\n"

    date_string = str(date)

    # Create date strings for convience
    year = date_string[:4]
    mint = int(date_string[4:6])
    month = calendar.month_name[mint]
    day = date_string[6:8]
    if day[0] == "0":
        day = day[1]

    # Find every instance of date while retaining
    for key, info in data.items():
        # Prints info for every day matched
        if key.startswith(date):
            # Prints date
            report += (month + " " + day + ", " + year).ljust(22)

            # Prints time
            report += key[8:10] + ":" + key[10:12] + ":" + key[12:]
            # Prints Temp, humidity, and rain
            report += (
                str(info["t"]).rjust(13)
                + str(info["h"]).rjust(10)
                + "{:.2f}".format(info["r"]).rjust(10)
                + "\n"
            )

    return report


def report_historical(data):
    if len(data) == 0:
        return "No weather data available"

    # creates list of dictionaries containing weather info for specified date
    # dats = [val for key, val in data.items() if key.startswith(date)]

    report = (
        "============================== HISTORICAL REPORT ===========================\n"
    )
    report += (
        "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    )
    report += (
        "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    )
    report += (
        "====================  ===========  ===========  ========  ========  ========\n"
    )

    days = []

    # Find every instance of date while retaining
    for key, info in data.items():
        year = key[:4]
        mint = int(key[4:6])
        month = calendar.month_name[mint]
        day = key[6:8]
        if day[0] == "0":
            day = day[1]

        date = key[:8]
        date_string = month + " " + day + ", " + year
        # Prints info for every day matched
        if date not in days:
            days.append(date)

            # add date's weather info to report
            report += date_string.ljust(20) + " "
            report += str(min_temperature(data, date)).rjust(12) + " "
            report += str(max_temperature(data, date)).rjust(12) + " "
            report += str(min_humidity(data, date)).rjust(9) + " "
            report += str(max_humidity(data, date)).rjust(9) + " "
            report += "{:.2f}".format(tot_rain(data, date)).rjust(9) + "\n"

    return report
