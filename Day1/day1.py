with open("input.txt", 'r') as f:
	# dial = f.readlines()
	safe_lock = list(map(int, f.read().replace('R', '').replace('L', '-').split()))

### PART 1 ###

zero_count = 0
x = 50 # Starting position of the safe lock according to my instructions.
for turn in safe_lock:
	x += turn
	if x % 100 == 0:
		zero_count += 1
print(f'part 1:\t{zero_count}') #This reads 1036 for my input which is correct.

### PART 2 ###
# Examples where 'x' is the current position of the safe lock and 'turn' is the number we turn right (positive) or left (negative).
# Example 1: x = 50, turn = 100
# Example 2: x = 25, turn = -100
# Example 3: x = 0, turn = -350
# Example 4: x = 75, turn = -50
def zero_crossings(x, turn):
    if turn > 0:
        return (x + turn) // 100 # Example 1 leads here and returns 1
    else:
        y = abs(turn) # Absolute value turns negative turns into positive for easier calculations.
        if x == 0:
            return y // 100 # Example 3 leads here and returns 3
        elif x <= y:
            return (y - x) // 100 + 1 # Example 2 leads here and returns 1
        else:
            return 0 # Example 4 leads here and returns 0


zero_count = 0
x = 50 # Starting position of the safe lock according to my instructions.
for turn in safe_lock:
    zero_count += zero_crossings(x, turn) # This function will count the number of times we cross 0 on each turn and add it to the total count.
    x = (x + turn) % 100

print(f'part 2:\t{zero_count}') #This reads 6228 for my input which is correct.