import sys, argparse
import numpy as np
from typing import List, Dict, Tuple, Any

def arg_parser():
    parser = argparse.ArgumentParser(description="Process input file.")
    parser.add_argument('input file', help = 'please provide an AOC file.', type = str)
    return parser

#part one: Santa deals with drunk elves
def santa_houses(s:str) -> Dict[Tuple[Any,...],int]:
    h: Dict[Tuple[Any,...],int] = {(0,0):1}
    current = np.array((0,0))
    cDict = {'^': np.array((0,1)), 'v': np.array((0,-1)), '>': np.array((1,0)), '<':np.array((-1,0))}

    for l in s:
        current += cDict[l]
        #print(current)
        if tuple(current) in h.keys():
            h[tuple(current)] += 1
        else:
            h[tuple(current)] = 1
    return h

#part two: twice the Santa
def two_santa_houses(s:str) -> Dict[Tuple[Any,...],int]:
    cDict = {'^': np.array((0,1)), 'v': np.array((0,-1)), '>': np.array((1,0)), '<':np.array((-1,0))}

    houses: Dict[Tuple[Any,...],int] = {(0,0):2}

    santa_loc = np.array((0,0))
    robo_santa_loc = np.array((0,0))
    i = 0
    for l in s:
        if i%2: #Santa moves first
            santa_loc += cDict[l]
            if tuple(santa_loc) in houses.keys():
                houses[tuple(santa_loc)] += 1
            else:
                houses[tuple(santa_loc)] = 1
        else:
            robo_santa_loc += cDict[l]
            if tuple(robo_santa_loc) in houses.keys():
                houses[tuple(robo_santa_loc)] += 1
            else:
                houses[tuple(robo_santa_loc)] = 1
        print(f'robo location: {robo_santa_loc}, santa location: {santa_loc}')
        i += 1
    return houses

def main(argv: List[str]) -> int:
    arg = arg_parser().parse_args(argv[1:])
    instr: str = ""
    house: Dict[Tuple[Any,...],int] = {}
    with open( argv[1],'r') as f:
        for line in f:
            instr += line.strip('\n')
            #part one:
            house = santa_houses(instr)
            #part two:
            two_santa_house = two_santa_houses(instr)
    #print all:
    print(f'{len(house.keys())}, {len(two_santa_house.keys())}')

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))