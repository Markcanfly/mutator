from io import TextIOWrapper

class Mutation:
    def __init__(self, text_in: TextIOWrapper, text_out: TextIOWrapper):
        self.input = text_in
        self.output = text_out

class ReplacementMutation(Mutation):
    '''Replacement Mutation'''
    OPERATORS = []
    def __init__(self, text_in: TextIOWrapper, text_out: TextIOWrapper, src: str, tgt: str):
        super().__init__(text_in, text_out)
        self.src = src
        self.tgt = tgt

    def mutate(self):
        self.input.seek(0)
        for line in self.input:
            self.output.write(line.replace(self.src, self.tgt))

class AOR(ReplacementMutation):
    '''Arithmetic Operator Replacement'''
    OPERATORS = ['+', '-', '*', '/', '**', '%']

class ROR(ReplacementMutation):
    '''Relational Operator Replacement'''
    OPERATORS = ['>', '<', '>=', '<=', '==', '!=']

class COR(ReplacementMutation):
    '''Conditional Operator Replacement'''
    OPERATORS = ['&&', '||', '&', '|', '^']

class SOR(ReplacementMutation):
    '''Shift Operator Replacement'''
    OPERATORS = ['<<', '>>', '>>>']

class LOR(ReplacementMutation):
    '''Logical Operator Replacement'''
    OPERATORS = ['&', '|', '^']

class ASR(ReplacementMutation):
    '''Assignment Operator Replacement'''
    OPERATORS = ['=', '+=', '-=', '*=', '/=', '%=', '**=', '<<=', '>>=', '>>>=']
