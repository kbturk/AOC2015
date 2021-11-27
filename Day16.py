import sys, argparse
from typing import List, Dict, NamedTuple, Tuple, Iterable
from pprint import pprint

def review_Sue(input:argparse.FileType('r')) -> int:
    for line in input:
        _, num, a, x, b, y, c, z = line.strip('\n').split()
        d = {a.strip(':'): int(x.strip(',')), 
             b.strip(':'): int(y.strip(',')), 
             c.strip(':'): int(z.strip(','))}
        #print(d)
        my_sue_check = 0
        for item in d.keys():
            match item:
                case 'children':
                    if d[item] == 3:
                        my_sue_check += 1
                case 'cats':
                    if d[item] > 7:
                        my_sue_check += 1
                case 'samoyeds':
                    if d[item] == 2:
                        my_sue_check += 1
                case 'pomeranians':
                    if d[item] < 3:
                        my_sue_check += 1
                case 'akitas':
                    if d[item] == 0:
                        my_sue_check += 1
                case 'vizslas':
                    if d[item] == 0:
                        my_sue_check += 1
                case 'goldfish':
                    if d[item] < 5:
                        my_sue_check += 1
                case 'trees':
                    if d[item] > 3:
                        my_sue_check += 1
                case 'cars':
                    if d[item] == 2:
                        my_sue_check += 1
                case 'perfumes':
                    if d[item] == 1:
                        my_sue_check += 1
            if my_sue_check == 3:
                return int(num.strip(':'))
    return 0

def arg_parser():
    parser = argparse.ArgumentParser(description="input file")
    parser.add_argument('input_file', help = 'please provide input file.', type = argparse.FileType('r'))
    return parser

def main(argv: List[str]) -> int:
    input = arg_parser().parse_args(argv[1:]).input_file
    print(review_Sue(input))
    
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))