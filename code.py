
# Create a Class 
class Growing_Cultures:

    def __init__(self):
        self.previous_grid = []
        self.iteration = 0
        self.stable = False
    
    # A Method that allows us to read in the grid from a text file
    def read_in_File(self, file):
        self.grid = [] 
        with open(file) as f:
            for line in f:
                line = line.strip("\n")
                self.grid.append([c for c in line])

        # Store the information about the initial state of the grid
        self.previous_grid = self.grid 

    # A Method that allows us to initialy populate livable cells within the grid
    def populate_Grid(self):
        updated_grid = []
        for row in self.grid:
            current_row = []
            for i in row:
                if i == ".":
                    current_row.append(".")
                elif i == "L":
                    current_row.append("#")
            updated_grid.append(current_row)

        # Store the information about the state of the grid after it has been populated
        self.grid = updated_grid

    # A Method that allows us to count number of unlivable, livable, and populated cells within the grid
    def count_Cells(self):
        unlivable_cells = 0
        populated_cells = 0
        livable_cells = 0
        for row in self.grid:
            for cell in row:
                if cell == '.':
                    unlivable_cells +=1
                if cell == "#":
                    populated_cells += 1
                if cell == "L":
                    livable_cells += 1
        return populated_cells, livable_cells, unlivable_cells

    # A Method that allows us to update the grid after each iteration
    def iterations(self):

        # An Inner function that returns a count of populated neighbour cells
        def get_Neighbours(index_row, index_cell):
            
            if 0 < index_row < len(self.grid) - 1:
                x_loc = (0, -1, 1)
            elif x > 0:
                x_loc = (0, -1)
            else:
                x_loc = (0, 1)

            if 0 < index_cell < len(self.grid[0]) - 1:
                y_loc = (0, -1, 1)
            elif y > 0:
                y_loc = (0, -1)
            else:
                y_loc = (0, 1)
                
            # Iterate for each of the cell's neigbours and count how many of them are populated
            populated = 0
            for x in x_loc:
                for y in y_loc:
                    if x == y == 0: 
                        continue
                    elif self.grid[index_row + x][index_cell + y] == "#":
                        populated += 1

            return populated

        # Get the location of each of the cells in the grid and
        # Change the staus of the cells depending on their neighrours
        updated_grid = []
        for index_row, row in enumerate(self.grid):
            current_row = []
            for index_cell, cell in enumerate(row):
                if cell == "L" and get_Neighbours(index_row, index_cell) == 0:
                    current_row.append("#")
                elif cell == "#" and get_Neighbours(index_row, index_cell) >= 4:
                    current_row.append("L")
                else:
                    current_row.append(cell)
            updated_grid.append(current_row)

        # Store the information about the state of the grid after every iteration
        self.grid = updated_grid

    # A Method to start the iterations and get the final stats 
    def get_Result(self, file):
        self.read_in_File(file)
        self.populate_Grid()
        while not self.stable:
            self.iteration += 1
            self.previous_grid = [[cell for cell in row] for row in self.grid]
            self.iterations()
            if self.grid == self.previous_grid:
                self.stable = True
                unlivable_cells, populated_cells, livable_cells = self.count_Cells()
                print(f"""
Number of hours (iterations) it takes to stabilize the cultures: {self.iteration}

Number of unlivable cell locations in the grid: {unlivable_cells}

Number of cell locations thatare occupied with cultures on the final day (when it stabilizes): {populated_cells}

The ratio of spaces upon which the culture has taken hold to total Livable spaces on the final day as a percentage: {round((populated_cells/livable_cells)*100, 2)}%
""")
          

if __name__ == "__main__":
    grid = Growing_Cultures()
    grid.get_Result("data/cell-cultures.txt")
