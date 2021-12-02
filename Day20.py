import sys, argparse
import itertools
from pprint import pprint
from typing import Dict, List, Set, Tuple

def arg_parser():
    parser = argparse.ArgumentParser(description = 'enter one argument: a number for lowest house number.')
    parser.add_argument('house_number', help = 'please provide puzzle input (int)', type = int)
    return parser

def count_houses(goal: int) -> int:
    house: Dict[int,int] = {}
    for i in range(1,goal+1):
        for j in range(i,goal,i):
            if j not in house.keys():
                house[j] = i * 10
            else:
                house[j] += i * 10
    #print(house)
    for k in sorted(house.keys()):
        if house[k] >= goal*10:
            print(k, house[k])
            return k
    return 0

def alt_presents(goal:int) -> int:
    for i in range(1,int(goal/10)+1):
        sum = 0
        for j in range(1,i+1):
            if i%j == 0:
                sum += j*10
        #print(i, sum)
        if sum >= goal:
            return i
    return 0

def count_houses2(goal: int, housenu = 50) -> int:
    house: Dict[int,int] = {}
    for i in range(1,goal+1):
        for j in range(i,housenu*i+1,i):
            if j not in house.keys():
                house[j] = i * 11
            else:
                house[j] += i * 11
    #print(house)
    for k in sorted(house.keys()):
        if house[k] >= goal*10:
            print(k, house[k])
            return k
    return 0

def main(args: List[str]) -> int:
    inputs = arg_parser().parse_args(args[1:]).house_number
    #print(f'{count_houses(int(inputs/10))}')
    #print(f'{alt_presents(int(inputs))}')
    print(f'{count_houses2(int(inputs/10))}')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))