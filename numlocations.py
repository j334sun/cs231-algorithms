##
## =======================================================
## Jialu Sun
## CS 231 Spring 2025
## Assignment 1, P1
## =======================================================
##

from grids import *
import check

def num_locations(grid, item):
    """
    num_locations(grid, item) produces the number of entries in grid that contain item.
    
    num_locations: Grid Str -> Int
    
    Examples:
    sample grid 1 from the module
    
    num_locations(grid_one, "red") => 3
    num_locations(grid_one, "mauve") => 0
    """
    count = 0
    rows = grid.row_num()
    cols = grid.col_num()
    
    for i in range(rows):
        for j in range(cols):
            if grid.access(i, j) == item:
                count += 1
                
    return count

# Test 1: Grid with the item present multiple times
grid_one = Grid(3, 4)
grid_one.enter(0, 0, "red")
grid_one.enter(0, 1, "green")
grid_one.enter(0, 2, "blue")
grid_one.enter(0, 3, "yellow")
grid_one.enter(1, 0, "orange")
grid_one.enter(1, 1, "red")
grid_one.enter(1, 2, "brown")
grid_one.enter(1, 3, "blue")
grid_one.enter(2, 0, "green")
grid_one.enter(2, 1, "purple")
grid_one.enter(2, 2, "blue")
grid_one.enter(2, 3, "red")
check.expect("Q1T1", num_locations(grid_one, "red"), 3)

# Test 2: Grid with the item not present
check.expect("Q1T2", num_locations(grid_one, "mauve"), 0)

# Test 3: Grid with the item present once
grid_two = Grid(2, 2)
grid_two.enter(0, 0, "apple")
grid_two.enter(0, 1, "banana")
grid_two.enter(1, 0, "cherry")
grid_two.enter(1, 1, "date")
check.expect("Q1T3", num_locations(grid_two, "banana"), 1)

# Test 4: Empty grid
grid_three = Grid(0, 0)
check.expect("Q1T4", num_locations(grid_three, "anything"), 0)
