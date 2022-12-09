import numpy as np

def logit(x):
    return -3.98 + 0.1*x[::, 0] + 0.5*x[::, 1]
def p(x):
    return 1/(1+np.exp(-logit(x)))

exec(input().strip())
