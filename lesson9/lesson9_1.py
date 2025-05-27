from dataclasses import dataclass

@dataclass
class Student:
    name:str;
    chinese:int;
    english:int;
    math:int;

    @property
    def total(self)->int:
        return self.chinese+self.english+self.math;

    def average(self)->float:
        return self.total/3.0;

    def __repr__(self)->str:
        return f"{self.name}'s info";

stu01 = Student(0,0,0,0);
stu01.name = "Jerry";
stu01.chinese = 78;
stu01.english = 90;
stu01.math = 90;

'''
num_list = [15,8,9,7,4,1,2,8];
print(num_list);
num_list.append(5);
num_list.extend([10,20]);
num_list.remove(9);
print(num_list);
'''

dict1 = {'alice':5, 'bella':8, 'cathy':6};

for key in dict1:
    print(key, dict1[key]);

print(dict1['diana']);


