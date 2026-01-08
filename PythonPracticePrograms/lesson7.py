grades = {
    "math": 85,
    "physics": 90,
    "chemistry": 78
}

# 1) Add "english": 88
grades["english"] = 88
# 2) Increase "math" by 5
grades["math"] += 5
# 3) Loop and print: subject -> grade
for key in grades:
    print(key, "->", grades[key])
