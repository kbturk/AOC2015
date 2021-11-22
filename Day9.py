import sys, argparse, itertools
from typing import List, Dict, NamedTuple, Tuple

def arg_parser():
    parser = argparse.ArgumentParser(description="input file.")
    parser.add_argument('input_file', help = 'please provide input file name.', type = str)
    return parser

def shortest_path(sleigh_routes: Dict[str,Dict[str,int]], cities: List[str]) -> int:
    short_way: Tuple(int,List[str]) = (2**10, cities)
    all_paths = list(itertools.permutations(cities))
    for path in all_paths:
        dist = 0
        for i in range(len(path)-1):
            try:
                dist += sleigh_routes[path[i]][path[i+1]]
            except:
                try:
                    dist += sleigh_routes[path[i+1]][path[i]]
                except:
                    print(f'ran into an error on: {path}')
                    dist = 2**10
        #print(dist, path)
        if dist < short_way[0]:
            short_way = (dist, path)
    return short_way

def longest_path(sleigh_routes: Dict[str,Dict[str,int]], cities: List[str]) -> int:
    long_way: Tuple(int,List[str]) = (0, cities)
    all_paths = list(itertools.permutations(cities))
    for path in all_paths:
        dist = 0
        for i in range(len(path)-1):
            try:
                dist += sleigh_routes[path[i]][path[i+1]]
            except:
                try:
                    dist += sleigh_routes[path[i+1]][path[i]]
                except:
                    print(f'ran into an error on: {path}')
                    dist = 0
        #print(dist, path)
        if dist > long_way[0]:
            long_way = (dist, path)
    return long_way

def air_routes(sleigh_routes: Dict[str,Dict[str,int]], cities: List[str], line:str) -> Tuple[Dict[str,Dict[str,int]], List[str]]:
    match line.rstrip('\n').split():
        case [a, "to", b, "=", c]:
            if a in sleigh_routes.keys():
                sleigh_routes[a][b] = int(c)
            else:
                sleigh_routes[a] = {b:int(c)}
            if a not in cities:
                cities.append(a)
            if b not in cities:
                cities.append(b)
        case _:
            print(f"sorry, line: {line} didn't match pattern.")
    return sleigh_routes, cities

def main(argv: List[str]) -> int:
    arg = arg_parser().parse_args(argv[1:])
    sleigh_routes: Dict[str,Dict[str,int]] = {}
    cities:List[str] = []
    with open(arg.input_file, 'r') as f:
        for line in f:
            map, cities = air_routes(sleigh_routes, cities, line)
    #print(map, cities)
    print(f'shortest way: {shortest_path(map, cities)}')
    print(f'longest way: {longest_path(map, cities)}')
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))