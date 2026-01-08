a = [2, 4, 6]
b = [10, 20, 30]

sums = []

# Create a list sums that contains a[i] + b[i] using zip
for a, b in zip(a, b):
    sums.append(a+b)

print(sums)
