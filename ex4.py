def parse_line(line):
    ranges = [0]*4 
    buf = ""
    index = 0 
    for i, l in enumerate(line):
        if l == ",":
            ranges[index] = int(buf)
            buf = "" 
            index += 1 
            continue
        if l == "-":
            ranges[index] = int(buf)
            buf = "" 
            index += 1
            continue
        buf += l 
    ranges[index] = int(buf)
    return ranges

def range_to_set(r1, r2):
    return set([x for x in range(r1,r2+1)])

# checks if arg is a proper subset of src
def is_proper_subset(src, arg):
    return ((src & arg) == arg) 

def is_weak_subset(src, arg):
    return len(list((src & arg))) > 0 

assert parse_line("2-4,6-8") == [2,4,6,8]
assert parse_line("22-44,66-88") == [22,44,66,88]

assert range_to_set(2,4) == set([2,3,4])
assert range_to_set(10,15) == set([10,11,12,13,14,15])

assert is_proper_subset(set([1,2,3]), set([2])) == True 
assert is_proper_subset(range_to_set(2,8), range_to_set(3,7)) == True            
assert is_proper_subset(range_to_set(2,8), range_to_set(7,10)) == False        


assert is_weak_subset(range_to_set(2,8), range_to_set(10,11)) == False
assert is_weak_subset(range_to_set(2,8), range_to_set(8,10)) == True
assert is_weak_subset(range_to_set(2,4), range_to_set(2,4)) == True

def pipeline(line):
    ranges = parse_line(line)
    bag1, bag2 = range_to_set(ranges[0], ranges[1]), range_to_set(ranges[2], ranges[3])

    if is_proper_subset(bag1, bag2) or is_proper_subset(bag2, bag1):
        return 1
    return 0

def pipeline2(line):
    ranges = parse_line(line)
    bag1, bag2 = range_to_set(ranges[0], ranges[1]), range_to_set(ranges[2], ranges[3])

    if is_weak_subset(bag1, bag2) or is_weak_subset(bag2,bag1):
        return 1
    return 0 
    

def process_file(fname, pipeline_func=pipeline):
    total = 0 
    with open(fname, "r") as inputfile:
        for line in inputfile:
            line = line[:-1]
            total += pipeline_func(line)
    return total

print("answer: ", process_file("day4.txt"))
print("answer2 ", process_file("day4.txt", pipeline2))
