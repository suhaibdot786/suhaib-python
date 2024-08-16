y =  'hello world '
result = "" 

for i in range(len(y)):
    if i % 2 == 0:
        result  +=    y[i].upper()  # Uppercase characters at even indices
    else:
        result  +=   y[i].lower()  # Lowercase characters at odd indices

print(result)
 
