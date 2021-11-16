import sys, argparse
from typing import List

def arg_parser():
    parser = argparse.ArgumentParser(description="Process input file.")
    parser.add_argument('input file', help = 'please provide an AOC file.', type = str)
    return parser

def main(argv: List[str]) -> int:
    arg = arg_parser().parse_args(argv[1:])
    s:str = ""
    with open( argv[1],'r') as f:
        for line in f:
            s += line.strip('\n')
    #part one/two:
    tot:int = 0
    spot = 0
    for letter in s:
        if letter == '(':
            tot += 1
        elif letter == ')':
            tot -= 1
        spot += 1
        if tot == -1:
           print(f'Santa enters the basement at: {spot}')
           return 0
    print(tot)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))