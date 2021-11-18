import sys, argparse
import hashlib
from typing import List, Dict, Tuple, Any

def arg_parser():
    parser = argparse.ArgumentParser(description="mining key.")
    parser.add_argument('mining_key', help = 'please provide secret key.', type = str)
    return parser

#Santa gets rich trading AdventCoins
def main(argv: List[str]) -> int:
    arg = arg_parser().parse_args(argv[1:])
    secret_hohoho = arg.mining_key

    l:int = 1

    while True:
        input_string = secret_hohoho + str(l)
        santa_hex = hashlib.md5(input_string.encode()).hexdigest()
        if santa_hex[0:6] == '000000':
            print(f'password {input_string} generated santa_hex {santa_hex}!')
            break
        l += 1

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))