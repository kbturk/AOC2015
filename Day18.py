import sys, argparse
from copy import deepcopy

from typing import Dict, List, Set, Tuple

def arg_parser():
    parser = argparse.ArgumentParser(description = 'enter three arguments: number of iterations, part 1 or 2, and puzzle input.')
    parser.add_argument('iterations', help = 'please provide light iteration', type = int)
    parser.add_argument('part', help = 'please enter 1 if this is part 1, 2 if this is part 2 of AoC', type = int)
    parser.add_argument('ifile', help = 'please provide text input file', type = argparse.FileType('r'))
    return parser

def conways_light(iter: int, input: List[str], part = 1) -> int:
    #build the initial state of the universe
    universe: Set[Tuple[int,int]] = set()
    x,y = 0,0
    for line in input:
        x = 0
        for c in line:
            if c == '#':
                universe.add((x,y))
            x += 1
        dim_x = x -1
        y += 1
    dim_y = y -1
    #add corner lights:
    if part == 2:
        for l in [(0,0), (0,dim_y), (dim_x, 0), (dim_x, dim_y)]:
            if l not in universe:
                universe.add(l)
    tick = 0
    while tick <iter:
        potential_new_light: Set[Tuple[int, int]] = set()
        universe_next_tick: Set[Tuple[int, int]] = set()
        #At the start, assume each light has 0 turned on lights:
        for light in universe:
            lit_neighbors = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    #if we run into the edge, pass. This ain't infinite conway.
                    if (part == 2 and
                        light in [(0,0), (0,dim_y), (dim_x, 0), (dim_x, dim_y)] and
                        light not in universe_next_tick):
                        universe_next_tick.add(light)
                    elif (light[0] + i > dim_x or light[0] + i < 0 or 
                          light[1] + j > dim_y or light[1] + j < 0):
                        pass
                    #add new empty lights to be evaluated as turning on:
                    elif (light[0] + i, light[1] + j) not in universe:
                        potential_new_light.add((light[0] + i, light[1] + j))
                    #pass self
                    elif i == j == 0:
                        pass
                    elif (light[0] + i, light[1] + j) in universe:
                        lit_neighbors += 1
            #light stays on if it has 2 or 3 lit neighbors
            if lit_neighbors == 2 or lit_neighbors == 3:
                universe_next_tick.add(light)
        #evaluate and check if turned off lights will be turned on.
        for light in potential_new_light:
            lit_neighbors = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    #if we run into the edge, pass. This ain't infinite conway.
                    if (light[0] + i > dim_x or light[0] + i < 0 or 
                        light[1] + j > dim_y or light[1] + j < 0):
                        pass
                    #ignore self
                    elif i == j == 0:
                        pass
                    elif (light[0] + i, light[1] + j) in universe:
                        lit_neighbors += 1
            if lit_neighbors == 3:
                universe_next_tick.add(light)
        universe = deepcopy(universe_next_tick)
        #advance the universe:
        tick += 1
    return len(universe)

def main(args: List[str]) -> int:
    inputs = arg_parser().parse_args(args[1:])
    input = [line.rstrip('\n') for line in inputs.ifile]
    print(f'conway\'s lights: {conways_light(inputs.iterations, input, part = 2)}')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))