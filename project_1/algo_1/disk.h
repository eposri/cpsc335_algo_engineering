/*
Algorithm 1: "The Alternating Disk Problem"

Author Information
    Name: Kayla Ngo
    Email: kngo29@csu.fullerton.edu
    CWID: 885083436
    Course: CPSC 335-13

File Information:
    Name: disk.h
    Programming Language: C++
    Purpose: 
        Header file for alternating disk algorithm that contains the function
        declarations
*/

#ifndef DISK_H
#define DISK_H

#include <vector>

std::vector<int> generate_disk_list(int n);
void print_disk_list(const std::vector<int>& list);
int sort_disk_list(std::vector<int>& list);

#endif