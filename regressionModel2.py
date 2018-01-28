import numpy as np
dataset = np.array([[1,14], [2,10], [4,12], [5,8], [6,9], [6,6], [8,3], [9,4], [11, 3], [12,1]])

# Step 1
Xmean = dataset[:,0].mean()
Ymean = dataset[:,1].mean()

# Step 2
sub =  (dataset - np.array([Xmean, Ymean]))
mul = sub[:,0] * sub[:,1]
M = mul.sum()/((dataset[:,0] - Xmean) ** 2).sum()

# Step 3
yy = Ymean - M * Xmean

print M*12+yy
