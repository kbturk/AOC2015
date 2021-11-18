import sys, argparse
import hashlib
from typing import List, Dict, Tuple, Any

def arg_parser():
    parser = argparse.ArgumentParser(description="input file.")
    parser.add_argument('input_file', help = 'please provide input file name.', type = str)
    return parser

#Part 1:
def nice_check(check:str) -> bool:
    prev_s:str = ""
    vowel_check:int = 0
    double_letter:bool = False

    for s in check:
        if s in 'aeiou':
            vowel_check += 1
        if s == prev_s:
            double_letter = True
        if prev_s + s in ['ab','cd','pq','xy']:
            return False
        prev_s = s

    if vowel_check >= 3 and double_letter:
        return True
    return False

#Part 2:
def nice_2_check(check:str) -> bool:
    prev_s:str = " "
    prev_prev_s:str = " "
    double_pair:bool = False
    repeats = False

    for i,s in enumerate(check, start=1):
        if prev_s+s in check[i:]:
           double_pair = True
        if prev_prev_s == s:
           repeats = True
        prev_prev_s = prev_s
        prev_s = s
    if double_pair and repeats:
        return True

    return False

#Santa needs a parser to determine nice strings for nice girls and boys.
def main(argv: List[str]) -> int:
    arg = arg_parser().parse_args(argv[1:])
    tot_nice_1 = 0
    tot_nice_2 = 0
    with open(arg.input_file, 'r') as f:
        for line in f:
            naughty_or_nice = line.strip('\n')
            if nice_check(naughty_or_nice):
                tot_nice_1 += 1
            if nice_2_check(naughty_or_nice):
                tot_nice_2 += 1
    print(tot_nice_1, tot_nice_2)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))