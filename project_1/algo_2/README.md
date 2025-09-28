# Algorithm 2: Matching Group Schedules
## The Problem
The group schedule matching problem takes two or more arrays as input. The arrays represent
availabilities and daily working periods of group members. The output is an array containing
intervals of time when all members are available for a meeting. The group schedule problem can
be defined as shown below:  

> __Input__:  arrays __𝑚__ of related elements, comprising the time intervals, and a HashMap, __𝑑__,
> representing a daily active periods of all members. __U__ is a global set of all arrays. The
> problem can be represented as:  
<div align="center">
  <img width="87" height="60" alt="algo2_proj1" src="https://github.com/user-attachments/assets/78b14087-ff1f-4767-8ddd-d1a06908bac9" />
</div>

> __Output__: a set of HashMap, __𝑟__, such that __r__ ⊆ __U__

Assume there are at least two persons in your class project group. You want to schedule a meeting
with another group member. You are provided with (a) a schedule of members’ daily activities,
containing times of planned engagements. They are not available to have a meeting you during
these periods; (b) the earliest and latest times at which they are available for meetings daily. Your
schedule and availabilities are provided too.  

Write an algorithm that takes in your schedule, your daily availability (earliest time, latest time)
and that of your group member (or members), and the duration of the meeting you want to
schedule. Time is given and should be returned in 24hr military format (HH:MM), for example:
9:30, 22:21. The given times (output) should be sorted in ascending order.  

An algorithm for solving this problem may involve combing the two sub-arrays into an array
containing a set of unavailabilities, with consideration of the daily active periods.

> __Sample Input:__  
> person1_Schedule =[[ ‘7:00’, ’8:30’], [’12:00’, ’13:00’], [’16:00’, ’18:00’]]  
> person1_DailyAct = [‘9:00’, ’19:00’]  

> person2_Schedule = [[ ‘9:00’, ’10:30’], [’12:20’, ’14:00’], [’14:30’, ’15:00’], [’16:00’, ’17:00’ ]]  
> person2_DailyAct = [‘9:00’, ’18: 30’]  
> duration_of_meeting =30  

> __Sample Output:__  
> [[’10:30’, ’12:00’], [’15:00’, ’16:00’], [’18:00’, ’18:30’]]  

### Pseudocode

### Mathematical Analysis

## Program Information
__Programming Languages:__ C++  
__Date:__ September 27, 2025  
__Files:__ main.cpp, schedule.cpp, schedule.h, main.sh

### To run this program:
```
./main.sh
```

### Development Information
__OS:__ Ubuntu 22.04.04 LTS  
__Text Editor:__ Visual Studio Code  
__Tools:__ G++ compiler  

### Author Information
__Name:__ Kayla Ngo  
__Email:__ kngo29@csu.fullerton.edu  
__CWID:__ 885083436  
__Course:__ CPSC 335-13  

__Submission for Project 1__
