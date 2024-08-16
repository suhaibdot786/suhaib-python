x="hello world"

result = []

# Uppercase characters at even indices
for i in range(0, len(x), 2):
    result.append(x[i].upper())

# Lowercase characters at odd indices
for i in range(1, len(x), 2):
    result.append(x[i].lower())

# Join the list into a single string
final_result = ''.join(result)
print(final_result)
