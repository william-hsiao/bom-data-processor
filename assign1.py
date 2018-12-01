#####################################
# Support given below - DO NOT CHANGE
#####################################

from assign1_support import *

#####################################
# End of support
#####################################

# Add your code here
def load_data(stations_file):
    """Return the list of station names

    load_stations() -> list(str)
    """
    fd = open(stations_file, "r")
    stations = []
    for line in fd:
        line = line.strip()
        if not line:
            continue
        stations.append(line)
    fd.close()
    return stations


def load_dates(stations):
    """Return list of all dates in the data set

       load_dates(list(str)) -> list(str)
       """
    date_list = []
    for stat in stations:
        station1 = load_data(stat+'.txt')
        for line in station1:
            date, temp = line.split(sep=None)
            date_list += [date]
        return date_list


def load_station_data(station):
    """Returns a list of the temperatures of the inputted station name

       load_station_data(str) -> list(float)
       """
    temp_list = []
    station1 = load_data(station+'.txt')
    for line in station1:
        date, temp = line.split(sep=None)
        temp_list += [float(temp)]
    return temp_list

def load_all_stations_data(stations):
    """Returns a list of lists of data for each stations

       load_all_stations_data(station) -> list(list(float))
       """
    temp_list = []
    for stat in stations:
        station1 = load_data(stat+'.txt')
        station_temp = []
        for line in station1:
            date, temp = line.split(sep=None)
            station_temp += [float(temp)]
        temp_list += [station_temp]
    return temp_list


def display_maxs(stations, dates, data, start_date, end_date):
    """Returns a table with maximum temperatures of the given stations
       within the dates provided

       display_maxs(list, list, list, str, str) -> None
       """
    count = 0

    display_stations(stations, 'Date')

    for date in dates:
        if date >= start_date:
            print (date, end='    ')
            for i in data:
                display_temp(float(i[count]))
            print ('', end='\n')
            count += 1
            if date == end_date:
                break
        else:
            count += 1


def temperature_diffs(data, dates, stations, station1, station2, start_date, end_date):
    """Returns a list of temperature differences between two stations
       within the range of dates

       temperature_diffs(list, list, list, str, str, str, str) -> list((str, float))
       """
    count = 0
    temp_diff = []
    for num, station in enumerate(stations):
        if station == station1:
            station_1 = num
        if station == station2:
            station_2 = num

    for date in dates:
        if date >= start_date:
            temp_difference = float(data[station_1][count])-float(data[station_2][count])
            if float(data[station_1][count]) == UNKNOWN_TEMP or float(data[station_2][count])== UNKNOWN_TEMP:
                temp_difference = UNKNOWN_TEMP
            dataset = (date, temp_difference)
            temp_diff.append(dataset)
            count += 1
            if date == end_date:
                break
        else:
            count += 1
    return temp_diff


def display_diffs(diffs, station1, station2):
    """Displays the data from temperature_diffs in a table format

       display_diffs(list, str, str) -> None
       """
    print ('Temperature differences between', station1, 'and', station2)
    print ()
    print ('Date      Temperature Differences')
    for line in diffs:
        date, temp = line
        print (date, end = "  ")
        display_temp(temp)
        print ('', end='\n')


def interact():
    """
    Initialises interactive loop

    interact() -> None
    """

    print ("Welcome to BOM Data")
    print()
    stations = load_stations(input ("Please enter the name of the Stations file: "))
    data = load_all_stations_data(stations)
    dates = load_dates(stations)
    print()
    while True:
        command = input("Command: ")
        command = command.split(sep=None)
        if command[0] == 'dm':
            if len(command) == 3:
                print()
                display_maxs(stations, dates, data, command[1], command[2])
            else:
                print('Error: Invalid number of arguments')
            print()
        elif command[0] == 'dd':
            if len(command) == 5:
                print()
                diffs = temperature_diffs(data, dates, stations, command[1], command[2], command[3], command[4])
                display_diffs(diffs, command[1], command[2])
            else:
                print('Error: Invalid number of arguments')
            print()
        elif command[0] == 'q':
            exit()
        else:
            if command[0] != 'dm' or command[0] != 'dd':
                print('Unknown command:', command[0])
            else:
                print('Error: Invalid input')
            print()



##################################################
# !!!!!! Do not change (or add to) the code below !!!!!
#
# This code will run the interact function if
# you use Run -> Run Module  (F5)
# Because of this we have supplied a "stub" definition
# for interact above so that you won't get an undefined
# error when you are writing and testing your other functions.
# When you are ready please change the definition of interact above.
###################################################

if __name__ == '__main__':
    interact()
