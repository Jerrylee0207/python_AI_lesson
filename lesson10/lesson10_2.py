import csv

with open("student_score.csv", "r", newline="", encoding="utf-8") as new_csv:
    reader = csv.DictReader(new_csv);
    student_data = [row for row in reader];

'''print(student_data);'''


fail_any = [student for student in student_data if int(student["CN"])<60 or int(student["EN"])<60 or int(student["math"])<60];


for row in fail_any:
    print(row);

'''
for i, student in enumerate(fail_any):
    print(f"{i+1:2d}, {student["name"]}, {int(student["CN"]):3d}, {int(student["EN"]):3d}, {int(student["math"]):3d}");
'''