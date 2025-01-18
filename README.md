# Sudoku Solver

This program implements a Sudoku solver capable of handling and solving 9x9 Sudoku puzzles. It uses advanced heuristics and backtracking to efficiently solve puzzles, even those with higher difficulty levels. If the Sudoku puzzle is unsolvable, the program will return a grid filled with `-1`s to indicate the unsolvable state.

## Features

1. **Input Validation**: Ensures the given Sudoku puzzle is valid before attempting to solve it.
2. **Heuristics**:
   - **Minimum Remaining Values (MRV)**: Prioritizes cells with the fewest valid options.
   - **Degree Heuristic**: Breaks ties by selecting the cell that constrains the most other cells.
3. **Sudoku Techniques**:
   - **Naked Singles**: Automatically fills cells with only one possible value.
   - **Hidden Singles**: Identifies cells that can only take one value within a row, column, or block.
4. **Backtracking**: Handles the brute-force solving logic for remaining cells after applying heuristics.
5. **Performance Metrics**: Displays the execution time to solve the puzzle.
6. **Unsolvable Puzzle Handling**: Returns a grid filled with `-1`s if the puzzle cannot be solved.

## How It Works

1. The program validates the input Sudoku puzzle to ensure there are no duplicate numbers in any row, column, or block. Invalid puzzles will not proceed to solving.
2. The `nakedSingles` and `hiddenSingles` functions are applied iteratively to simplify the puzzle and reduce the search space.
3. The `findEmpty` function uses MRV and degree heuristics to select the next cell to solve.
4. The `backtrack` function attempts to solve the puzzle recursively by filling in valid numbers and backtracking when necessary.
5. If the puzzle is solvable, the solved Sudoku grid is printed, along with the execution time. If it is unsolvable, a grid of `-1`s is returned.

## How to Use

1. Replace the `sudoku` array in the program with your 9x9 Sudoku puzzle.
   - Use `0` to represent empty cells.
   - Example:
     ```python
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
     ```
2. Run the program.
3. The solved Sudoku grid will be printed in two formats:
   - As a numpy array.
   - As a formatted grid with `-1`s for unsolvable puzzles.
4. The execution time will also be displayed.

## Example Output

### Input Sudoku:

```
[[8 0 0 0 0 0 0 0 0]
 [0 0 3 6 0 0 0 0 0]
 [0 7 0 0 9 0 2 0 0]
 [0 5 0 0 0 7 0 0 0]
 [0 0 0 0 4 5 7 0 0]
 [0 0 0 1 0 0 0 3 0]
 [0 0 1 0 0 0 0 6 8]
 [0 0 8 5 0 0 0 1 0]
 [0 9 0 0 0 0 4 0 0]]
```

### Solved Sudoku:

```
Final Sudoku Grid:
8 1 2 7 5 3 6 4 9
9 4 3 6 8 2 1 7 5
6 7 5 4 9 1 2 8 3
1 5 4 2 3 7 8 9 6
3 6 9 8 4 5 7 2 1
2 8 7 1 6 9 5 3 4
5 2 1 9 7 4 3 6 8
4 3 8 5 2 6 9 1 7
7 9 6 3 1 8 4 5 2
```

Execution Time: 0.0023 seconds

### Unsolvable Sudoku:

```
Final Sudoku Grid:
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1
```

Execution Time: 0.0018 seconds

## Dependencies

- Python 3.x
- NumPy

Install dependencies with:

```bash
pip install numpy
```

## Limitations
- Performance may degrade for extremely complex puzzles.

## Future Improvements

- Implement a more advanced version of Algorithm X with Dancing Links to optimize constraint satisfaction.
- Add support for non-standard Sudoku sizes (e.g., 4x4 or 16x16).
- Enhance pre-solving techniques with advanced constraint satisfaction algorithms.

