f = open("./d18_input.txt")
math = []
for line in f:
    line = line.strip().split(" ")
    temp = []
    for x in line:
        for char in x:
            if char in "()*+":
                temp.append(char)
            else:
                temp.append(int(char))
    math.append(temp)

# def newMath(exp, i = 0):
#     res = 0
#     op = "+"
#     mult = []
#     while i < len(exp):
#         x = exp[i]
#         if isinstance(x,int):
#             if op == "+": 
#                 res += x
#             else: res *= x
#         elif x == "(":
#             temp = newMath(exp,i+1)
#             if op == "+": res += temp[0]
#             else: res *= temp[0]
#             i = temp[1]
#         elif x == ")":
#             break
#         elif x in "*+":
#             op = x
        
#         i += 1
#     return (res,i)

def newMath(exp, i = 0):
    res = 0
    op = "+"
    mult = []
    while i < len(exp):
        x = exp[i]
        if isinstance(x,int):
            if op == "+": 
                res += x
            else: 
                mult.append(res)
                res = x
        elif x == "(":
            temp = newMath(exp,i+1)
            if op == "+": 
                res += temp[0]
            else: 
                mult.append(res)
                res = temp[0]
            i = temp[1]
        elif x == ")":
            break
        elif x in "*+":
            op = x
        i += 1
    for m in mult:
        res*=m
    return (res,i)

total = 0
for expression in math:
    total += newMath(expression)[0]
print(total)