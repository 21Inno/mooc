# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, an integer in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row 
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxes", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7 
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
# 
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

# check_sudoku should return None
from itertools import chain

ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,0,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0], 
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]


def check_sudoku(grid):
    ###Your code here.
    """ This function ckeck the validity of a sudoku
    parameter:
    ---------
    grid : it's the sudoku (list of list)
    return:
    ---------
    TRUE, FALSE or NONE
"""
    if type(grid) != list: #check if the sudoku is a grid
        return None 
    num=0
    nb_row=0
    nb_col=0
    for i in grid:
        nb_row+=1
        nb_col = 0
        for j in i:
            num +=1
            nb_col+=1
        if nb_col !=9: #check if the number of column is 9

            return None
    if nb_row != 9:#check if the number of row is 9

        return None

    if (num!=81): #check if there are 81 cases in the sudoku

        return None
    
    #check row
    for i in grid:
        for j in i:
            if (i.count(j)>1 and (j!=0)):

                return False
    
    
    #check column
    transpo = list(zip(*grid))
    for i in transpo:
        for j in i:
            if (i.count(j)>1 and (j!=0)):

                return False


    # create the sub-grids 1 to 9
    l1 = list(chain.from_iterable([x[:3] for x in grid[:3]])) 
    
    l2 = list(chain.from_iterable([x[3:6] for x in grid[:3]]))
    
    l3 = list(chain.from_iterable([x[6:9] for x in grid[:3]]))
    
    l4 = list(chain.from_iterable([x[:3] for x in grid[3:6]]))
    
    l5 = list(chain.from_iterable([x[3:6] for x in grid[3:6]]))
    
    l6 = list(chain.from_iterable([x[6:9] for x in grid[3:6]]))
    
    l7 = list(chain.from_iterable([x[:3] for x in grid[6:9]]))
    
    l8 = list(chain.from_iterable([x[3:6] for x in grid[6:9]]))
    
    l9 = list(chain.from_iterable([x[6:9] for x in grid[6:9]]))

    # check the sub-grids
    for l in [l1,l2,l3,l4,l5,l6,l7,l8,l9]:
        for i in l:
            if (l.count(i)>1 and (i!=0)):

                return False

    return True
#check_sudoku(ill_formed) # --> None
#print(check_sudoku(valid))      # --> True
#check_sudoku(invalid)    # --> False
#check_sudoku(easy)       # --> True
#check_sudoku(hard)       # --> True
     
