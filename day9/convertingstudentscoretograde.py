stuednt_score = {
    "mohan": 79,
    "Latha": 89,
    "kushal": 65,
    "Ajay": 95,
}
student_grade = {}
# score 91-100 =Outstanding score 81-90 Exceeds expectation score 71-80 Acceptable score <=70 fail
for student in stuednt_score:
    if stuednt_score[student] >= 91:
        student_grade[student] = "Outstanding"
    elif stuednt_score[student] >= 81:
        student_grade[student] = "Exceeds expectation"
    elif stuednt_score[student] >= 71:
        student_grade[student] = "Acceptable"
    elif stuednt_score[student] <= 70:
        student_grade[student] = "fail"
print(student_grade)
