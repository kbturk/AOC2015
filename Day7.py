import sys, argparse
from typing import List, Dict, NamedTuple, Any, Union, Tuple, Iterable
from pprint import pprint

class Named(NamedTuple):
    source: str

class Fixed(NamedTuple):
    value:int

GateSource = Union[Named,Fixed]

class OrGate(NamedTuple):
    lhs: GateSource
    rhs: GateSource

class AndGate(NamedTuple):
    lhs: GateSource
    rhs: GateSource

class NotGate(NamedTuple):
    operand: GateSource

class LShift(NamedTuple):
    operand: GateSource
    shift: int

class RShift(NamedTuple):
    operand: GateSource
    shift:int

Wire = Union[Named, Fixed, OrGate, AndGate, NotGate, LShift, RShift]
Circuit = Dict[str, Wire]

def eval_circ(circuit: Circuit, wire: Wire) -> int:
    match wire:
        case Named(source = s):
            val = eval_circ(circuit, circuit[s])
            circuit[s] = Fixed(value=val)
            return val
        case Fixed(value = v): return v
        case OrGate(lhs=e1,rhs=e2): return eval_circ(circuit, e1) | eval_circ(circuit, e2)
        case AndGate(lhs=e1, rhs=e2): return eval_circ(circuit, e1) & eval_circ(circuit, e2)
        case NotGate(operand = opr): return eval_circ(circuit, opr) ^ 65535
        case LShift(operand = opr, shift = sh): return eval_circ(circuit, opr) << eval_circ(circuit,sh)
        case RShift(operand = opr, shift = sh): return eval_circ(circuit, opr) >> eval_circ(circuit,sh)

def parse_source(source: GateSource) -> Union[Named, Fixed]:
    if type(source) == int:
        return Fixed(source)
    elif source.isdigit():
        return Fixed(int(source))
    else:
        return Named(source)

def parse_wire(line: str) -> Tuple[str, Wire]:
    match line.strip('\n').split():
        case [x, "OR", y, "->", z]: return z, OrGate(parse_source(x), parse_source(y))
        case [x, "AND", y, "->", z]: return z, AndGate(parse_source(x),parse_source(y))
        case ["NOT", x,"->", z]: return z, NotGate(parse_source(x))
        case [x, "LSHIFT", y, "->", z]: return z, LShift(parse_source(x),parse_source(y))
        case [x, "RSHIFT", y, "->", z]: return z, RShift(parse_source(x),parse_source(y))
        case [x,"->", z]: return z, parse_source(x)

def parse_circuit(lines: Iterable[str]) -> Circuit:
    return dict(parse_wire(l) for l in lines)

def arg_parser():
    parser = argparse.ArgumentParser(description="input file.")
    parser.add_argument('input_file', help = 'please provide input file name.', type = str)
    return parser

def main(argv: List[str]) -> int:
    arg = arg_parser().parse_args(argv[1:])
    logic_gate_instr:List[str] = []
    wire_signals: Dict[Any,...] = {}
    with open(arg.input_file, 'r') as f:
        circuit = parse_circuit(f)
    for wire in circuit.keys():
        result = eval_circ(circuit, circuit[wire])
    print(eval_circ(circuit,circuit['a']))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))