import sys
from typing import List, Dict, NamedTuple, Tuple
from copy import deepcopy



def look_and_say(input: str, times: int) -> List[int]:
    duplicate = None
    digits:List[int] = [int(l) for l in input]
    next_digits:List[int] = []
    count: int = 1
    i = 0
    while i < times:
        for j in range(1,len(digits)):
            if digits[j-1] == digits[j]:
                count +=1
            else:
                next_digits.extend([count, digits[j-1]])
                count = 1
        next_digits.extend([count,digits[-1]])
        count = 1
        digits = deepcopy(next_digits)
        next_digits = []
        i += 1
    return digits

def main(argv: List[str]) -> int:
    print(len(look_and_say(argv[1], int(argv[2]))))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))