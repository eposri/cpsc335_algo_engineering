/*
Algorithm 1: "The Alternating Disk Problem"

Author Information
    Name: Kayla Ngo
    Email: kngo29@csu.fullerton.edu
    CWID: 885083436
    Course: CPSC 335-13

File Information:
    Name: disk.cc
    Programming Language: C++
    Compile: 
        g++ -c -m64 -Wall -o disk.o disk.cc -fno-pie -no-pie -std=c++17
    Purpose: 
        The implementation file that contains the logic for the alternating
        disk algorithm
*/

#include <iostream>
#include <vector>

#include "disk.h"

// generate_disk_list(int n)
// creates the alternating colors of disks (2n row)
// input: positive integer n
// output: vector (2n) of type int, where
//         0 is light-colored disks
//         1 is dark-colored disks
// return: vector (alternating disks list)
std::vector<int> generate_disk_list(int n) {
    std::vector<int> list;

    for (int i = 0; i < n; i++) {
        list.push_back(0);  // n light
        list.push_back(1);  // n dark
    }

    return list;
}

// print_disk_list(const std::vector<int>& list)
// input: const reference to disk list
// output: prints disk list 
void print_disk_list(const std::vector<int>& list) {
    for (int disk : list) {
        std::cout << disk << " ";
    }

    std::cout << std::endl;
}

// sort_disk_list(std::vector<int>& list)
// modifies disk list to be sorted from dark to light
// input: reference to disk list
// output: disk list (2n)
//         first n is dark-colored (1)
//         remaining n is light-colored (0)
// return: m = number of swaps, integer
int sort_disk_list(std::vector<int>& list) {
    int m = 0;  // number of swaps
    bool swap;  // swap tracker

    // do-while swap is true,
    do {
        swap = false;
        // iterate through disk list and swap dark to light
        for (size_t i = 0; i < list.size()-1; i++) {
            if ((list[i] == 0) && (list[i+1] == 1)) {
                int temp = list[i];     // temp holder = current value
                list[i] = list[i+1];    // current position = next value
                list[i+1] = temp;       // next position = temp holder
    
                m++;
                swap = true;
            }
            // continues to iterate through list until swap is false
        }
    } while (swap);

    return m;
}