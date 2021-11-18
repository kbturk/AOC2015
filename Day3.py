import sys, argparse
import numpy as np
from typing import List, Dict, Tuple, Any

def arg_parser():
    parser = argparse.ArgumentParser(description="Process input file.")
    parser.add_argument('input file', help = 'please provide an AOC file.', type = str)
    return parser

#Santa deals with drunk elves
def santa_houses(s:str, s2:str = "") -> Dict[Tuple[Any,...],int]:
    h: Dict[Tuple[Any,...],int] = {(0,0):1}
    santa_loc = np.array((0,0))
    cDict = {'^': np.array((0,1)), 'v': np.array((0,-1)), '>': np.array((1,0)), '<':np.array((-1,0))}

    for l in s:
        santa_loc += cDict[l]
        #print(santa_loc)
        if tuple(santa_loc) in h.keys():
            h[tuple(santa_loc)] += 1
        else:
            h[tuple(santa_loc)] = 1

    robo_santa_loc = np.array((0,0))
    if s2 != "":
        h[(0,0)] += 1

    for l in s2:
        robo_santa_loc += cDict[l]
        if tuple(robo_santa_loc) in h.keys():
            h[tuple(robo_santa_loc)] += 1
        else:
            h[tuple(robo_santa_loc)] = 1            
    return h

def main(argv: List[str]) -> int:
    arg = arg_parser().parse_args(argv[1:])
    instr: str = ""
    instr1: str = ""
    instr2: str = ""
    house: Dict[Tuple[Any,...],int] = {}
    with open( argv[1],'r') as f:
        for line in f:
            instr += line.strip('\n')
    #part one:
    house = santa_houses(instr)
    #part two:
    i = 0
    for s in instr:
        if i%2: #Santa moves first
            instr1 += s
        else:
            instr2 += s
        i += 1
    two_santa_house = santa_houses(instr1, instr2)
    #print all:
    print(f'{len(house.keys())}, {len(two_santa_house.keys())}')

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))