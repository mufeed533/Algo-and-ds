"Find the number of unique paths in a matrix, where a path contains only zeros"

def matrix_dfs(arr, r, c, visit):
    ROWS, COLS = len(arr), len(arr[0])
    if (min(r,c) < 0) or (r == ROWS or c == COLS) or ((r,c) in visit) or arr[r][c] == 1:
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1
    
    visit.add((r,c))
    
    count = 0
    count += matrix_dfs(arr, r+1, c, visit)
    count += matrix_dfs(arr, r-1, c, visit)
    count += matrix_dfs(arr, r, c+1, visit)
    count += matrix_dfs(arr, r, c-1, visit)
    
    visit.remove((r,c))
    return count

arr = [[0,0,0,0], [1,1,0,0], [0,0,0,0], [0,1,0,0]]
print(matrix_dfs(arr, 0, 0, set()))
