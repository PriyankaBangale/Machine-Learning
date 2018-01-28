from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

dataset = np.array([[1,14],
                    [2,10],
                    [4,12], [5,8],
                    [6,9], [6,6], [8,3],
                    [9,4], [11, 3],
                    [12,1]])

regr = LinearRegression()
X = dataset[:,0].reshape(len(dataset),1)
Y = dataset[:,1].reshape(len(dataset), 1)
predict = np.array([[14]])

regr.fit(X, Y)

# Plotting a graph
plt.scatter(X, Y,  color='black')
X = list(X)
X.append(predict)
X = np.array(X)

plt.plot(X, regr.predict(X), color='blue',linewidth=3)
plt.show()
