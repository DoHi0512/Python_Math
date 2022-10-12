import math

#함수식
def f(x):
  return math.sin(x) / x
  
#접선의 기울기
def D(g,x):
  h = 1e-5
  return ((g(x+h) - g(x-h)) / (2*h) )

#초기값, 학습율
a = 0.2
r = 0.01

#경사상승법
for i in range(1000):
  a += D(f,a)

print(f(a))
