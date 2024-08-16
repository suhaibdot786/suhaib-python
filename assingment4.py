x =  'hello world '
result = "" 

for i in range(len(x)):
    if i % 2 == 0:
        result  +=    x[i].upper()  # Uppercase characters at even indices
    else:
        result  +=   x[i].lower()  # Lowercase characters at odd indices

print(result)
 
