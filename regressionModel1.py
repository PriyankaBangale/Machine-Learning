dataset = [[1,14], [2,10], [4,12], [5,8], [6,9], [6,6], [8,3], [9,4], [11, 3], [12,1]]
X, Y = list(), list()

for i in dataset:
    X.append(i[0])
    Y.append(i[1])

# Step 1
Xmean = float(sum(X))/len(X)
Ymean = float(sum(Y))/len(Y)

#Step 2
mslope1, mslope2 = 0, 0
for i in range(len(X)):
    mslope1 += (X[i] - Xmean) * (Y[i] -Ymean)
    mslope2 += (X[i] - Xmean) ** 2

M = mslope1/mslope2

# Step 3
yy = Ymean - M * Xmean

print M*9 + yy