def to_list(s):
    lines = s.split("\n") 
    grid = [] 
    for line in lines:
        grid.append(list(line)); 
    return grid 
    
def pad(grid, val=-1):
    row_len = len(grid[0]) 
    new_size = row_len + 2 
    
    new_grid = [] 
    new_grid.append([val]*new_size); 
    
    for row in grid:
        row = [val] + row + [val] 
        new_grid.append(row) 
    
    new_grid.append([val]*new_size) 
    
    return new_grid

def print_grid(grid):
    for line in grid:
        for l in line:
            print(l,end="\t")
        print()

dirs_8 = [[-1,-1],
        [0,-1],
        [1,-1],
        [1,0],
        [1,1],
        [0,1],
        [-1,1],
        [-1,0]]

dirs_4 = [
        [-1,0],
        [0,-1],
        [1,0],
        [1,0]
    ]

def get_val(grid, i, j, dir):
    dx, dy = dir 
    return grid[i+dx][j+dy]

def condition_1(grid, i, j, dir_vals):
    target = grid[i][j]
    for d in dir_vals:
        if int(d) < int(target):
            return True 
    return False 

def conv(grid, dirs,condition, pad=-1):
    count = 0 
    for i, line in enumerate(grid):
        for j, l in enumerate(line):
            if l == pad:
                continue 
            dir_vals = [get_val(grid, i, j, dir) for dir in dirs]
            if (condition(grid, i, j, dir_vals)):
                count += 1
    return count 

