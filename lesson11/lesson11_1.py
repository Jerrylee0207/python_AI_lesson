import requests
import io
from io import StringIO
import csv


from requests import Response

url:str = "https://raw.githubusercontent.com/Jerrylee0207/python_AI_lesson/refs/heads/main/lesson10/student_score.csv";

response:Response = requests.get(url);

if response.status_code==200:
    print("success");
    content:str = response.text;

file:StringIO = io.StringIO(content);
reader = csv.DictReader(file);
students = [row for row in reader];
file.close();

for student_data in students:
    print(student_data);