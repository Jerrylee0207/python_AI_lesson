#import edu
from edu.tools import check_stat as func_a;

def main():
    try: 
        height = eval(input("請輸入身高(公分):"))/100;
        weight = eval(input("請輸入體重(公斤):"));

        if(height<1.2 or height>2.2):
            raise Exception("height error");
        elif(weight<30 or weight>200):
            raise Exception("weight error");

        bmi = weight/height**2;
        func_a(height, weight,bmi);
    
    except ValueError:
        print("value error");
    
    except Exception as errtxt:
        print(errtxt);

if(__name__=="__main__"):
    main();