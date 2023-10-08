stack = '''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3
'''

#for l in stack[1:]:
 #   print(l, l == " ", l == "\n")

def fmt_line(line, n):
    formatted_line = ""
    counter = 0
    for i,l in enumerate(line, n):
        if (counter == n):
            counter = 0
            continue
        formatted_line += l 
        counter += 1
    return formatted_line 
 
def parse_line(line, n):
    line = fmt_line(line, n)
    start = 0
    end = n
    limit = len(line)
    line_data = ['#'] * n  
    index = 0
    
    while end <= limit:
        sub = line[start:end];
        for c in sub:
            if c != '[' and c != ']' and c != '' and c != ' ':
                line_data[index] = c 
        index += 1 
        start = end
        end += n

    return line_data
        
 
def parse_stack(stack_str, n):
    stack_str = stack_str.replace("\n", " ") 
    ch_per_line = (n * 3) + (n-1) + 1 
    lines_read = (len(stack_str)/ch_per_line) 

    start = 1
    end = ch_per_line 
    index = 1

    stack_data = [] 
    while (index <= lines_read):
        stack_data.append(parse_line(stack_str[start:end], n)) 
        #print(parse_line(stack_str[start:end], n)) 
        #print("line: ", index, stack_str[start:end], len(stack_str), start, end)
        start = end
        end += ch_per_line
        index += 1

    return stack_data 
  
stack_2 = '''
                        [R] [J] [W]
            [R] [N]     [T] [T] [C]
[R]         [P] [G]     [J] [P] [T]
[Q]     [C] [M] [V]     [F] [F] [H]
[G] [P] [M] [S] [Z]     [Z] [C] [Q]
[P] [C] [P] [Q] [J] [J] [P] [H] [Z]
[C] [T] [H] [T] [H] [P] [G] [L] [V]
[F] [W] [B] [L] [P] [D] [L] [N] [G]
 1   2   3   4   5   6   7   8   9 
'''
print(parse_stack(stack_2, 9))
    
