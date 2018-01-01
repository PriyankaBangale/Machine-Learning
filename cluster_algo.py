from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

dataset = np.array([[3,104], [2,100], [1,81], [101,10], [99,5], [98,2]])
cluster = KMeans(n_clusters=3)

cluster.fit(dataset)
labels = cluster.labels_
centroids = cluster.cluster_centers_

plt.scatter(dataset[:,0], dataset[:,1])
plt.show()

colors = ['g.', 'r.', 'b.']
for i in range(len(dataset)):
    plt.plot(dataset[i][0], dataset[i][1], colors[labels[i]], markersize = 10)

plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()