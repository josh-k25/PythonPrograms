sentence = "  Hello Josh Welcome To Python  "

# 1) Remove leading/trailing spaces
sentence = sentence.strip()

# 2) Convert to all lowercase
sentence = sentence.lower()

# 3) Split into a list of words
words = sentence.split()

# 4) Print the list
print(words)