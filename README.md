# Dutch National Flag Problem

## Problem Description

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

## Solution

I initialized three pointers. Two that maintain the index of the location where 0 and 2 are supposed to be stored and one pointer that moves across the array and helps in the sorting and swapping process.

Time Complexity: Since the time taken is dependent on the size of array (as we have to traverse the whole array), time complexity is O(n) where n is the input size.

Space Complexity: Other than some variables to store indices we are not using any additional space. Therefore, space complexity is O(1)