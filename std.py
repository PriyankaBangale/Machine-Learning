import math
dataset = {'A':600, 'B':470, 'C':170, 'D':430, 'E':300}

mean = sum(dataset.values())/len(dataset)
sum = 0
for dog, data in dataset.items():
    square = (data - mean) ** 2
    sum += square
print ("mean = ", mean)
var = sum / len(dataset)
print( "variance =", var)
std = int(math.sqrt(var))
print( "standard deviation = ",  std)
maxT = mean + std
minT = mean - std

print( "max threshold = ", maxT)
print( "min threshold = ", minT)

for dog in dataset.keys():
    if dataset[dog] > maxT:
        print ("Dog %s is tall" %(dog))
    elif dataset[dog] < minT:
        print ("Dog %s is short" %(dog))
    else:
        print( "Dog %s is average"  %(dog))

