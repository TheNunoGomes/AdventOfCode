import numpy as np

def checkBirthYear(byr):
    return 1920 <= byr <= 2002

def checkIssueYear(iyr):
    return 2010 <= iyr <= 2020

def checkExpiryYear(eyr):
    return 2020 <= eyr <= 2030

def checkHeight(height):
    return (height.find("in") != -1 and 59 <= int(height.replace('in', '')) <= 76) or (height.find("cm") != -1 and 150 <= int(height.replace('cm', '')) <= 193)

def validate1(data):
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
                    
            elif field[0] == "hcl":
                import re
                if re.search("^#([a-fA-F0-9]{6})$", field[1]):
                    includedFields = np.append(includedFields, field[0])
            
            elif field[0] == "ecl" and field[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                includedFields = np.append(includedFields, field[0])

            elif field[0] == "pid":
                import re
                if re.search("^([0-9]{9})$", field[1]):
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
        buffer[i] = buffer[i].replace('\n', ' ')
        buffer[i] = buffer[i].split(' ')
        for j in range(len(buffer[i])):
            buffer[i][j] = buffer[i][j].split(':')
    data = buffer
    
#print(validate1(data))

print(checkHeight('194cm'))