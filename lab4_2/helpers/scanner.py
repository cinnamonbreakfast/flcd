
res_words = []
seps = []
ops = []

def load_dom():
    with open('data/tokens', 'r') as f:
        for i in range(7):
            separator = f.readline().strip()
            if separator == "_":                    # Special case [SPACE]
                separator = " "
            seps.append(separator)
        for i in range(15):
            ops.append(f.readline().strip())
        for i in range(21):
            res_words.append(f.readline().strip())

def getStringToken(line, index):
    token = ''
    quotes = 0

    while index < len(line) and quotes < 2:
        if line[index] == '\'':
            quotes += 1
        token += line[index]
        index += 1

    return token, index


def isPartOfOperator(char):
    for op in ops:
        if char in op:
            return True
    return False


def getOperatorToken(line, index):
    token = ''

    try:
        num = int(line[index:])
        token +=line
        index += 1
        return token, index
    except:
        pass

    while index < len(line) and isPartOfOperator(line[index]):
        token += line[index]
        index += 1

    return token, index


def tokenize(line):
    token = ''
    index = 0
    tokens = []
    while index < len(line):
        if isPartOfOperator(line[index]):
            if token:
                tokens.append(token)

            token, index = getOperatorToken(line, index)
            tokens.append(token)
            token = ''

        elif line[index] == '\'':
            if token:
                tokens.append(token)
            token, index = getStringToken(line, index)
            tokens.append(token)
            token = ''

        elif line[index] in seps:
            if token:
                tokens.append(token)
            token, index = line[index], index + 1
            tokens.append(token)
            token = ''

        else:
            token += line[index]
            index += 1
    if token:
        tokens.append(token)
    return tokens