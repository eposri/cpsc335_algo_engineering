#/bin/bash

# Algorithm 1: "The Alternating Disk Problem"
# Kayla Ngo
# kngo29@csu.fullerton.edu
# CWID# 886374479
# CPSC 335-13
# This file is the script file for the algorithm.

echo "Compile the source file disk.cc"
g++ -c -m64 -Wall -o disk.o disk.cc -fno-pie -no-pie -std=c++17

echo "Compile the source file main.cc"
g++ -c -m64 -Wall -o main.o main.cc -fno-pie -no-pie -std=c++17

echo "Link the object modules to create an executable file"
g++ -m64 -o main.out main.o disk.o -lm -fno-pie -no-pie -std=c++17 -z noexecstack

echo "Execute the program"
chmod +x main.out
./main.out

#Delete some unnecessary files
rm *.o
rm *.out