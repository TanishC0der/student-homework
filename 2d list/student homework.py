
scores=[9,12,13,14,20,28,29,30,31,35,48,36,49,51,62,68,70,84,90,92,70,84,90,92]


# putting scores into 3 lists
below_31=[]
between_31_and_69=[]
above_69=[]
for i in scores:
    if i<31:
        below_31.append(i)
    elif i >30 and i< 70:
        between_31_and_69.append(i)
    else:
        above_69.append(i)

#printing the scores 
print("The scores below 31 are :")
print(below_31)
print("\n")
print("The Scores between 31 and 69 are:")
print(between_31_and_69)
print("\n")
print("the scores above 69 are :")
print(above_69)
 
