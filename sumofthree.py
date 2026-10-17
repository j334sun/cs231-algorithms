##
## ======================================================= 
##   Jialu Sun
##   CS 231 Spring 2024
##   Assignment 1, P1
## =======================================================
##

import check

def sum_of_three(num):
    """
    sum_of_three(num) adds the two numbers found to num and produces the sum.
    Effects: Adds the sum of the two numbers to num.
    sum_of_three: (Int) -> Int
    Requries: num to be an integer
    Examples:
        if num = 3, sum_of_three(num) = 72.
    """
    TEAMS_NUM = 27
    FAQ_NUM = 42

    sum = TEAMS_NUM + FAQ_NUM + num

    return sum

            
# Test 1: Add the two constants to the input (27 + 42 + 3 = 72).
check.expect("Q1T1", sum_of_three(3), 72)
