x = 2

h = 1e-5

def f(x):
  return x**2 - 3*x - 1

for i in range(10):
  m = (f(x+h) - f(x)) / h
  x += -f(x)/m
  print(x)

