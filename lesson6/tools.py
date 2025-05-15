def check_stat(height:float,weight:float,bmi:float):
    if(bmi>=35):
        print("您的體質為重度肥胖");
    elif(bmi>=30):
        print("您的體質為中度肥胖");
    elif(bmi>=27):
        print("您的體質為輕度肥胖");
    elif(bmi>=24):
        print("您的體重過重");
    elif(bmi>=18.5):
        print("您的體質正常");
    else:
        print("您的體重過輕");
    
    print(f"身高(公尺):{height:.2f}");
    print(f"體重(公斤):{weight:.2f}");
    print(f"BMI:{bmi:.2f}");