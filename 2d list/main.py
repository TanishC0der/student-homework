matrix=[
    [1,2,3],
    [4,5,6,],
    [7,8,9,]
]
element=matrix[1][1]
print(element)
for element in matrix:
    print(element)
#input for rows and columns
rows=int(input("Enter the number of rows"))
columns=int(input("Enter the number of columns"))

matrix=[]

for i in range(rows):
    row_list=[]
    for j in range(columns):
        value=int(input(f"Enter the value for the row{i+1},collumn{j+1}"))
        row_list.append(value)
    matrix.append(row_list)
for element in matrix:
    print(element)        



