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
        return cod not in reserved_tokens + reserved_words
    return True

def detect(program):
    st = SymbolTable()
    pif = PIF()
    prog_in = open('p1.in', 'r')

    line = prog_in.read()

    lnumb = 0

    line_data = re.split('("[^a-zA-Z0-9]")|([^a-zA-Z0-9])', line)
    # line_data = re.split('{|}', line)
    print(line_data)

    line_data = list(filter(None, line_data))
    line_data = map(lambda e: e.strip(), line_data)
    line_data = list(filter(None, line_data))

    print(list(line_data))


    for e in line_data:
        if(is_reserved(e)):
            pif.add(e, 0)
        elif is_ident_const(e):
            index = 0
            try:
                index = st.add(e, 0)
                pif.add(e, index)
            except:
                continue
        else:
            print("Lexical error for " + e)

    print("\nST is:")
    print(st)
    print("PIF is:")
    print(pif)

if __name__ == "__main__":
    detect('p1.in')