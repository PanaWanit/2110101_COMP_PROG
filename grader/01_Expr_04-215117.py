from math import *

w = float(input())
h = float(input())

print(sqrt(w*h)/60)
print(2.4265e-2 * w**0.5378 * h**0.3964)
print(3.33e-2 * w **(0.6157-0.0188*log(w, 10)) * h**0.3)
