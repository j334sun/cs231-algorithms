## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##   
##   CS 231 code download
##   Version date: February 2022
##   File name: grids.py
##   
## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##
class Grid:
    """
    Fields: entries (listof (listof Any)), rows (Int), cols (Int)
    Requires: 0 < rows
              0 < cols

    """
    
    def __init__(self, r, c):
        """
        Grid(r, c) produces a Grid object with r rows and c columns.
        Effects: Creates a new Grid.
         __init__: Int Int -> Grid
        Requires: 0 < r
                  0 < c            
 
        """
        self.entries = []
        self.rows = r
        self.cols = c
        for row in range(r):
            newrow = [None]*c
            self.entries.append(newrow)

    def __repr__(self):
        """
        repr(self) produces a string with all entries.
        __repr__: Grid -> Str

        """
        output = ""
        for row in range(self.rows):
            output = output + repr(self.entries[row]) + "\n"
        return output


    def row_num(self):
        """
        self.row_num() returns the number of rows in self.
        row_num: Grid -> Int

        """
        return self.rows

    def col_num(self):
        """
        self.col_num() returns the number of columns in self.
        col_num: Grid -> Int

        """
        return self.cols
    
    def access(self, i, j):
        """
        self.access(i, j) returns the entry in row i and column j.
        access: Grid Int Int -> Any
        Requires: 0 <= i < self.rows
                  0 <= j < self.cols

        """
        return self.entries[i][j]

    def access_row(self, i):
        """
        self.access_row(i) produces a list of items in row i.
        access_row: Grid Int -> (listof Any)
        Requires: 0 <= i < self.rows

        """
        return self.entries[i]

    def access_col(self, j):
        """
        self.access_col(j) produces a list of items in column j.
        access_row: Grid Int -> (listof Any)
        Requires: 0 <= j < self.cols

        """
        rows = self.rows
        result = []
        for row in range(rows):
            result.append(self.entries[row][j])
        return result

    def enter(self, i, j, item):
        """
        self.enter(i, j, item) enters item in row i and column j.
        Effects: Mutates self.
        enter: Grid Int Int Any -> None
        Requires: 0 <= i < self.rows
                  0 <= j < self.cols

        """
        self.entries[i][j] = item

    def enter_row(self, i, row_list):
        """
        self.enter_row(i, row_list) enters row_list as row i.
        Effects: Mutates self.
        enter_row: Grid Int (listof Any) -> None
        Requires: 0 <= i < self.rows
                  row_list is a list of length self.cols

        """
        self.entries[i] = row_list

    def enter_col(self, j, col_list):
        """
        self.enter_col(j, col_list) enters col_list as column j.
        Effects: Mutates self.
        enter_col: Grid Int (listof Any) -> None
        Requires: 0 <= j < self.cols
                  col_list is a list of length self.rows

        """
        rows = self.rows
        for row in range(rows):
            self.entries[row][j] = col_list[row]

    def convert_grid_int(self):
        """
        self.convert_grid_int() changes all entries to integers.
        Effects: Mutates self.
        convert_grid_int: Grid -> None
        Requires: all entries are string versions of integers

        """
        rows = self.row_num()
        cols = self.col_num()
        for row in range(rows):
            for col in range(cols):
                old_value = self.access(row, col)
                new_value = int(old_value)
                self.enter(row, col, new_value)

    def create_image(self):
        """
        self.create_image() produces a compact string representing the grid.
        create_image: Grid -> Str
        Requires: all entries are strings

        """
        rows = self.rows
        cols = self.cols
        result = ""
        for row in range(rows):
            result = result + compact_list(self.access_row(row)) + "\n"
        return result

    def __eq__(self, other):
        """
        self == other produces True if self and other have the same entries.
        __eq__: Grid Grid -> Bool

        """
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for row in range(self.rows):
            if self.entries[row] != other.entries[row]:
                return False
        return True
            
def make_grid(fname):
    """
    make_grid(fname) opens the file fname, reads in the lines with the
        information given below, and produces a Grid:
        - number of rows
        - number of columns
        - string entries for each row (one line each)
    make_grid: Str -> Grid

    """
    data_file = open(fname,"r")
    data_list = data_file.readlines()
    data_file.close()

    rows = int(data_list[0].strip().split()[0])
    cols = int(data_list[1].strip().split()[0])

    new_grid = Grid(rows, cols)

    for row in range(rows):
        line = data_list[row+2]
        data = line.strip().split()
        for col in range(cols):
            new_grid.enter(row, col, data[col])

    return new_grid

def compact_list(string_list):
    """
    compact_list(string_list) produces a single string from items 
        in string_list.
    compact_list: (listof Str) -> Str

    """
    result = ""
    for item in string_list:
        result = result + str(item)
    return result


def make_grid_text_file(num_rows, num_cols, content, file_name):
    """
    make_grid_text_file(num_rows, num_cols, content, file_name) creates
        a new text file for a grid with the name formed by concatenating
        "testgraph" and file_name, for a grid with num_rows rows, num_cols
        columns, and the entries are individual characters concatenated
        as the string content.
    Effects: Creates a new text file.
    make_grid_text_file: Int Int Str Str -> None
    Requires: 0 < num_rows
              0 < num_cols
              len(content) is the product of num_rows and num_cols
    Code adapted from code generously provided by Adam Hunter
    (a student from Spring 2018)

    """ 
    # Creates a new text file.
    gridfile = open("testgrid{0}.txt".format(file_name), 'w')

    # Creates a line with the number of rows.
    gridfile.write(str(num_rows)+" \n")

    # Creates a line with the number of columns.
    gridfile.write(str(num_cols)+" \n")

    # Creates a line for each row.
    current = 0

    for row in range(num_rows):
        row_string = ""
        for col in range(num_cols):
            row_string = row_string + content[current] + " "
            current = current + 1
        row_string = row_string + "\n"
        gridfile.write(row_string)
        
    gridfile.close
            


