from weather import *

# import calendar

myfile = "weather.dat"
mychoice = 0

while True:
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print()
    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("9. Exit the program")
    print()
    mychoice = int(input("Enter menu choice: "))
    print()

    if mychoice == 1:
        myfile = input("Enter data filename: ")
        weather = read_data(filename=myfile)

    elif mychoice == 2:
        dt = input("Enter date: ")
        tm = input("Enter time: ")
        t = int(input("Enter temperature: "))
        h = int(input("Enter humidity: "))
        r = float(input("Enter rainfall: "))
        weather[dt + tm] = {"t": t, "h": h, "r": r}
        write_data(data=weather, filename=myfile)

    elif mychoice == 3:
        d = input("Enter date: ")
        display = report_daily(data=weather, date=d)
        print(display)

    elif mychoice == 4:

        display = report_historical(data=weather)
        print(display)

    elif mychoice == 9:
        break
