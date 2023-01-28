students_score=input("Enter the students score\n").split()

for n in range(0,len(students_score)):
    students_score[n]=int(students_score[n])
    

highest_score=0
for x in students_score:
    if(x>highest_score):
        highest_score=x
    else:
        highest_score=highest_score

print(f"The highest Score is {highest_score}")