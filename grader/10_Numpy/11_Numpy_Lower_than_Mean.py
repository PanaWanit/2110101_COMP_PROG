import numpy as np

def read_data():
    w = np.array([float(_) for _ in input().split()])
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(_) for _ in input().split()]
    return w, data

def report_lower_than_mean(weight, data) :
    scores = np.sum(weight * data[::, 1:], axis=1)
    mean = np.mean(scores)
    if np.sum(scores < mean)==0:
        print("None")
    else:
        print(", ".join([str(x) for x in data[scores < mean][:, 0]]))

exec(input().strip())
