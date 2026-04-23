# NOTES TO TRY. Read line by line in the data.
# Split all numbers into seperate array entries
# Can either try finiding the max() number if that's possbile. Do that twice.

# Or can just do an iterative comparison to see which 1 if bigger.
# Keep the index of the larger number noted down then do it again but either starting from the index of the larger
# number or remove all the numbers that don't need to be checked for the 2nd time.

# Once the 2 numbers are found, join them together to make 1 number and then add it to the overall total.
from operator import index

joltage_list = []
large_joltage = []
large_joltage_sum = 0
total_sum = 0


with open("input.txt", 'r') as f:
    banks = f.read().splitlines()

for battery in banks:
    cell_list = [int(cell) for cell in str(battery)]
    first_max = int(max(cell_list[:-1]))
    sliced_list = cell_list[cell_list.index(first_max) + 1:len(cell_list)]
    second_max = int(max(sliced_list))
    total_sum += int(str(first_max) + str(second_max))

print(f"{total_sum} is Part 1 total") # 17193 was the correct number for my input. PART 1 ANSWER

# PART 2 would require the same sort of iteration but finding the largest 12 numbers and then joining them together to
# make a 12 digit number. Then add all those 12 digit numbers together to get the final answer.

total_sum_p2 = 0


for batteries in banks:
    cell_list = [int(cell) for cell in str(batteries)]
    current_digits = []
    remaining_list = cell_list
    
    # We need to find 12 numbers iteratively
    for i in range(12):

        # Break if we run out of numbers to check.
        if not remaining_list:
            break
            
        # To ensure we have room for the following numbers we search in the list excluding the last few elements .
        # This is similar to how part 1 worked except it is now build for scale and not just 2 hard coded numbers.
        # We let the last check be the full remaining_list just as a minor optimisation.
        if i < 11:
            search_area = remaining_list[:-(11 - i)] if len(remaining_list) > (11 - i) else remaining_list
        else:
            search_area = remaining_list
            
        if not search_area: 
            break
            
        # Find the max in the current search area
        current_max = max(search_area)
        current_digits.append(str(current_max))
        
        # Find the index of this max and slice the list for the next iteration
        max_idx = remaining_list.index(current_max)
        remaining_list = remaining_list[max_idx + 1:]

    # Join the 12 digits together to make one large number
    if len(current_digits) == 12:
        twelve_digit_num = int("".join(current_digits))
        total_sum_p2 += twelve_digit_num

print(f"Part 2 Total Sum: {total_sum_p2}")