import math as m
start = 2
end = 4
ans = 0

def f(x):
  return m.sin(x)

for i in range(100):
  mid = (start + end) / 2
  if f(start) * f(mid) > 0 :
    start = mid
  elif f(mid) == 0 :
    ans = mid
  else:
    end = mid
  ans = mid
print(ans)
