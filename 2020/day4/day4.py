import numpy as np

def checkBirthYear(byr):
    return 1920 <= byr <= 2002

def checkIssueYear(iyr):
    return 2010 <= iyr <= 2020

def checkExpiryYear(eyr):
    return 2020 <= eyr <= 2030

def checkHeight(hgt):
    return (hgt.find("in") != -1 and 59 <= int(hgt.replace('in', '')) <= 76) or (hgt.find("cm") != -1 and 150 <= int(hgt.replace('cm', '')) <= 193)

def checkHairColor(hcl):
    import re
    return re.search("^#([a-fA-F0-9]{6})$", hcl) != None

def checkEyeColor(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def checkPassportId(pid):
    import re
    return re.search("^([0-9]{9})$", pid) != None

def validate1(data):
    requiredFields = np.array(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    validPassports = 0
    for passport in data:
        if len(passport) < 7:
            continue
        includedFields = np.array([])
        for field in passport:
            if field[0] == "byr":
                includedFields = np.append(includedFields, field[0])
            
            elif field[0] == "iyr":
                includedFields = np.append(includedFields, field[0])
            
            elif field[0] == "eyr":
                includedFields = np.append(includedFields, field[0])
            
            elif field[0] == "hgt":
                includedFields = np.append(includedFields, field[0])
                    
            elif field[0] == "hcl" :
                includedFields = np.append(includedFields, field[0])
            
            elif field[0] == "ecl":
                includedFields = np.append(includedFields, field[0])

            elif field[0] == "pid":
                includedFields = np.append(includedFields, field[0])

        if np.array_equal(sorted(includedFields), sorted(requiredFields)):
            validPassports += 1
    return validPassports
    
def validate2(data):
    requiredFields = np.array(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    validPassports = 0
    for passport in data:
        if len(passport) < 7:
            continue
        includedFields = np.array([])
        for field in passport:
            if field[0] == "byr" and checkBirthYear(int(field[1])):
                includedFields = np.append(includedFields, field[0])
            
            elif field[0] == "iyr" and checkIssueYear(int(field[1])):
                includedFields = np.append(includedFields, field[0])
            
            elif field[0] == "eyr" and checkExpiryYear(int(field[1])):
                includedFields = np.append(includedFields, field[0])
            
            elif field[0] == "hgt" and checkHeight(field[1]):
                includedFields = np.append(includedFields, field[0])
                    
            elif field[0] == "hcl" and checkHairColor(field[1]):
                includedFields = np.append(includedFields, field[0])
            
            elif field[0] == "ecl" and checkEyeColor(field[1]):
                includedFields = np.append(includedFields, field[0])

            elif field[0] == "pid" and checkPassportId(field[1]):
                includedFields = np.append(includedFields, field[0])

        if np.array_equal(sorted(includedFields), sorted(requiredFields)):
            validPassports += 1
    return validPassports
    
def read_blocks(file):
    block = ''
    for line in file:
        if line.startswith('>') and len(block)>0:
            yield block
            block = ''
        block += line
    yield block
    
def cleanData(data):
    for passport in data:
        passport.replace('\n', ' ')

with open('data.txt') as f:
    for block in read_blocks(f):
        buffer = block.split('\n\n')
    for i in range(len(buffer)):
        buffer[i] = buffer[i].replace('\n', ' ').split(' ')
        for j in range(len(buffer[i])):
            buffer[i][j] = buffer[i][j].split(':')
    data = buffer
    
valid1 = validate1(data)
valid2 = validate2(data)