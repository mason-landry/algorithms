
class Grid:
    def __init__(self, puzzle:list, size=9):
        # Define size of sudoku grid (default is 9x9)
        self.size = size
        self.grid = puzzle

    ## method to update grid value
    def update(self, val, i, j):
        self.grid[i][j] = val

    ## method to print grid at end
    def show(self):
        for i in self.grid:
            print(*i)

    ## method to find next empty space in grid
    def find_next_empty(self):
        '''Finds next empty space in puzzle grid, reading left to right and top to bottom.

        Params: None
        Output: 
        r - row index
        c - column index
        '''
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0:
                    return r,c

    ## method to check whether the current number being tesed is a possible move
    def validate(self, val, r, c):
        '''Validates whether the value 'val' works in the space r,c
        Params:

        val - Number between 1 and 9 to test
        r - row index
        c - column index
        '''
        ## Check row
        for i in range(self.size):
            if self.grid[r][i] == val and c != i:
                return False

        ## Check column
        for i in range(self.size):
            if self.grid[i][c] == val and r != i:
                return False

        ## Check box
        box_x = c // 3
        box_y = r // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.grid[i][j] == val and (i,j) != (r,c):
                    return False

        return True
    
    def solve(self):
        '''
        Recursive solving algorithm. Updates matrix with valid solutions and resets if it hits a problem
        '''
        # Get r,c indices if empty space
        idx = self.find_next_empty()
        if idx:
            r,c = idx

            # Loop to try numbers 1 through 10 in each empty space
            for i in range(1, self.size + 1):
                if self.validate(i, r, c):
                    self.update(i,r,c)
                
                    # Check if the remaining spaces can be solved with this solution:
                    if self.solve(): # Recursion!
                        return True


                    self.update(0,r,c)
        else:
            # no more empty spaces, puzzle must be solved!
            return True
        
        return False

if __name__ == '__main__':
    sudoku = [
        [0, 0, 9, 4, 0, 0, 0, 8, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 3, 0, 2, 7, 0],
        [0, 3, 0, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 5, 0, 3, 0, 0, 4],
        [9, 0, 0, 0, 0, 1, 0, 3, 0],
        [0, 6, 2, 0, 4, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 9, 0, 0, 0, 8, 5, 0, 0]]
    grid = Grid(sudoku)
    grid.show()
    grid.solve()
    print("- - - - - - - - - ")
    grid.show()

    