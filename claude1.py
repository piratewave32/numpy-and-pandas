
import numpy as np

a = np.array([3, 8, 15, 22, 7, 30])
print(np.where(a>10,"Higher","Low"))
print(np.where(a%2,"Divisible","Non-Divisible"))

b =np.array([8, 3, 9, 1, 5])
print(-np.sort(-b))
print(np.unique(np.array([5, 5, 2, 2, 9])))