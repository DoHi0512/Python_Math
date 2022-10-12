import sympy as sp
def f(x):
  return x**4 - 4*x**3 + 3


a = 2
r = 0.01
h = 1e-5


for i in range(10000000):
  m = (f(a+h) - f(a-h)) /(2*h)
  a -= m * r
 
print(f(a))
