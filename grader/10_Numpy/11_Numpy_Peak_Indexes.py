import numpy as np

def peak_indexes(x):
    shf_l = x[:-2]
    shf_r = x[2:]
    mid = x[1:-1]
    return np.arange(1, x.shape[0]-1)[(shf_l < mid) & (mid > shf_r)]


def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")
exec(input().strip()) # Don't remove this line
