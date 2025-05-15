from large_pow import large_pow

def main():
    value = int(input("please enter val:"));
    power = int(input("please enter pow:"));
    modulo = int(input("please enter mod:"));
    print(f"{value}^{power} mod {modulo} = {large_pow(value, power, modulo)}");

main();