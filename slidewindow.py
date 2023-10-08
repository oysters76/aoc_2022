def slide(s, stride, operation):
    start = 0
    end = stride
    size = len(s)

    result = None 
    while (end <= size):
        window = s[start:end]
        do_stop, result = operation(start,end,window,s,stride)
        if (do_stop):
            return result 
        start += 1
        end += 1
    return result

def print_func(start,end,window,s,stride):
    print("start: ", start, "\tend: ", end, "\t:", window)
    return False, None 

def verify(start,end,window,s,stride):
    if (len(list(set(window))) == stride):
        return True, end   
    return False, -1

test_cases = [
    ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7],
    ["bvwbjplbgvbhsrlpgdmjqwftvncz", 5],
    ["nppdvjthqldpwncqszvftbrmjlhg", 6],
    ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10],
    ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11] 
]
test_cases_2 = [
    ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19],
    ["bvwbjplbgvbhsrlpgdmjqwftvncz", 23],
    ["nppdvjthqldpwncqszvftbrmjlhg", 23],
    ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29],
    ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26] 
]

def test_all(testcases,stride=4):
    for i,ts in enumerate(testcases):
        in_val, expected = ts
        assert slide(in_val, stride,verify) == expected, "Testcase " + str(i) + " failed!"

test_all(test_cases)
test_all(test_cases_2, 14)

def process_file(fname,stride=4):
    with open(fname, "r") as inputfile:
        data = inputfile.read()
        return slide(data, stride, verify) 
    return -1 

print("Answer 1: ", process_file("day6.txt"))
print("Answer 2: ", process_file("day6.txt",stride=14))

