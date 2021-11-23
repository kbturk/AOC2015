import sys, argparse, json, itertools
from typing import List, Dict, NamedTuple, Tuple, Any
from pprint import pprint

def arg_parser():
    parser = argparse.ArgumentParser(description="input file")
    parser.add_argument('input_file', help = 'please provide input file.', type = argparse.FileType('r'))
    return parser

def parse_input(party_rules: Dict[str, int], line:str) -> Dict[str,int]:
    sign = None
    match line.rstrip('.\n').split():
        case [a, _, "gain", x, *obj, b]:
            if a in party_rules.keys():
                party_rules[a][b] = int(x)
            else:
                party_rules[a] = {b:int(x)}
        case [a, _, "lose", x, *obj, b]:
            if a in party_rules.keys():
                party_rules[a][b] = -int(x)
            else:
                party_rules[a] = {b: -int(x)}
        case _:
            print(f'sorry, I didn\'t understand that: {line}.')
    return party_rules

def pursuit_of_happiness(party_rules) -> Tuple[int, List[str]]:
    best_happiness:Tuple[int,List[str]] = (0, [])
    options = list(itertools.permutations(party_rules))
    for pursuit in options:
        happiness = 0
        for i in range(len(pursuit)):
            happiness += party_rules[pursuit[i]][pursuit[(i+1)%len(pursuit)]]
            happiness += party_rules[pursuit[(i+1)%len(pursuit)]][pursuit[i]]
        if happiness > best_happiness[0]:
            best_happiness = (happiness, pursuit)
    return best_happiness

def main(argv: List[str]) -> int:
    input = arg_parser().parse_args(argv[1:]).input_file
    party_rules = {}
    guests = []
    for line in input:
        party_rules = parse_input(party_rules, line)
    print(f'best happiness: {pursuit_of_happiness(party_rules)}')
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))