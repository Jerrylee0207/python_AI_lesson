
import random
import csv

with open("names.txt", encoding="utf-8") as file:
    file_text = file.readlines();

name_arr = [name.strip() for name in file_text];

pick = int(input("請輸入所需要的姓名數量:"));

'''
for i, name in enumerate(random.sample(name_arr, pick)):
    print(f"{i+1:3d}.{name}")
'''
name_select = random.sample(name_arr, pick);

student_data:list[dict] = [
    {
        "name":name,
        "CN":random.randint(50,100),
        "EN":random.randint(50,100),
        "math":random.randint(50,100)
    }
    for name in name_select
]

key_list = student_data[0].keys();
with open("student_score.csv", "w", newline="", encoding="utf-8") as new_csv:
    writer = csv.DictWriter(new_csv,fieldnames=key_list);
    writer.writeheader();
    writer.writerows(student_data);
print("finish write");





