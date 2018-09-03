def getAtom(atom):
    atom = atom.strip(' ')
    return(atom)
    if (atom[0] != '¬'): return(atom)
    return('¬' + atom[1:].strip(' '))

def readRules():
    print(input())
    rules = []
    while (True):
        line = input()
        if (line == "END"): break
        print(line)
        antecedent, consequent = line.split("=>")
        rules += [[[getAtom(s) for s in antecedent.split('^')], consequent.strip(' ')]]
    return(rules)

def readBase():
    print(input())
    base = set()
    while (True):
        line = input()
        if (line == "END"): break
        print(line)
        [base.add(symbol) for symbol in line.split()]
    return(base)

def readTarget():
    print(input())
    target = ""
    while (True):
        line = input()
        if (line == "END"): break
        print(line)
        target = line
    return(target)
