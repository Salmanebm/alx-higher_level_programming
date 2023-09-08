#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    count = len(sys.argv) - 1
    res = 0
    if count < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] == "+":
        res = add(int(sys.argv[1]), int(sys.argv[3]))
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], res))
    elif sys.argv[2] == "-":
        res = sub(int(sys.argv[1]), int(sys.argv[3]))
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], res))
    elif sys.argv[2] == '*':
        res = mul(int(sys.argv[1]), int(sys.argv[3]))
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], res))
    elif sys.argv[2] == "/":
        res = div(int(sys.argv[1]), int(sys.argv[3]))
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
