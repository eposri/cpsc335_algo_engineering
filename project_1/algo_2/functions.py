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

#def convert_military(mins):

def convert_availability():
    START_TIME = 0
    END_TIME = 1439

    # sort minutes scheduler (stored in master scheduler dict)
