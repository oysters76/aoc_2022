import uuid 
import math

GLOBAL_SIZE = {}

def get_uuid():
    return str(uuid.uuid1())

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent
        self.uid = get_uuid()
        
    def add_child(self, child):
        self.children.append(child)

    def is_file(self):
        return len(self.children) == 0

    def find_size(self, mem={}):
        stack = [self]
        total_size = 0
        visited = [] 

        while len(stack) > 0:
            n = stack.pop()
            print(n)
            if n == None:
                continue
            if n.uid in visited:
                continue
            visited.append(n.uid)
            
            if isinstance(n, File):
                total_size += n.size
            elif n.uid in mem.keys():
                total_size += mem[n.uid]
            else:
                for i, child in enumerate(n.children):
                    stack.append(child)
                
        return total_size

    def is_dir(self):
        return len(self.children) > 0

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.uid = get_uuid()
        
def get_root():
    return Node("root", None)

def is_command(line):
    return line[0] == "$"

def is_cd(line):
    return line.split(" ")[1] == "cd"

def is_ls(line):
    return line.split(" ")[1] == "ls"

def get_cd_dir(line):
    return line.split(" ")[2]

def is_file(line):
    return line[0] in '0123456789'

def get_file(line):
    return File(get_file_name(line),
                get_file_size(line)) 

def get_file_name(line):
    return line.split(" ")[1] 

def get_file_size(line):
    return int(line.split(" ")[0])

def is_cd_prev(line):
    return get_cd_dir(line) == ".."


def test_all_util_funcs():
    assert is_command("$ cd /") == True, "is_command error"
    assert is_command("123 f.txt") == False, "is_command error"

    assert is_cd("$ cd ..") == True, "is_cd error"
    assert is_cd("dir folder") == False, "is_cd error"

    assert is_ls("$ ls") == True, "is_ls error"
    assert is_ls("dir folder") == False, "is_ls error"

    assert get_cd_dir("$ cd ..") == "..", "get_cd_dir error"

    assert is_file("1234 file") == True, "is_file error"

    assert get_file_size("1234 file") == 1234, "get_file_size error"

    assert is_cd_prev("$ cd ..") == True, "is_cd_prev error"

test_all_util_funcs()

def build_file_tree(lines):
    ft = get_root() 
    cnode = ft
    prev = None
    for line in lines.split("\n"):
        line = line.replace("\n", "")

        if line == "":
            continue
        
        if is_command(line):
            if is_cd(line):
                if is_cd_prev(line):
                    cnode = cnode.parent
                    prev = cnode.parent 
                else:
                    prev = cnode
                    cnode = Node(get_cd_dir(line), cnode)
                    prev.add_child(cnode) 
        else:
            if is_file(line):
                cnode.add_child(get_file(line))
                
    return ft 

def read_and_parse(fname):
    ft = None
    with open(fname, "r") as inputfile:
        ft = build_file_tree(inputfile.read())
    return ft

def get_all_dirs(ft):
    stack = [ft]
    dirs = []
    visited = [] 
    while len(stack) > 0:
        n = stack.pop()
        if n == None:
            continue
        if n.uid in visited:
            continue
        visited.append(n.uid)

        if not isinstance(n, Node):
            continue

        dirs.append(n)
        for i, child in enumerate(n.children):
            stack.append(child)
    return dirs

def find_dir_size(dirs):
    mem = {}
    uid_map = {}
    dirs.reverse()
    
    for i,d in enumerate(dirs):
        size = d.find_size(mem)
        mem[d.uid] = size 
        uid_map[d.uid] = d
        
    return mem,uid_map 

def filter(mem, threshold=100000):
    total = 0 
    for uid in mem.keys():
        if mem[uid] <= threshold:
            total += mem[uid]
    return total

'''Sample example
ft = read_and_parse("sample_day7.txt")
print("total size: ", ft.find_size())
dirs = get_all_dirs(ft)
mem, uid_map = find_dir_size(dirs)
print("answer: ", filter(mem))
'''

def pipeline(fname, threshold=100000):
    ft = read_and_parse(fname)
    dirs = get_all_dirs(ft)
    mem, _ = find_dir_size(dirs)
    print("answer: ", filter(mem))
    return ft,dirs,mem

TOTAL_SPACE = 70000000
SPACE_NEED = 30000000


def pipeline2(fname, n_space=SPACE_NEED):
    ft,dirs,mem = pipeline(fname)
    min_uid, min_val = find_best_dir(dirs, ft, mem, n_space)
    print("answer: ",min_val)

def find_remaining_space(ft, mem={},total_space=TOTAL_SPACE):
    used_space = 0 
    if ft.uid in mem:
        used_space = mem[ft.uid]
    else:
        used_space = ft.find_size(mem)
    return total_space - used_space

def find_best_dir(dirs, ft, mem, need=SPACE_NEED):
    rem_space = find_remaining_space(ft,mem)

    min_uid = -1
    min_val = math.inf

    for i, d in enumerate(dirs):
        size = mem[d.uid]
        space_after = rem_space + size
        is_valid = space_after >= need

        if not is_valid:
            continue

        space_after = rem_space+size

        if size < min_val:
            min_uid = d.uid
            min_val = size
    return min_uid, min_val


'''example 2
ft = read_and_parse("sample_day7.txt")
print("total size: ", ft.find_size())
dirs = get_all_dirs(ft)
mem, uid_map = find_dir_size(dirs)
print("answer: ", filter(mem))
best_uid, best_size = find_best_dir(dirs, ft, mem)
print("best size: ", best_size, " folder: ", uid_map[best_uid].name)
'''


pipeline2("day_7.txt")
