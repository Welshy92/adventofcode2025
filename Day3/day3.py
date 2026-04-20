# NOTES TO TRY. Read line by line in the data.
# Split all numbers into seperate array entries
# Can either try finiding the max() number if that's possbile. Do that twice.

# Or can just do an iterative comparison to see which 1 if bigger.
# Keep the index of the larger number noted down then do it again but either starting from the index of the larger
# number or remove all the numbers that don't need to be checked for the 2nd time.

# Once the 2 numbers are found, join them together to make 1 number and then add it to the overall total.
from operator import index


total_sum = 0


with open("input.txt", 'r') as f:
    banks = f.read().splitlines()

for battery in banks:
    cell_list = [int(cell) for cell in str(battery)]
    first_max = int(max(cell_list[:-1]))
    sliced_list = cell_list[cell_list.index(first_max) + 1:len(cell_list)]
    second_max = int(max(sliced_list))
    total_sum += int(str(first_max) + str(second_max))

    print(total_sum)

print(total_sum) # 17193 was the correct number for my input.