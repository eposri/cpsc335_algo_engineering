'''
Algorithm 2: "Matching Group Schedules"

Author Information
    Name: Kayla Ngo
    Email: kngo29@csu.fullerton.edu
    CWID: 885083436
    Course: CPSC 335-13

File Information:
    Name: functions.py
    Programming Language: Python 3.13.5
    Purpose: 
        Core scheduler logic of converting time stamps of unavailability into availability
        Formatting logic implementation
'''

scheduler = {}

def print_header(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)
    
def convert_minutes(time_stamp):
    hrs, min = map(int, time_stamp.split(":"))
    return min + (hrs * 60)

def convert_military(mins):
    hrs = mins // 60
    mins = mins % 60
    return f"{hrs:02}:{mins:02}"    # :02 for zeroes padding in interval

def convert_availability():
    START_TIME = 0
    END_TIME = 1439

    # iterate through master scheduler dict
    for name, schedule in scheduler.items():
        # access and sort minutes scheduler (stored in master scheduler dict)
        mins_schedule = sorted(schedule["mins"])

        # available scheduler list
        avail_mins = []
        avail = []

        prev_time = START_TIME - 1

        # iterate through minutes scheduler
        # inclusively taking into account unavailable time stamps (-/+ 1)
        for start, end in mins_schedule:
            # if start_time (in mins) > previous_time
            if start - 1 > prev_time + 1:
                # push back [previous_time, start_time]
                avail_start_time = convert_military(prev_time + 1)
                avail_end_time = convert_military(start - 1)
                avail_mins.append([prev_time + 1, start - 1])
                avail.append([avail_start_time, avail_end_time])
            prev_time = max(prev_time, end)

        # append remaining available time unless at END_TIME
        if prev_time + 1 <= END_TIME:
            avail_start_time = convert_military(prev_time + 1)
            avail_end_time = convert_military(END_TIME)
            avail_mins.append([prev_time + 1, END_TIME])
            avail.append([avail_start_time, avail_end_time])

        schedule["avail_mins"] = avail_mins
        schedule["avail"] = avail


def find_availabilities():
    print_header("Available Schedule to Meet")