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
        Main() function entry point for the algorithm 2 program 
'''

from functions import *

def add_schedule():
    print_header("New Schedule Entry")

    name = input("Enter person's name: ").strip()

    scheduler[name] = {
        "unavail": [],
        "mins": [],
        "avail": []
    }

    while True:
        print(f"Beginning time entry for {name}'s schedule. Enter 'q' to exit when finished.")

        start = input("Unavailable start time (HH:MM): ").strip()
        if start.lower() == "q":
            break

        end = input("Unavailable end time (HH:MM): ").strip()

        scheduler[name]["unavail"].append([start, end])
        
        # for logic in functions.py to convert to availability
        start_min = convert_minutes(start)
        end_min = convert_minutes(end)
        scheduler[name]["mins"].append([start_min, end_min])
        
        # storing data for printing purposes in view_all_schedule
        # debuggin: print(f"\nCurrent unavailability for {name}: {scheduler[name]["unavail"]}")
        #print(f"\nCurrent unavailability for {name}: {scheduler[name]["mins"]}")
        #availability = convert_availability(unavailability)
    
    #convert_availability()



def view_all_schedules():
    print_header("Schedules")
    for name, schedule in scheduler.items():
        print(f"\n{name}'s unavailable schedule: {schedule["unavail"]}")
        print(f"\n{name}'s minutes schedule: {schedule["mins"]}")
        #print(f"\n{name}'s available schedule: {schedule["avail"]}")

def menu():
    print_header("Matching Group Scheduler")

    print("Choose the following options: ")
    print("1. Add a new person's unavailabile schedule")
    print("2. View all person's schedules")
    print("3. Find matching availability for a group meeting")
    print("4. Exit the scheduler")

    opt = input("Enter options 1 - 4: ").strip()

    return opt


def main():
    while True:
        opt = menu()
        if opt == "1":
            add_schedule()
        elif opt == "2":
            view_all_schedules()
        elif opt == "3":
            find_availabilities()
        elif opt == "4":
            print("\nGoodbye.")
            break
        else:
            print("\nPlease enter a valid option.")


if __name__ == "__main__":
    main()