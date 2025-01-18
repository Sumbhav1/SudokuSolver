import numpy as np
import time

sudoku = np.array([
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
])

def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """
    #--- generating valid options for a given cell ---
    def getPossibleValues(row, col):
        if sudoku[row, col] != 0:
            return set()
        
        values = set(range(1,10))
        values -= set(sudoku[row, :])
        values -= set(sudoku[:, col])
        values -= set(sudoku[row // 3 *3 : row // 3 * 3 +3, col// 3 *3 : col// 3 * 3 +3].flatten())
        return values
        
    # ---- finding next best empty cell using minimum remaining value and degree heuristics to reduce search tree ----
    def findEmpty():
        min_values = 10
        cell = None
        max_effected_cells = -1
        for i in range(9):
            for j in range(9):
                if sudoku[i, j] == 0:
                    num_possible_values = len(getPossibleValues(i, j))
                    if num_possible_values < min_values:
                        min_values = num_possible_values
                        cell = (i, j)
                    elif num_possible_values == min_values:
                        effected_cells = countEffectedCells(i, j)
                        if effected_cells > max_effected_cells:
                            max_effected_cells = effected_cells
                            cell = (i, j)

        return cell
        
    #--- in the event of a tie, choose the cell which effects the most amount of empty cells --   
    def countEffectedCells(row, col):
        effected_cells = 0
        for x in range(9):
            if sudoku[row, x] == 0 and x != col:
                effected_cells += 1
            if sudoku[x, col] == 0 and x != row:
                effected_cells += 1

        block_r, block_c = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                r, c = block_r + i, block_c + j
                if sudoku[r, c] == 0 and (r, c) != (row, col):
                    effected_cells += 1
        return effected_cells
            
    # -----sudoku solving strategies ------
    def nakedSingles():
        again = False
        for i in range(9):
            for j in range(9):
                if sudoku[i, j] == 0:
                    possible_values = getPossibleValues(i, j)
                    if len(possible_values) == 1:
                        sudoku[i, j] = possible_values.pop()
                        changed = True
        return again

    def hiddenSingles():
        again = False
        for num in range(1, 10):
            for  i in range(9):
                hidden_single = [j for j in range(9) if num in getPossibleValues(i, j)]
                if len(hidden_single) == 1:
                    sudoku[i, hidden_single[0]] = num 
                    again = True
            
            for j in range(9):
                hidden_single = [i for i in range(9) if num in getPossibleValues(i, j)]
                if len(hidden_single) == 1:
                    sudoku[hidden_single[0], j] = num 
                    again = True

            for x in range(0, 9, 3):
                block_r = x // 3 * 3
                block_c = x // 3 * 3
                possible_cells = []
                for i in range(block_r, block_r + 3):
                    for j in range(block_c, block_c + 3):
                        if num in getPossibleValues(i, j):
                            possible_cells.append((i, j))
                if len(possible_cells) == 1:
                    row, col = possible_cells[0]
                    sudoku[row, col] = num
                    again = True
        return again
        
    #--- checking input sudokus for validity ---
    def isValidSudoku():
        def isValid(group):
            nums = [x for x in group if x != 0]
            freq = {}
            for num in nums:
                if num in freq:
                    return False
                freq[num] = 1
            return True

        for x in range(9):
            if not isValid(sudoku[x, :]) or not isValid(sudoku[:, x]):
                return False
            
        for block_r in range(0, 9, 3):
            for block_c in range(0, 9, 3):
                block = sudoku[block_r:block_r + 3, block_c:block_c + 3].flatten()
                if not isValid(block):
                    return False
        return True
        
    #---- handles brute force logic ---
    def backtrack():
        current_cell = findEmpty()
        if not current_cell:
            return True
        row, col = current_cell
        for num in sorted(getPossibleValues(row, col)):
            sudoku[row, col] = num
            if backtrack():
                return True
            sudoku[row, col] = 0
        return False
        
    if not isValidSudoku():
        return np.full((9, 9), -1)
        
    while nakedSingles():
        pass
        
    while hiddenSingles():
        pass
 
    if backtrack():
        solved_sudoku = sudoku
    else:
        return np.full((9, 9), -1)
    
    
    return solved_sudoku

start_time = time.time()  # Start the timer
result = sudoku_solver(sudoku)  # Run the solver
end_time = time.time()  # Stop the timer

print("Solved Sudoku:")
print(result)  # Print the solved Sudoku
print("\nFinal Sudoku Grid:")
for row in result:  # Print Sudoku row by row
    print(" ".join(str(cell) if cell != -1 else "." for cell in row))
print(f"Execution Time: {end_time - start_time:.6f} seconds")