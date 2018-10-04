import cvxpy as cp
import numpy as np

b = np.array([2.7, 2.2, 1.6, 2.3, 1.1])
s = np.array([2, 2.4, 3.2, 2.3, 3])

m = cp.Variable(5)
n = cp.Variable(5)
x = cp.Variable(5)
y = cp.Variable(5)

constraints = []
constraints.append(y[0] == 100)
constraints.append(x[0] == 0)
for i in range(4):
    constraints.append(y[i+1] == y[i] + s[i+1]*n[i+1] - b[i+1]*m[i+1])
    constraints.append(x[i+1] == x[i] + m[i+1] - n[i+1])

constraints.append(m[0] == 0)
constraints.append(n[0] == 0)
for i in range(4):
    constraints.append(n[i+1] <= x[i])
    constraints.append(b[i+1]*m[i+1] <= y[i])
    constraints.append(m[i+1] >= 0)
    constraints.append(n[i+1] >= 0)
    constraints.append(x[i+1] >= 0)
    constraints.append(y[i+1] >= 0)

objective = cp.Maximize(y[4])
prob = cp.Problem(objective, constraints)
prob.solve()
print(y[4].value)
print('Number of Shares Bought per Day')
print(m.value)
print('-------------------------------')
print('Number of Shares Sold per Day')
print(n.value)
print('-------------------------------')
print('Total Money at the End of the Day')
print(y.value)