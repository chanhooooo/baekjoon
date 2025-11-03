#25206 너의 평점은
grade_to_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
total_credit = 0
total_score_times_credit = 0
subjects = []
splits = []
for _ in range(20):
    c = input()
    subjects.append(c.split(" "))

for subject_info in subjects:
    credit_str = subject_info[1]
    grade = subject_info[2]
    if(grade == "P"):
        continue
    else:
        credit = float(credit_str)
        score = grade_to_score[grade]
        total_credit +=credit
        total_score_times_credit += (credit * score)
        
final_gpa = total_score_times_credit / total_credit
print(final_gpa)