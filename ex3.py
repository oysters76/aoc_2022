LETTERS = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
SCORES = {val:index+1 for index,val in enumerate(LETTERS)}

def split_value(s):
    size = len(s)
    half = int(size/2) 
    return s[0:half], s[half:size]

def to_set(s1, s2):
    return set(s1), set(s2) 

def intersect(s1,s2):
    return (s1 & s2).pop() 

def get_score(scores_map, s):
    return scores_map[s] 
    
def pipeline(s,scores_map):
    s1, s2 = split_value(s) 
    s1, s2 = to_set(s1, s2) 
    inter = intersect(s1, s2) 
    return get_score(scores_map,inter) 


assert split_value("vJrwpWtwJgWrhcsFMMfFFhFp") == ("vJrwpWtwJgWr", "hcsFMMfFFhFp"), "split value function failed" 
assert to_set("vJrwpWtwJgWr","hcsFMMfFFhFp") == (set("vJrwpWtwJgWr"),set("hcsFMMfFFhFp")), "to set function failed" 
assert intersect(set("vJrwpWtwJgWr"),set("hcsFMMfFFhFp")) == "p", "intersect function failed" 
assert get_score(SCORES,"p") == 16, "get score function failed"


def test_pipeline(s, expected):
    assert pipeline(s,SCORES) == expected, "test for: " + s + " failed"

test_pipeline("vJrwpWtwJgWrhcsFMMfFFhFp", 16); 
test_pipeline("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", 38) 
test_pipeline("PmmdzqPrVvPwwTWBwg", 42) 
test_pipeline("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 22) 
test_pipeline("ttgJtRGJQctTZtZT", 20) 
test_pipeline("CrZsJsPPZsGzwwsLwLmpwMDw",19)

def process_group(group_arr, scores_map):
    bag1, bag2, bag3 = group_arr 
    bag1, bag2, bag3 = set(bag1), set(bag2), set(bag3) 
    badge = (bag1 & bag2 & bag3).pop() 
    return scores_map[badge]

assert process_group(["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"],SCORES) == 18
assert process_group(["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"], SCORES) == 52

def process_group_file(fname):
    total_score = 0 
    with open(fname, "r") as inputfile:
        group_buffer = [] 
        counter = 0
        line_count = 0
        groups = [] 
        for line in inputfile:
            if (counter == 3):
                print(group_buffer)
                groups.append(group_buffer) 
                total_score += process_group(group_buffer, SCORES) 
                group_buffer = []
                counter = 0
            group_buffer.append(line[:-1]) 
            counter += 1 
            line_count += 1
    total_score += process_group(group_buffer, SCORES)
    print("total lines: ", line_count, " groups: ", len(groups), " mod: ", line_count%len(groups))
    return total_score 

def read_and_eval(fname):
    score = 0 
    with open(fname, "r") as inputfile:
        for line in inputfile:
            score += pipeline(line,SCORES)
    return score


print(read_and_eval("day3.txt"))
print(process_group_file("day3.txt"))


