import sys, argparse
from typing import List

def arg_parser():
    parser = argparse.ArgumentParser(description="input file.")
    parser.add_argument('input_file', help = 'please provide input file name.', type = str)
    return parser

def gift_list(line: str) -> str:
    line = line[1:-1]
    hex_digit1 = None
    hex_digit = False
    esc_digit = False
    unwrapped = ""
    for c in line:
        if hex_digit:
            if hex_digit1 == None:
                hex_digit1 = c
            else:
                unwrapped += chr(int(hex_digit1 + c, base = 16))
                hex_digit1 = None
                hex_digit = False
                esc_digit = False
        elif esc_digit:
            if c == "\\":
                unwrapped += c
                esc_digit = False
            elif c == '"':
                unwrapped += c
                esc_digit = False
            elif c == "x":
                hex_digit = True
            else:
                unwrapped += c
                esc_digit = False
        else:
            if c == "\\":
                esc_digit = True
            else:
                unwrapped += c
    return unwrapped

def extra_wrapping(line: str) -> str:
    wrapping = ""

    for i,c in enumerate(line):
        if c == '"':
            if i == 0:
                wrapping += '"\\"'
            elif i == len(line)-1:
                wrapping += '\\""'
            else:
                wrapping += '\\"'
        elif c ==  '\\':
           wrapping += '\\\\'
        else:
           wrapping += c
    return wrapping

def main(argv: List[str]) -> int:
    arg = arg_parser().parse_args(argv[1:])
    total = 0
    more_wrapping = 0
    with open(arg.input_file, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            #print(line.rstrip('\n'))
            #print(gift_list(line))
            #print(extra_wrapping(line))
            total += len(line) - len(gift_list(line))
            more_wrapping += len(extra_wrapping(line)) - len(line)
    print(f'part1: {total}\npart2: {more_wrapping}')
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))