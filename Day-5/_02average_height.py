
# to find the average height
students_height=input("Enter the students height\n").split()

for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])
print(students_height)

sum=0

for x in students_height:
    sum=sum+x

average=sum/len(students_height)
print(round(average))