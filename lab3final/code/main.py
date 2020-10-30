from SymbolTable import SymbolTable
from PIF import PIF
import re

reserved_words = ['array', 'const', 'do', 'else', 'if', 'int', 'elif', 'while', 'for', 'range', 'class', 'struct', 'string', 'float', 'char', 'boolean', 'input', 'WRITE', 'READ', 'fun', 'entry']
reserved_tokens = ['{', '}', ';', '"', '(', ')', '+', '-', '*', '/', '=', '<', '<=', '==', '=>', '===', '>', '~', '%', '&', '^']

def is_reserved(cod):
    return cod in reserved_words + reserved_tokens

def is_ident_const(cod):
    try:
        prefix = int(cod[0])
    except:
        if cod[0] == "'" and cod[-1] == "'" or cod[0] == "\"" and cod[-1] == "\"":
            return True
        elif cod[0] == "'" and cod[-1] != "'" or cod[0] == "\"" and cod[-1] != "\"":
            return False
        elif cod[0] != "'" and cod[-1] == "'" or cod[0] != "\"" and cod[-1] == "\"":
            return False

        if cod[0] == '+' or cod[0] == '-':
            try:
                prefix = int(cod[1:])
                if prefix == 0:
                    return False
                return True
            except:
                return False

        return cod not in reserved_tokens + reserved_words
    return True

def detect(program):
    pname = program.split('.')
    st = SymbolTable()
    pif = PIF()
    prog_in = open(program, 'r')
    PIF_out = open(pname[0]+"_PIF.out", "w+")
    ST_out = open(pname[0]+"_ST.out", "w+")
    CONS_out = open(pname[0]+"_ERR.out", "w+")

    line = prog_in.readline()

    code_data = re.split('([^"\'\+\-a-zA-Z0-9])', line)

    code_data = list(filter(None, code_data))
    code_data = map(lambda e: e.strip(), code_data)
    code_data = list(filter(None, code_data))

    line_nr = 1

    while line:
        for e in code_data:
            if (is_reserved(e)):
                pif.add(e, 0)
            elif is_ident_const(e):
                index = 0
                try:
                    index = st.add(e, 0)
                    pif.add(e, [st.hash(e), index])
                except:
                    continue
            else:
                print("Lexical error for", e, "at line", line_nr)

        line = prog_in.readline()

        code_data = re.split('([^"\'\+\-a-zA-Z0-9])', line)

        code_data = list(filter(None, code_data))
        code_data = map(lambda e: e.strip(), code_data)
        code_data = list(filter(None, code_data))

        line_nr += 1

    ST_out.write("Using HashTable for data representation\n\n")
    for e in st:
        ST_out.write(str(e))
        ST_out.write('\n')

    for e in pif:
        PIF_out.write(str(e))
        PIF_out.write('\n')

if __name__ == "__main__":
    detect('p1.in')