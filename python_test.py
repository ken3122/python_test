#!/usr/bin/env python

import sys
#import os
import re
import ast
import argparse
import getpass
import datetime


def print_welcome():
    date = datetime.datetime.now().strftime("%B %d %Y")
    user = getpass.getuser()
    print(f"Hello, {user}! Today is {date}. Beautiful day for miracles!")

def eval_string(in_string):
    try:
        elements = ast.literal_eval(in_string)
    except (ValueError, SyntaxError) as error:
        print(error, file=sys.stderr)
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        return elements

def open_file(name):
    try:
        file_object = open(name)
        line = file_object.readline()
    except IOError as error:
        print(error, file=sys.stderr)
        sys.exit(1)
    else:
        return line

def open_file_w(name):
    try:
        out = open(name, 'w')
    except IOError as error:
        print(error, file=sys.stderr)
        sys.exit(1)
    else:
        return out

def main():
    if args.file is not None:
        contents = open_file(args.file)
    else:
        contents = args.string
    
    elements = eval_string(contents)
    
    if args.out is not None:
        out = open_file_w(args.out)

    print_welcome()
    print("Input string:\n", contents)
    print("Output tuples:")
   
    tuples_union = []
    if isinstance(elements, tuple):
        for element in elements:
            if isinstance(element, tuple):
                for t in element:
                    tuples_union.append(t)
            elif isinstance(element, int) and element >= 0:
                if len(tuples_union) >= element:
                    print(tuple(tuples_union[:element]))
                    if args.out is not None:
                        print(tuple(tuples_union[:element]),file=out)
                    del tuples_union[:element]
                else:
                    sys.exit(0)
            else:
                print(f"Incorrect input: {element} is not narutal number or tuple.", file=sys.stderr)
                sys.exit(1)
    elif isinstance(elements, int):
        if elements == 0:
            print(tuple())
            sys.exit(0)
        elif elements > 0:
            sys.exit(0)
        else:
            print(f"Incorrect input: {elements} is not narutal number or tuple.", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"Incorrect input: {elements} is not narutal number or tuple.", file=sys.stderr)
        sys.exit(1)

    if args.out is not None:
        out.close() 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Magical pipeline.')
    parser.add_argument('-f', '--file', help='input file')
    parser.add_argument('-o', '--out', help='output file')
    parser.add_argument('-s', '--string', help='string to process')
    args = parser.parse_args()
    main()
