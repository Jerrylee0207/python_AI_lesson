def menu(apptizer:str, main_course:str, dessert:str):
    print(f"apptizer:{apptizer}");
    print(f"main course:{main_course}");
    print(f"dessert:{dessert}");

def print_tuple(*args):
    print(args);

def print_keyval(**kwargs):
    print(kwargs);

def print_mix(*args, **kwargs):
    print(args);
    print(kwargs);


def main():

    arr:args = (1,2,3,4,5,6,7,8,9,10);
    print(1,2,3,4,5,6,7,8,9,10, sep='*', end='tail\n');



main();

    