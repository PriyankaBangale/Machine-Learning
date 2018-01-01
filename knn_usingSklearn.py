from sklearn.neighbors import KNeighborsClassifier
import numpy as np

dataset = np.array([[3,104], [2,100], [1,81], [101,10], [99,5], [98,2]])
labels = ['Romance', 'Romance', 'Romance', 'Action', 'Action', 'Action']

predict = np.array([[18, 90]])
clf = KNeighborsClassifier()
clf.fit(dataset, labels)
print (clf.predict(predict))
