numbers=[
    [1,2,3],
    [4,5,6],
    [8,7,9]
]

del_elements=[]

for i in range(len(numbers)):
    del_elements.append(numbers[i][i])
print(del_elements)