numbers=list(range(51))
even_numbers=[]
odd_numbers=[]

for i in numbers:
    square=i**2
    #print(square)
    if i%2==0:
        even_numbers.append(square)
        
    else:
        odd_numbers.append(square)
print("squares for odd numbers:")
print(odd_numbers)
print("\n")
print("square for even numbers")
print(even_numbers)

