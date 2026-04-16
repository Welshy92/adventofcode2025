with open("input.txt", 'r') as f:
	# dial = f.readlines()
	dial = list(map(int, f.read().replace('R', '').replace('L', '-').split()))

### PART 1 ###
zero_count = 0
x = 50
for turn in dial:
	x += turn
	if x % 100 == 0:
		zero_count += 1
print(f'part 1:\t{zero_count}') #This reads 1036 which is correct.

### PART 2 ###
zero_count = 0
x = 50
for turn in dial:
	zero_count += abs(turn) // 100
	a = 1 if turn > 0  else -1
	rem = a * abs(turn % 100)
	x += rem
	if x >= 100 or (x <= 0 and x != rem):
		zero_count += 1
	x %= 100
print(f'part 2:\t{zero_count}') # This reads 6193 which is incorrect. It is too low.