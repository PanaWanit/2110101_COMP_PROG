x = list(map(float, input().strip("[]").split(",")))
y = list(map(float, input().strip("[]").split(",")))

print(x, "+", y, "=", [x[i]+y[i] for i in range(3)])
