from dataclasses import dataclass

'''
fruit = ["apple", "orange", "banana"];
fruit.append("tomato");
fruit.pop(2);
print(fruit);
'''
@dataclass
class fruit:
    name:str;
    color:str;
    sweetness:int;

basket:list[fruit] = [fruit(name="apple",color="red",sweetness=7),
                      fruit(name="banana",color="yellow",sweetness=3),
                      fruit(name="blueberry",color="blue",sweetness=7),
                      fruit(name="orange",color="orange",sweetness=8),
                      fruit(name="grava",color="green",sweetness=4)];

for fruit in basket:
    print(fruit.name, fruit.color, fruit.sweetness);

