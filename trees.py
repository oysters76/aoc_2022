import math

def load_as_list(fname):
    grid = [] 
    with open(fname, "r") as input_file:
        for line in input_file:
            line = line.replace("\n", "")
            grid.append(list(line))
    return grid

def is_edge(row, col, grid):
    if row == 0 or row == len(grid)-1:
        return True
    if col == 0 or col == len(grid[0])-1:
        return True
    return False

def get_row(row, col, grid):
    return grid[row]

def get_col(row, col, grid):
    d = []
    for i, r in enumerate(grid):
        d.append(grid[i][col])
    return d


def is_big(target, index, arr):
    left =  arr[0:index]
    right = arr[index+1:]
    
    is_big = True
    for l in left:
        if int(l) >= int(target):
            is_big = False
            break

    if is_big:
        return True

    for r in right:
        if int(r) >= int(target):
            return False

    return True

def score(target, arr):
    score = 0
    for a in arr:
        if int(a) < int(target):
            score += 1
        else:
            score += 1
            break
    return score 

def get_score(target, index, arr):
    left = arr[0:index]
    right = arr[index+1:]
    left.reverse()
    return score(target, left) * score(target, right)

def get_scenic_score(row, col, grid):
    row_d = get_row(row, col, grid)
    col_d = get_col(row, col, grid)
    target = grid[row][col]
    return get_score(target, col, row_d) * get_score(target, row, col_d)

def is_visible(row, col, grid):
    if is_edge(row, col, grid):
        return True

    row_d = get_row(row, col, grid)
    col_d = get_col(row, col, grid)

    target = grid[row][col]
    result = is_big(target, col, row_d) or is_big(target, row, col_d)
    
    return is_big(target, col, row_d) or is_big(target, row, col_d)

def find_all_visible(grid):
    count = 0 
    for row, d in enumerate(grid):
        for col, _ in enumerate(d):
            if is_visible(row, col, grid):
                count += 1
    return count

def find_max(grid):
    max = -1
    for row, d in enumerate(grid):
        for col, _ in enumerate(d):
            score = get_scenic_score(row, col, grid)
            if score > max:
                max = score
    return max

SAMPLE = "day8_sample.txt"
ACT = "day8.txt"

def test_all(fname):
    grid = load_as_list(SAMPLE)
    assert is_edge(0,0,grid) == True, "is_edge error"
    assert is_edge(3,3,grid) == False, "is_edge error"
    assert is_edge(4,0,grid) == True, "is_edge error"

    print(get_row(3,3,grid))
    print(get_col(3,3,grid))

test_all(SAMPLE)
#print("answer: ", find_all_visible(load_as_list(ACT)))
print("answer2: ", find_max(load_as_list(ACT)))            
