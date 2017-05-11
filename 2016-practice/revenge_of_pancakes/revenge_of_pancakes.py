def flip_stack(pos, stack):
    stack_list = []
    for i in range(0,pos):
        stack_list.append(stack[pos - (i+1)])
        # print stack_list,
    stack_list.append(stack[len(stack)-1])
    # print "".join(stack_list)

def check_cakes(stack):
    new_stack = stack
    prog_stack = stack
    count = 1
    if len(stack) > 1:
        if "-" in prog_stack:
            for i in range(0,len(prog_stack)):
                if stack[abs(i-len(prog_stack))-1] == "-":
                    # print abs(i-len(prog_stack))-1
                    new_stack = flip_stack(abs(i-len(prog_stack))-1, prog_stack)
                    count = count + 1
        else:
            return "0," + stack
    elif "-" in stack:
        return "0,+"
    else:
        return "0,+"
    if new_stack == stack:
        return str(count) + "," + new_stack

def init(file_name):
    case_num = 0
    w = open("output.txt", "w")
    with open(file_name, "r") as f:
        for line in f:
            if case_num != 0:
                print check_cakes(line)
            case_num = case_num + 1

init(raw_input(">> "))
