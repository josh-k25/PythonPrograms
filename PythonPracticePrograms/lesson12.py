nums = [3, 6, 9, 12, 15]

# Use filter + lambda to create a list of numbers divisible by 3
# Use map + lambda to create a list of those numbers multiplied by 10
# Print the final list

threes = list(filter(lambda x: x % 3 == 0, nums))
tenTimesThrees = list(map(lambda x: x * 10, threes))

print(tenTimesThrees)