class Rule:

    def __init__(self):
        self.conds = []
        self.cons = []

    def addCondition(self, cond):
        self.conds.append(cond)

    def addConsequence(self, cons):
        self.cons.append(cons)

    def satisfy(self, conds):
        if not conds:
            return False
        temprules = self.conds[:]
        instance = conds[0].split('(')[1].split(')')[0]
        for i in range(len(temprules)):
            splitted = temprules[i].split('(')
            temprules[i] = splitted[0] + '(' + instance + ')'
        for c in temprules:
            if c not in conds:
                return False
        return True

    def getConsequenceInstance(self, facts):
        if not facts:
            return []

        tempcons = self.cons[:]
        instance = facts[0].split('(')[1].split(')')[0]
        for i in range(len(tempcons)):
            tempcons[i] = tempcons[i].split('(')[0] + '(' + instance + ')'
        return tempcons


def loadRules():
    rules = []
    rulein = input()
    while rulein:
        rulein = rulein.replace("if", "")
        condcons = rulein.split('then')
        conds = condcons[0].split('and')
        rule = Rule()
        for c in conds:
            c = c.strip()
            rule.addCondition(c)
        cons = condcons[1].split('and')
        for c in cons:
            c = c.strip()
            rule.addConsequence(c)
        rules.append(rule)
        rulein = input()
    return rules

def loadGeneric():
    goals = []
    goal = input()
    while goal:
        goals.append(goal)
        goal = input()
    return goals

def consNotInFacts(cons, facts):
    for c in cons:
        if c not in facts:
            return True
    return False


def tryHard(rules, goals, facts):
    while True:
        change = False
        for r in rules:
            if consNotInFacts(r.getConsequenceInstance(facts), facts) and r.satisfy(facts):
                newfacts = r.getConsequenceInstance(facts)
                facts += newfacts
                print('We now know new facts:', *newfacts)
                change = True
        if not change:
            break
    for g in goals:
        if g in facts:
            print("Goal", g, ": OK")
        else:
            print("Goal", g, ": FAIL")






print("Please enter the rules (possible formats are described in the README). When you are finished, press ENTER two times:")
rules = loadRules()
print("Please enter the facts:")
facts = loadGeneric()
print("Now enter the goals:")
goals = loadGeneric()
tryHard(rules, goals, facts)
