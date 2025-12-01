zero_counter = 0
new_num = 0


def grabEntry():
    lines_list = []

    with open("input.txt", "r") as file:
        lines_with_newlines = file.readlines()

    for line in lines_with_newlines:
        lines_list.append(line.strip())
    
    return lines_list


def makeSum(startnum, direction, endnum):
    global zero_counter
    global new_num

    if direction == "L":
        new_num = startnum - endnum
    else:
        new_num = startnum + endnum
    
    if new_num >= 100:
        new_num = new_num - 100
        zero_counter = zero_counter + 1
    elif new_num <= 0:
        new_num = new_num + 100
        zero_counter = zero_counter + 1


def main():

    data_list = grabEntry()

    makeSum(50, "R", 55)
    print("Current Number = " + str(new_num))
    print("zero_counter = " + str(zero_counter))

    makeSum(new_num, "L", 25)
    print("Current Number = " + str(new_num))
    print("zero_counter = " + str(zero_counter))

    print(data_list)


main()