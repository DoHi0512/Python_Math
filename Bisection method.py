start = 0
end = 5
ans = 0

def f(x):
  return x**2-3*x-1
for i in range(100):
  mid = (start + end) / 2
  if f(mid) > 0 :
    print(mid)
    end = mid
  elif f(mid) < 0 :
    print(mid)
    start = mid
  else:
    ans = mid

print(ans)
