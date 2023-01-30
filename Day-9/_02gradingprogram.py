student_scores={
    "Harry":81,
    "Ron":78,
    "Herminone":99,
    "Draco":74,
    "Neville":62,
}
grade={ }

for key in student_scores:
    print(key)
    print(student_scores[key])
    if(student_scores[key]>90 and   student_scores[key]<=100):
        grade[key]="outstanding"
    elif(student_scores[key]>80 and   student_scores[key]<=90):
        grade[key]="Exceeds Expectation"
    elif(student_scores[key]>70 and   student_scores[key]<=80):
        grade[key]="Acceptable"
    else:
        grade[key]="fail"
        
print(grade)