
import random
file = open("names.txt", encoding="utf-8");
file_text = file.readlines();

name_arr = [name.strip() for name in file_text];

pick = int(input("請輸入所需要的姓名數量:"));

for i in range(0, pick):
    index = random.randint(0, len(name_arr));
    print(f"{i+1:3d}.{name_arr[index]}");

file.close();