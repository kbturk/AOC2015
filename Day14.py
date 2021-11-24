import sys, argparse, json, itertools
from typing import List, Dict, NamedTuple, Tuple, Any
from pprint import pprint

def arg_parser():
    parser = argparse.ArgumentParser(description="input file")
    parser.add_argument('input_file', help = 'please provide input file.', type = argparse.FileType('r'))
    parser.add_argument('race_time', help = 'please provide race time as second argument.', type = int)
    return parser

def mathlete(reindeer_stats: Dict[str,Dict[str,int]], time:int) -> List[Tuple[str, float]]:
    deerdistance: List[Tuple[str,float]] = []
    distance:float = 0
    for deer in reindeer_stats.keys():
        tot_time = reindeer_stats[deer]['for']+ reindeer_stats[deer]['rest']
        distance = reindeer_stats[deer]['fly']*reindeer_stats[deer]['for']*(time//tot_time)
        if time % tot_time >= reindeer_stats[deer]['for']:
            distance += reindeer_stats[deer]['fly']*reindeer_stats[deer]['for']
        else:
            for i in range(time % tot_time + 1):
                distance += reindeer_stats[deer]['fly']
        deerdistance.append((deer, distance))
    return deerdistance

def fastest_deer(race_stats: Dict[str, List[int]]) -> List[str]:
    winner: List[str] = [] 
    dist: int = 0
    for deer in race_stats.keys():
        if race_stats[deer][0] > dist:
            winner = [deer]
            dist = race_stats[deer][0]
        elif race_stats[deer][0] == dist:
            winner.append(deer)
    return winner

def deer_position(reindeer_stats: Dict[str,Dict[str,int]],time) -> Dict[str,List[int]]:
    race_stats: Dict[str, List[int]] = {}
    for x in reindeer_stats.keys():
        race_stats[x] = [0,0]
    for i in range(time):
        for deer in race_stats.keys():
            tot_time = reindeer_stats[deer]['for']+ reindeer_stats[deer]['rest']
            if i % tot_time < reindeer_stats[deer]['for']:
                race_stats[deer][0] += reindeer_stats[deer]['fly']
        fastest_deers = fastest_deer(race_stats)
        for deers in fastest_deers:
            race_stats[deers][1] += 1
    return race_stats

def main(argv: List[str]) -> int:
    input = arg_parser().parse_args(argv[1:]).input_file
    time = arg_parser().parse_args(argv[1:]).race_time
    reindeer_stats:Dict[str,Dict[str,int]] = {}
    for line in input:
        name, _,_, x,_,_, y, _,_,_,_,_,_,z,_ = line.rstrip('.\n').split()
        reindeer_stats[name] = {'fly': int(x), 'for': int(y), 'rest':int(z)}
    #print(mathlete(reindeer_stats, time))
    metalists = deer_position(reindeer_stats, time)
    print(metalists)
    sum = 0
    for k in metalists:
        sum += metalists[k][1]
    print(sum)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))