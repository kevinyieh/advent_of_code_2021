f = open("./d6_input.txt","r")
print(f)
total, curAnswers = 0, None
for line in f:
    line = line.rstrip()
    if not line:
        total += len(curAnswers)
        curAnswers = None
    else:
        if curAnswers is None:
            curAnswers = set()
            for char in line: curAnswers.add(char)
        else:
            temp = set()
            for char in line: temp.add(char)
            curAnswers = curAnswers.intersection(temp)
print(total+len(curAnswers))
    