import csv


def break_apart_the_date_time(date_time):
    '''
    Breaks up the time stamp of the Muse data
    :param date_time: Timestamp
    :return: The year, month, day, hour, minute, and second converted into floats
    '''
    date_time_split = date_time.split()

    date_split = date_time_split[0].split('-')
    year = float(date_split[0])
    month = float(date_split[1])
    day = float(date_split[2])

    time_split = date_time_split[1].split(':')
    hour = float(time_split[0])
    minute = float(time_split[1])
    second = float(time_split[2])

    return year, month, day, hour, minute, second


def trim_data(file_loc, start_after_seconds=10, end_before_seconds=10):
    '''
    Loads the data, takes out the empty rows and entries before the first 'start_after_seconds' and after the last
    'end_before_seconds'
    :param file_loc: File location of the .csv file
    :param start_after_seconds: How many seconds to ignore at first
    :param end_before_seconds: How many seconds to ignore at the end
    :return: The trimmed data as a list of lists (each representing the different rows) and a list of the column names
    '''
    #  Open the file
    file = open(file_loc, 'r')
    csv_thing = csv.reader(file)

    #  Just grab everything
    data = []
    for row in csv_thing:
        data.append(row)

    column_names = data.pop(0)[:-1]
    start_year, start_month, start_day, start_hour, start_minute, start_second = break_apart_the_date_time(data[1][0])
    end_year, end_month, end_day, end_hour, end_minute, end_second = break_apart_the_date_time(data[-1][0])

    start_second += start_minute * 60 + (start_hour + (start_day + (start_month + start_year * 365) * 30) * 24) * 3600
    end_second += end_minute * 60 + (end_hour + (end_day + (end_month + end_year * 365) * 30) * 24) * 3600

    #  Trim out the null rows and ones outside our desired timezone
    final_data = []
    for row in data:
        year, month, day, hour, minute, second = break_apart_the_date_time(row[0])
        second += minute * 60 + (hour + (day + (month + year * 365) * 30) * 24) * 3600
        if second < start_second + start_after_seconds:
            continue

        if second > end_second - end_before_seconds:
            continue

        if '' == row[2]:
            continue
        final_data.append(row)

    #  Cut the time off
    timestamps = [final_data[i].pop(0) for i in range(len(final_data))]

    #  Convert everything to floats
    for row in range(len(final_data)):
        for col in range(len(final_data[0])):
            if not final_data[row][col] == '':
                final_data[row][col] = float(final_data[row][col])

    return final_data, column_names, timestamps


def get_column_average(data, column):
    '''
    Averages a column of a data table
    :param data: Data table
    :param column: Desired column to average
    :return: Average of the column
    '''
    return sum([data[row][column] for row in range(len(data))]) / len(data)


def print_table(data):
    '''
    Prints out a table row by row
    :param data: Data table
    :return: None
    '''
    for row in data:
        print(row)


def pivot_data(data):
    '''
    Pivots the table (turns rows into columns and columns into rows)
    :param data: Data to pivot
    :return: Pivoted data list
    '''
    return [[data[row][col] for row in range(len(data))] for col in range(len(data[0]))]


def call(csvFile):
    #  This if statement will only run if you 'run' this .py file
    #  It won't run if you import this .py file to another (or just copy and paste the function)
    should_i_print_everything = False  # Change back to true later if you want to debug
    desired_data, column_names, timestamps = trim_data(csvFile, 10, 10)

    desired_data_pivot = pivot_data(desired_data)

    if should_i_print_everything:
        print("COLUMN NAMES")
        print(column_names)

    Gamma_TP9 = get_column_average(desired_data, 16)
    Gamma_AF7 = get_column_average(desired_data, 17)
    Gamma_AF8 = get_column_average(desired_data, 18)
    Gamma_TP10 = get_column_average(desired_data, 19)
    Beta_TP9 = get_column_average(desired_data, 12)
    Beta_AF7 = get_column_average(desired_data, 13)
    Beta_AF8 = get_column_average(desired_data, 14)
    Beta_TP10 = get_column_average(desired_data, 15)
    Threshold1 = -1.0438801960382091
    Threshold2 = -0.9
    Threshold3 = -0.6
    Threshold4 = 0.16

    if should_i_print_everything:
        # print()
        print("DATA")
        print_table(desired_data)
        print("GAMMA TP9 AVERAGE")
        print(Gamma_TP9)
        print()
        print("GAMMA AF7 AVERAGE")
        print(Gamma_AF7)
        print()
        print("GAMMA AF8 AVERAGE")
        print(Gamma_AF8)
        print()
        print("GAMMA TP10 AVERAGE")
        print(Gamma_TP10)
        print()
        print("BETA TP9 AVERAGE")
        print(Beta_TP9)
        print()
        print("BETA AF7 AVERAGE")
        print(Beta_AF7)
        print()
        print("BETA AF8 AVERAGE")
        print(Beta_AF8)
        print()
        print("BETA TP10 AVERAGE")
        print(Beta_TP10)
        print()
        print()
        print()
    if (Gamma_TP9 > Threshold1) and (Beta_TP10 <= Threshold4):
        print("User is perceived happy; playing video recording")
        return 1

    if (Gamma_AF7 > Threshold2) and (Beta_AF7 > Threshold3):
        print("Don't be sad, here's one of your motivational quotes")
        return 0
