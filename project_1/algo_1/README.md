# Algorithm 1: The Alternating Disk Problem
## The Problem
_The problem below is adapted from Levitin’s textbook:_

You have a row of __𝟐𝒏__ disks of two colors, __𝒏__ light and __𝒏__ dark. They alternate: light, dark, light,
dark, and so on. You want to get all the dark disks to the left hand side and all the light disks
to the right hand end. The only moves you are allowed to make are those that interchange the
positions of two neighboring disks. Design an algorithm for solving this puzzle and determine
the number of moves it takes.

> __Input__: a positive integer __𝑛__ and a list of __2𝑛__ disks of alternating colors light-dark, starting with
> light  
> __Output__: a list of __2𝑛__ disks, the first __𝑛__ disks are dark, the next __𝑛__ disks are light, and an integer
> __𝑚__ representing the number of swaps to move the light ones after the dark ones  

<img width="659" height="62" alt="algo1_proj1" src="https://github.com/user-attachments/assets/b32462e8-bca7-46b3-aa27-be2df00b2190" />

### Pseudocode
__std::vector<int> generate_disk_list(int n)__  
Purpose: creates the alternating disks list given an input __n__  
Input: positive integer __n__  
Output: vector (__2n__) of type int, where  
>__0__ is light-colored disks  
>__1__ is dark-colored disks  
Return: a vector of alternating disks, __list__  
```
Let __list__ = a vector of ints
For each element in __list__:
    push_back light-colored disk = 0
    push_back dark-colored disk = 1
Return __list__
```  

__void print_disk_list(const std::vector<int>& list)__  
Input: constant reference to the alternating disks list, __list__  
Output: prints disk list in 0's and 1's
Return: nothing

```
For every __disk__ in __list__:
    print the current element __disk__

```  

__int sort_disk_list(std::vector<int>& list)__  
Purpose: modifies disk list to be sorted from dark to light  
Input: reference to the alternating disks list, __list__  
Output: sorted disk list (__2n__)  
> first __n__ is dark-colored (1)  
> remaining __n__ is light-colored (0)  
```
Let __m__ = number of swaps
Let __swap__ = true

While swap holds true:
    __swap__ is false, no elements left to swap
    For each element in __list__:
        If (current_element = 0) and (next_element = 1):
            Swap the two elements (0,1) -> (1, 0)
        __m__++
        __swap__ is true (0,1) -> (1,0)
    Return __m__

```  


### Mathematical Analysis
```
std::vector<int> generate_disk_list(int n) {
    std::vector<int> list;              // +1

    for (int i = 0; i < n; i++) {       // n
        list.push_back(0);              // +2 atomics
        list.push_back(1);
    }                                   

    return list;
}                                       // Overall: 2n+1
```

```
void print_disk_list(const std::vector<int>& list) {
    for (int disk : list) {
        std::cout << disk << " ";         // Overall: n
    }

    std::cout << std::endl;
}
```

```
int sort_disk_list(std::vector<int>& list) {
    int m = 0;      // +1
    bool swap;      // +1

    do {        // n
        swap = false;       // +1
        for (size_t i = 0; i < list.size()-1; i++) {        // n
            if ((list[i] == 0) && (list[i+1] == 1)) {       // +5
                int temp = list[i];     // +2
                list[i] = list[i+1];    // +3
                list[i+1] = temp;       // +2

                m++;        // +1
                swap = true;        // +1
            }
        }
    } while (swap);     // Overall: 14n^2

    return m;
}
```

This gives a total complexity of:  
T(n) = 2n + 1 + n + 14n^2  
T(n) = 14n^2 + 3n + 1  

O(n^2)

## Program Information
__Programming Languages:__ C++  
__Date:__ September 27, 2025  
__Files:__ main.cc, disk.c, disk.h, main.sh  

### To run this program:
```
chmod +x main.sh    # only need to run this once
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
