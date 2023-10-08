import sys

stack = [['', 'N','Z'], ['D','C','M'], ['','','P']]
stack2 = [['Z','N'], ['M', 'C', 'D'], ['P']]

def parse_instruction(inst):
    do_copy = False
    buf = ""
    vals = [] 
    for l in inst:
        if l in '1234567890':
            do_copy = True
        else:
            if (buf != ""):
                vals.append(int(buf))
                buf = "" 
            do_copy = False
        if do_copy:
            buf += l
    return vals


assert parse_instruction("move 1 from 2 to 1\n") == [1,2,1] 
assert parse_instruction("move 22 from 221 to 21\n") == [22,221,21]

def move(inst, stack):
    how_many, src, dest = inst

    src -= 1
    dest -= 1

    times = 0
    while times < how_many:
        elem = stack[src].pop()
        stack[dest].append(elem)
        times += 1 

    return stack

def move2(inst, stack):
    how_many, src, dest = inst
    src -= 1
    dest -= 1
    times = 0

    crates = []
    while times < how_many:
        crates.append(stack[src].pop())  
        times += 1
    crates.reverse()

    stack[dest] = stack[dest] + crates 
    return stack


def apply_moves(fname, stack, move_func=move):
    with open(fname, "r") as inputfile:
        for line in inputfile:
            stack = move_func(parse_instruction(line), stack)
    return stack 

def add_row(stack, row):
    stack.append(row)
    return stack 

def get_top(stack):
    top = "" 
    for i in range(len(stack)):
        l = len(stack[i])
        r = '' 
        if (l != 0):
            r = stack[i][l-1] 
        top += r 

    return top 

stack3 = []
stack3 = add_row(stack3, ['F', 'C', 'P', 'G', 'Q', 'R'])
stack3 = add_row(stack3, ['W', 'T', 'C', 'P'])
stack3 = add_row(stack3, ['B', 'H', 'P', 'M', 'C'])
stack3 = add_row(stack3, ['L', 'T', 'Q', 'S', 'M', 'P', 'R'])
stack3 = add_row(stack3, ['P', 'H', 'J', 'Z', 'V', 'G', 'N'])
stack3 = add_row(stack3, ['D', 'P', 'J'])
stack3 = add_row(stack3, list("LGPZFJTR"))
stack3 = add_row(stack3, list("NLHCFPTJ"))
stack3 = add_row(stack3, list("GVZQHTCW"))

stack3 = apply_moves("inst2.txt", stack3, move2)
print(stack3)
print("answer: ", get_top(stack3))







