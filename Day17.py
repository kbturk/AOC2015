import sys, argparse, itertools
from typing import List, Dict, NamedTuple, Tuple, Iterable
from pprint import pprint
from itertools import combinations

def arg_parser():
    parser = argparse.ArgumentParser(description="total liters and containers")
    parser.add_argument('tot_liters', help = 'please provide total liters to be stored', type = int, nargs = 1)
    parser.add_argument('containers', help = 'please provide container sizes.', type = int, nargs = "+")
    return parser

def combin(tot_liters: int, containers: List[int], part = 1) -> int:
    tot = 0
    min_cont = False
    seen: List[List[int]] = []

    for i in range(len(containers)):
        eggnog_solutions = combinations(containers, i)
        for eggnog in eggnog_solutions:
            if sum(eggnog) == tot_liters:
                min_cont = True
                if sorted(list(eggnog)) not in seen:
                    seen.append(sorted(list(eggnog)))
                    mult_sum = 1
                    for y in eggnog:
                        if containers.count(y) - eggnog.count(y) > 0:
                            mult_sum *= containers.count(y) - eggnog.count(y) + 1
                    tot += mult_sum
        if part == 2:
            if min_cont:
                return tot
    return tot

def main(argv: List[str]) -> int:
    input = arg_parser().parse_args(argv[1:])
    print(combin(input.tot_liters[0], input.containers, 2))


    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))