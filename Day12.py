import sys, argparse, json
from typing import List, Dict, NamedTuple, Tuple, Any
from pprint import pprint

def arg_parser():
    parser = argparse.ArgumentParser(description="JSON input file")
    parser.add_argument('input_file', help = 'please provide 8 char starting password.', type = argparse.FileType('r'))
    return parser

def sum_list(json_file: List[Any]) -> int:
    sum = 0
    for l in json_file:
        if type(l) == dict:
            sum += sum_dict(l)
        elif type(l) == list:
            sum += sum_list(l)
        elif type(l) == int:
            sum += l
    return sum

def sum_dict(json_file: Dict[Any,Any]) -> int:
    sum = 0
    for c in json_file:
        if type(json_file[c]) == dict:
            sum += sum_dict(json_file[c])
        elif type(json_file[c]) == list:
            sum += sum_list(json_file[c])
        elif type(json_file[c]) == int:
            sum += json_file[c]
        elif json_file[c] == 'red':
            return 0
    return sum

def main(argv: List[str]) -> int:
    jsonIF = arg_parser().parse_args(argv[1:]).input_file
    input = json.load(jsonIF)
    print(sum_dict(input))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))