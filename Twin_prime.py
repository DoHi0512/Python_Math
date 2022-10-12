from matplotlib import pyplot as plt
import numpy as np
prime = [2,3,5]
ratio = []
t = int(input())
num = np.arange(100,t+1,100)
cnt = 1
for i in range(5,t+1):
  flag = True
  for prime_num in prime:
    if prime_num**2 > i : break
    if i % prime_num == 0 :
      flag = False
      break
      
  if flag == True:
    if prime[-1] + 2 == i : cnt+=1
    prime.append(i)
    
  if i % 100 == 0:
    ratio.append(cnt/len(prime)*100)

plt.plot(num,ratio,label = 'Twin_prime')
plt.ylabel('Percentage')
plt.xlabel('Range')
plt.legend()
plt.show()
