import numpy as np

G = np.array(["A", "B", "C", "C"])
grades = np.array(["A", "B", "C"])
points = np.array([4, 3, 1])
print(G.reshape((G.shape[0], 1)) == grades)
ind = np.argmax(G.reshape((G.shape[0], 1)) == grades, axis=1)
print(np.sum(points[ind]))
