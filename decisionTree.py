from sklearn.tree import DecisionTreeClassifier
import numpy as np
dataset = np.array([[0.0, 1.0, 1.0], [1.0, 1.0,1.0],
    [1.0, 0.0, 1.0], [1.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],[0.0,1.0, 1.0],
    [0.0, 1.0, 1.0], [0.0, 1.0, 1.0],
    [0.0, 1.0, 1.0], [1.0, 0.0, 0.0]]
                    )
labels = ['SELECTED', 'SELECTED', 'SELECTED', 'SELECTED', 'SELECTED', 'NOT SELECTED',
          'NOT SELECTED', 'NOT SELECTED', 'NOT SELECTED', 'NOT SELECTED']
predict = np.array([[1.0, 0.0, 0.0]])

clf=DecisionTreeClassifier(criterion='entropy')
clf.fit(dataset, labels)
print clf.predict(predict)