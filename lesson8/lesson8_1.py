week = ["Mon", "Tue", "Wen", "Thr", "Fri", "Sat", "Sun"];

'''
for i in range(0,7):
    print(week[i]);
'''

slice_1 = week[0:3];

'''
nation = {"TW":"Taiwan", "JP":"Japan", "HK":"Hong Kong"};
for key in nation:
    print(key, nation[key]);
'''
'''
nation_set = {"TW", "JP", "HK", "US", "UK", "TW", "JP", "HK", "US", "UK"};
    print(len(nation_set));
'''
'''
arr_01 = [i*(1+i)//2 for i in range(1, 21)];
print(arr_01);
'''

students_stat = [
                    {"name":"Alice", "age":14, "score":100},
                    {"name":"Bob", "age":16, "score":70},
                    {"name":"Cathy", "age":15, "score":50},
                    {"name":"Daniel", "age":17, "score":67},
                    {"name":"Evan", "age":18, "score":80},
                    {"name":"Finn", "age":20, "score":46},
                    {"name":"Gabriel", "age":16, "score":69},

                ];

students_stat60_1 = [student for student in students_stat if student["score"]>=60];


def is_over60(student):
    if student["score"]>=60:
        return True;
    else:
        return False;


students_stat60_2 = filter(is_over60, students_stat);


for student in students_stat60_1:
        print(f"01{student}");


for student in students_stat60_2:
        print(f"02{student}");

students_stat60_3 = list(filter(lambda student:student if student["score"]>=60 else None, students_stat));

for student in students_stat60_3:
        print(f"03{student}");


