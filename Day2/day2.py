with open("input.txt", 'r') as f:
    IDs = f.read().split(',')

# Example 1: n = 123123
# Example 2: n = 123456
def is_invalid(n):
    stringy = str(n)
    length = len(stringy) # 6 for both examples
    
    if length % 2 != 0: # determine if the length of the number is odd or even. If it's odd, it can't be made up of two identical halves, so it can't be invalid.
        return False
    
    half = length // 2
    left = stringy[:half]
    right = stringy[half:]

    return left == right # Retuns true if both halves are the same, meaning the ID is invalid. Otherwise it returns false.

total = 0

for id_range in IDs:
    # I split the 2 numbers to define the range then loop through each number in the range to check if it is valid.
    numbers = id_range.split('-')
    start = int(numbers[0])
    end = int(numbers[1])
    for x in range(start, end + 1):
        if is_invalid(x):
            total += x

print("Sum of all invalid IDs:", total) # This reads 123456789 for my input which is correct.