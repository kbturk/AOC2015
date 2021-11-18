import sys, argparse
import numpy as np
from typing import List, Dict, Tuple, Any
from copy import deepcopy

def arg_parser():
    parser = argparse.ArgumentParser(description="input file.")
    parser.add_argument('input_file', help = 'please provide input file name.', type = str)
    return parser

#Part 1: lights can only be on or off
def christmas_light_parse(instr: List[str],christmas_lights):
    i = 0
    if instr[0] == 'turn':
        x1,y1,x2,y2 = [int(co) for co in instr[2].split(',') + instr[4].split(',')]

        if instr[1] == 'on':
            turn = 1
        elif instr[1] == 'off':
            turn = 0
        else:
            print('ERROR in christmas_light_parse on turn')
            return christmas_lights

        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                christmas_lights[i,j] = turn

    elif instr[0] == 'toggle':
        x1,y1,x2,y2 = [int(co) for co in instr[1].split(',') + instr[3].split(',')]
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                christmas_lights[i,j] = int(not(christmas_lights[i,j]))
    else:
        print('ERROR in christmas_light_parse.  First word was not toggle or turn')
    return christmas_lights

#Part 2: BEHOLD THE POWER OF LEDs
def christmas_LED_parse(instr: List[str],christmas_lights):
    i = 0
    if instr[0] == 'turn':
        x1,y1,x2,y2 = [int(co) for co in instr[2].split(',') + instr[4].split(',')]
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if instr[1] == 'on':
                    christmas_lights[i,j] += 1
                elif instr[1] == 'off':
                    christmas_lights[i,j] = max(christmas_lights[i,j] - 1, 0)
                else:
                    print('ERROR in christmas_light_parse on turn')
                    return christmas_lights
    elif instr[0] == 'toggle':
        x1,y1,x2,y2 = [int(co) for co in instr[1].split(',') + instr[3].split(',')]
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                christmas_lights[i,j] += 2
    else:
        print('ERROR in christmas_light_parse.  First word was not toggle or turn')
    return christmas_lights

#How the hell do I untangle all these light instructions?
def main(argv: List[str]) -> int:
    arg = arg_parser().parse_args(argv[1:])
    christmas_lights = np.zeros((1000,1000), dtype=int)
    christmas_LEDs = deepcopy(christmas_lights)
    light_config:List[str] = []
    with open(arg.input_file, 'r') as f:
        for line in f:
            light_config = (line.strip('\n').split())
            #christmas_lights = christmas_light_parse(light_config,christmas_lights)
            christmas_LEDs = christmas_LED_parse(light_config, christmas_LEDs)
    #print(sum(sum(christmas_lights)))
    print(sum(sum(christmas_LEDs)))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))