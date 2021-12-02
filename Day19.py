import sys, argparse
from copy import deepcopy
from pprint import pprint
from typing import Dict, List, Set, Tuple

def arg_parser():
    parser = argparse.ArgumentParser(description = 'enter two arguments: the replacement file and original formula.')
    parser.add_argument('replacement_file', help = 'please provide text input file', type = argparse.FileType('r'))
    parser.add_argument('initial_formula', help = 'please provide Rudolf\'s original medicine formula', type = str)
    return parser

def book_builder(instructions: List[str]) -> Dict[str,List[str]]:
    replacement_book: Dict[str,List[str]] = {'e':[]}
    for line in instructions:
        a, _, b = line.split()
        if a not in replacement_book.keys():
            replacement_book[a] = [b]
        else:
            replacement_book[a].append(b)
    #pprint(replacement_book)
    return replacement_book

def rev_book_builder(instructions: List[str]) -> Dict[str,List[str]]:
    replacement_book: Dict[str,List[str]] = {}
    for line in instructions:
        a, _, b = line.split()
        if b not in replacement_book.keys():
            replacement_book[b] = [a]
        else:
            replacement_book[b].append(a)
    pprint(replacement_book)
    return replacement_book

def make_rudolf_meds(instructions: List[str], formula: str) -> int:
    steps = 0
    current_formula = deepcopy(formula)
    rev_replacement_book = rev_book_builder(instructions)
    greedy_search = sorted(rev_replacement_book.keys(),key=lambda x: len(x), reverse= True)
    print(greedy_search)

    i = 0
    while set(current_formula) != {'e'}:
        for l in greedy_search:
            if l in current_formula:
                print(f'{l} found in {current_formula}')
                current_formula = current_formula.replace(l,rev_replacement_book[l][0],1)
                steps += 1
            if 
    return steps

def rudolf_med_combos(instructions: List[str], initial_formula: str) -> int:
    replacement_book = book_builder(instructions)
    seen: Set[str]= set()
    new_form:str = ""
    for item in replacement_book.keys():    
        for i in range(len(initial_formula)):
            if initial_formula[i] == item:
                for l in replacement_book[item]:        
                    new_form = initial_formula[:i]+l+initial_formula[i+1:]
                    #pprint(new_form)
                    if new_form not in seen:
                        seen.add(new_form)
        for i in range(len(initial_formula)-2):
            if initial_formula[i:i+2] == item:
                for l in replacement_book[item]:        
                    new_form = initial_formula[:i]+l+initial_formula[i+2:]
                    #pprint(f'{item} == {initial_formula[i:i+2]}')
                    if new_form not in seen:
                        seen.add(new_form)
    return len(seen)

def main(args: List[str]) -> int:
    inputs = arg_parser().parse_args(args[1:])
    instructions = [line.rstrip('\n') for line in inputs.replacement_file]
    print(f'Rudolf\'s medicine:\n Possible combos:{rudolf_med_combos(instructions, inputs.initial_formula)}')
    print(f'Number of steps needed {make_rudolf_meds(instructions, inputs.initial_formula)}')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))