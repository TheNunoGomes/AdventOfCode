import numpy as np

def calculatePowerConsumption(data):
    gamma = ''
    base10s, base2s = [int(number, 2) for number in data], data
    msb = 2**(len(base2s[0])-1)

    while base2s[0]:
        gamma += '0' if len([number for number in base10s if number < msb]) > len(base10s)/2 else '1'
        base10s = [number if number < msb else number-msb for number in base10s]
        base2s = [number[1:] for number in base2s]
        msb = 2**(len(base2s[0])-1)
        
    gamma = int(gamma, 2)
    return gamma * (2**len(data[0])-1 - gamma)

def calculateLifeSupportRating(data):
    oxygen = co2 = np.array([int(number, 2)for number in data])
    base2s = data
    o2_msb = co2_msb = 2**(len(data[0])-1)
    
    while len(oxygen) > 1 or len(co2) > 1:
        if len(oxygen) > 1:
            if len(oxygen[oxygen < o2_msb]) > len(oxygen)/2:
                oxygen = oxygen[oxygen < o2_msb]
                o2_msb -= 2**(len(base2s[0])-2)
            else:
                oxygen = oxygen[oxygen >= o2_msb]
                o2_msb += 2**(len(base2s[0])-2)
        if len(co2) > 1:
            if len(co2[co2 < co2_msb]) > len(co2)/2:
                co2 = co2[co2 >= co2_msb]
                co2_msb += 2**(len(base2s[0])-2)
            else:
                co2 = co2[co2 < co2_msb]
                co2_msb -= 2**(len(base2s[0])-2)
        base2s = [number[1:] for number in base2s]

    return oxygen[0] * co2[0]

data = np.genfromtxt('data.txt', dtype = 'str')
        
power = calculatePowerConsumption(data)
lsr = calculateLifeSupportRating(data)

print(power, lsr)