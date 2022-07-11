'''Java source code mutation tool

A tool for generating mutated versions of java source code.
'''
import pathlib
import mutation
import sys
from itertools import combinations
MUTATORS = [mutation.AOR, mutation.ROR, mutation.COR, mutation.SOR, mutation.LOR, mutation.ASR]

orn = {
    '+': 'Addition',
    '-': 'Subtraction',
    '*': 'Multiplication',
    '/': 'Division',
    '**': 'Exponentiation',
    '%': 'Modulo',
    '>': 'Greater than',
    '<': 'Less than',
    '>=': 'Greater than or equal to',
    '<=': 'Less than or equal to',
    '==': 'Equal to',
    '!=': 'Not equal to',
    '&&': 'Logical and',
    '||': 'Logical or',
    '&': 'Bitwise and',
    '|': 'Bitwise or',
    '^': 'Bitwise xor',
    '<<': 'Bitwise left shift',
    '>>': 'Bitwise right shift',
    '>>>': 'Bitwise right shift with zero fill',
    '=': 'Assignment',
    '+=': 'Addition assignment',
    '-=': 'Subtraction assignment',
    '*=': 'Multiplication assignment',
    '/=': 'Division assignment',
    '%=': 'Modulo assignment',
    '**=': 'Exponentiation assignment',
    '<<=': 'Bitwise left shift assignment',
    '>>=': 'Bitwise right shift assignment',
    '>>>=': 'Bitwise right shift with zero fill assignment'
}

for op in orn:
    orn[op] = orn[op].replace(' ', '_')

def main():
    if len(sys.argv) < 3:
        print('Usage: main.py <input_dir> <output dir>')
        return
    source_path = sys.argv[1]
    target_path = sys.argv[2]
    source = pathlib.Path(source_path)
    target = pathlib.Path(target_path)
    target.mkdir(parents=True, exist_ok=True)
    paths = source.glob('**/*.java')
    for path in paths:
        with path.open('r') as source_file:
            for mutator_class in MUTATORS:
                for o1, o2 in combinations(mutator_class.OPERATORS, 2):
                    subtarget = target/f'{mutator_class.__name__}_{orn[o1]}_{orn[o2]}'
                    (subtarget/path).parent.mkdir(parents=True, exist_ok=True)
                    with (subtarget/path).open('w') as target_file:
                        mutator = mutator_class(source_file, target_file, o1, o2)
                        mutator.mutate()
                    


if __name__ == '__main__':
    main()
