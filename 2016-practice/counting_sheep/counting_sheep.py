def cycle(n):
    x = 1
    repeat = 1
    numbers_seen = []
    while len(numbers_seen) != 10:
        z = x * n
        print z,n,x,x * n
        z_string = str(z)
        x = x + 1
        if z == n:
            repeat = repeat + 1
        if repeat > 2:
            break
        for y in range(0,len(z_string)):
            if z_string[y] not in numbers_seen:
                numbers_seen.append(z_string[y])
    if repeat > 2:
        return "INSOMNIA"
    else:
        print numbers_seen
        return z
def init(file_name):
    case_num = 0
    w = open("output.txt", "w")
    with open(file_name, "r") as f:
        for line in f:
            if case_num != 0:
                w.write("Case #" + str(case_num) + ": " + str(cycle(int(line))) + "\n")
            if case_num == 100:
                break
            case_num = case_num + 1


init(raw_input("Enter Filename: "))
