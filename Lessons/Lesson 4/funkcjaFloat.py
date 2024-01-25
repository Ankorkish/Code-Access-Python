f=float('5.5')
print(f) #output: 5.5

f=float('5')
print(f) #output: 5.0

f=float('     -5')
print(f) #output: -5.0

f=float('1e3')
print(f) #output: 1000.0

f=float('-Infinity')
print(f) #output: -inf

f=float('inf')
print(f)  #output: inf
print(type(f)) #output:<class 'float'>