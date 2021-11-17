import sys, argparse
from typing import List, Dict

class lwh:
    def __init__(self, data):
        self.l = int(data[0])
        self.w = int(data[1])
        self.h = int(data[2])

    def surface_area(self) -> List[int]:
        return 2*[self.l*self.w, self.w*self.h, self.h*self.l]

    def sa_min(self) -> int:
        return min(self.surface_area())

    def vol(self) -> int:
        return self.l * self.w * self.h

    def sht_perm_dist(self) ->int:
        return min([2*(self.l+self.w),2*(self.w+self.h), 2*(self.h+self.l)])

def arg_parser():
    parser = argparse.ArgumentParser(description="Process input file.")
    parser.add_argument('input file', help = 'please provide an AOC file.', type = str)
    return parser

def main(argv: List[str]) -> int:
    arg = arg_parser().parse_args(argv[1:])
    paper = 0
    ribbon = 0
    with open( argv[1],'r') as f:
        for line in f:
            package:lwh = lwh(line.strip('\n').split('x'))
            paper += sum(package.surface_area()) + package.sa_min()
            ribbon += package.vol() + package.sht_perm_dist()
    #part one:
    print(paper)
    #part two:
    print(ribbon)

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))