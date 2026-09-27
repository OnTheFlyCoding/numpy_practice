import numpy as np
import pandas as pan


mylist = [1,2,3]
print(f'Printing a python list mylist: {mylist}, that has a type({type(mylist)})');print()

newlist = np.array([1,2,3])
print(f'Printing a numpy list mylist: {newlist}, that has a type({type(newlist)})');print()

print(f'Printing the product of mylist * 2 = {mylist*2}')
print(f'PRinting the product of newlist * 2 = {newlist*2} ')
