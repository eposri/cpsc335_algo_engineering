/*
Algorithm 1: "The Alternating Disk Problem"

Author Information
    Name: Kayla Ngo
    Email: kngo29@csu.fullerton.edu
    CWID: 885083436
    Course: CPSC 335-13

File Information:
    Name: main.cc
    Programming Language: C++
    Compile: 
        g++ -c -m64 -Wall -o main.o main.cc -fno-pie -no-pie -std=c++17
    Purpose: 
        Main() function entry point for the algorithm program from disk.cpp
*/

#include <iostream>
#include <vector>

#include "disk.h"

int main() {
    std::cout << "Welcome to Algorithm 1: The Alternating Disk Problem"
              << std::endl;

    int x;

    while (true) {
        std::cout << "Please enter a positive integer: ";
        std::cin >> x;

        if (x <= 0) {
            std::cout << "Input is negative, please try again: " << std::endl;
            continue;
        }

        break;
    }

    std::vector<int> li = generate_disk_list(x);
    std::cout << "Printing out the alternating disks list: " << std::endl;
    print_disk_list(li);

    std::cout << "Sorting the alternating disks list: " << std::endl;
    int swap_count = sort_disk_list(li);
    print_disk_list(li);
    std::cout << "Number of swaps: " << swap_count << std::endl;

    return 0;
}