import re

from helpers.FA import FiniteAutomataState
from helpers.SymbolTable import SymbolTable
from helpers.PIF import PIF
from helpers.scanner import *

if __name__ == "__main__":
    error = ""
    load_dom()

    prog_ST = SymbolTable()
    prog_PIF = PIF()

    FA_ident = FiniteAutomataState('data/identifier')
    FA_const = FiniteAutomataState('data/constant')

    print(res_words)
    print(seps)
    print(ops)

    input_code = input("read from: ")
    prog_in = open(input_code, 'r')

    line = prog_in.readline()

    line_nr = 1

    while line:
        code_data = tokenize(line.strip())

        for token in code_data:
            if token in res_words + seps + ops:
                if token == ' ':
                    continue
                prog_PIF.add(token, (-1, -1))

            elif FA_ident.accepted(token):
                id = prog_ST.add(token, 0)
                prog_PIF.add(token, id)

            elif FA_const.accepted(token):
                const = prog_ST.add(token, 0)
                prog_PIF.add(token, [prog_ST.hash(token), const])
            else:
                print("Lexical error for", token, "at line", line_nr)

        line = prog_in.readline()

        line_nr += 1

    stout = open("sym.out", "w")
    stout.write(str(prog_ST))

    pifout = open("pif.out", "w")
    pifout.write(str(prog_PIF))
