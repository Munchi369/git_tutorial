#!/usr/bin/env python3
"""Simple command-line calculator."""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("a", type=float, help="First operand")
    parser.add_argument("operator", choices=['+','-','*','/'], help="Operator")
    parser.add_argument("b", type=float, help="Second operand")
    args = parser.parse_args()

    op = args.operator
    if op == '+':
        result = args.a + args.b
    elif op == '-':
        result = args.a - args.b
    elif op == '*':
        result = args.a * args.b
    elif op == '/':
        if args.b == 0:
            raise ZeroDivisionError("division by zero")
        result = args.a / args.b
    print(result)


if __name__ == "__main__":
    main()
