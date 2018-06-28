import numpy as np

# question 1
arr = np.array([1,2,3,4,5,6,8,9])

#question 2
arr3 = np.array([1,2,3],[4,5,6],[7,8,9])

#question 
mod= 0;
for items in arr:
    mod = items%2
    if(mod == 1):
        print(items)