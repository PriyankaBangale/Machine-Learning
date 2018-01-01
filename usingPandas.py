import pandas as pd
dataset = {'A':600, 'B':470, 'C':170, 'D':430, 'E':300}
mydataset = pd.Series(dataset)

maxT = mydataset.mean() + mydataset.std()
minT = mydataset.mean() - mydataset.std()

print ("Taller Doggies: ", mydataset[mydataset > maxT])
print ("Shorter Doggies: ", mydataset[mydataset < minT])
