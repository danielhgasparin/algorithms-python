"""Spiral matrix module.

Spiral matrices are like, for size 4x4: 
[[ 1,  2,  3,  4],
 [12, 13, 14,  5],
 [11, 16, 15,  6],
 [10,  9,  8,  7]]
"""

def spiral_matrix(n):
    """Return a spiral matrix of size "n"x"n"."""
    matrix = [[None for _ in range(n)] for _ in range(n)]
    val = 1
    start_col = 0
    start_row = 0
    end_col = n - 1
    end_row = n - 1

    while start_col <= end_col and start_row <= end_row:
        for i in range(start_col, end_col + 1):
            matrix[start_row][i] = val
            val += 1
        start_row += 1
    
        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = val
            val += 1
        end_col -= 1
    
        for i in range(end_col, start_col - 1, -1):
            matrix[end_row][i] = val
            val += 1
        end_row -= 1
    
        for i in range(end_row, start_row - 1, -1):
            matrix[i][start_col] = val
            val += 1
        start_col += 1
    return matrix