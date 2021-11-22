import sys, argparse
from typing import List, Dict, NamedTuple, Tuple
from string import ascii_lowercase

def santa_check(pwd:str) -> bool:
    first_check, second_check, third_check, third_check1 = False, True, False, False
    #first check: pwd must include straight of at least three letters
    for i in range(len(pwd)-2):
        if pwd[i:i+3] in ascii_lowercase:
            first_check = True
    #second check: pwd may not contain letters i,o,l
    for j in ['i','o','l']:
        if j in pwd:
           second_check = False
    #third check: pwd must contain two non-overlapping pairs of letters, like aa, bb, cc
    i = 0
    while i < len(pwd)-1:
        if third_check1:
            if pwd[i] == pwd[i+1]:
                third_check = True
        elif pwd[i] == pwd[i+1]:
            third_check1 = True
            i += 1
        i += 1
    return first_check and second_check and third_check

def pwd_increment(pwd:str) -> str:
    i = 0
    while not santa_check(pwd):
        fwd = list(pwd)
        if 'i' in pwd or 'o' in pwd or 'l' in pwd:
            if 'i' in fwd:
                start = fwd.index('i')
            elif 'o' in fwd:
                start = fwd.index('o')
            elif 'l' in fwd:
                start = fwd.index('l')
            fwd[start] = chr(ord(fwd[start])+1)
            if start != len(fwd)-1:
                for j in range(start+1,len(fwd)):
                    fwd[j] = 'a'
        rev = fwd[::-1]
        for i in range(len(rev)):
            if rev[i] == "z":
                rev[i] = "a"
            else:
                rev[i] = chr(ord(rev[i])+1)
                break
        pwd = "".join(rev[::-1])
        santa_check(pwd)
    return pwd

def arg_parser():
    parser = argparse.ArgumentParser(description="password string")
    parser.add_argument('password_string', help = 'please provide 8 char starting password.', type = str)
    return parser

def main(argv: List[str]) -> int:
    init_password = arg_parser().parse_args(argv[1:]).password_string
    print(pwd_increment(init_password))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))