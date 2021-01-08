input = open("input.txt","r")
arr = [{}]
for line in input:
    line = line.rstrip()
    if not line:
        arr.append({})
    else:
        line = line.split()
        for pair in line:
            key, value = pair.split(":")
            arr[-1][key] = value

def validBYR(val):
    if not val.isnumeric():
        return False
    return 1920 <= int(val) <= 2002
def validIYR(val):
    if not val.isnumeric():
        return False
    return 2010 <= int(val) <= 2020
def validEYR(val):
    if not val.isnumeric():
        return False
    return 2020 <= int(val) <= 2030
def validHGT(val):
    num, unit = val[:-2], val[-2:]
    if (not num.isnumeric()) or (unit not in ["cm","in"]):
        return False
    if unit == "cm":
        return 150 <= int(num) <= 193
    else:
        return 59 <= int(num) <= 76
def validHCL(val):
    if val[0] != "#" and len(val) != 7:
        return False
    chars = set(["a","b","c","d","e","f","0","1","2","3","4","5","6","7","8","9"])
    for char in val[1:]:
        if char not in chars:
            return False
    return True
def validECL(val):
    colors = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    return val in colors
def validPID(val):
    return len(val) == 9 and val.isnumeric()

def validPassports(arr):
    requiredFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    count = 0
    for passport in arr:
        valid = True
        for field in requiredFields:
            if field not in passport:
                valid = False
            elif field == "byr" and not validBYR(unicode(passport[field])):
                valid = False
            elif field == "iyr" and not validIYR(unicode(passport[field])):
                valid = False
            elif field == "eyr" and not validEYR(unicode(passport[field])):
                valid = False
            elif field == "hgt" and not validHGT(unicode(passport[field])):
                valid = False
            elif field == "hcl" and not validHCL(unicode(passport[field])):
                valid = False
            elif field == "ecl" and not validECL(unicode(passport[field])):
                valid = False
            elif field == "pid" and not validPID(unicode(passport[field])):
                valid = False
            if not valid: break
        count = count+1 if valid else count
    return count

print(validPassports(arr))