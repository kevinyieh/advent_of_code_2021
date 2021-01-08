from collections import defaultdict

f = open("d19_input.txt")
rules = defaultdict(list)
for line in f:
    if line == "\n": break
    k, v = line.split(":")
    v = v.split("|")
    for rule in v:
        rules[k].append(rule.strip("\" \n").split(" "))

messages = []
for line in f:
    messages.append(line.strip())

simpleRules = defaultdict(set)

def simplifyRules(rules, key):
    if key in simpleRules: return list(simpleRules[key])
    build = []
    for rule in rules[key]:
        b = []
        for r in rule:
            if r.isnumeric():
                remaining = simplifyRules(rules,r)
                if not b: 
                    b = remaining
                else:
                    newB = []
                    for x in remaining:
                        for i in range(len(b)):
                            newB.append(b[i] + x)
                    b = newB
            else:
                simpleRules[key] = set(r)
                return [r]
        build.extend(b)
    simpleRules[key] = set(build)
    return build
simplifyRules(rules,"0")

count = 0
for message in messages:
    if message in simpleRules["0"]:
        count += 1
print(count)