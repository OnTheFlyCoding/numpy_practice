import numpy as np

rng = np.random.default_rng() #remove seed to random the order of the suffle
array = np.array([1,2,3,4,5])
fruits = np.array(['🍊','🍍','🥥','🍎','🍐'])
fruit = rng.choice(fruits)
threeFruit = rng.choice(fruits,size=(3,3))
print(fruit)
print(threeFruit)
# rng.shuffle(array)
# rng.shuffle(fruits)
# print(array)
# print(fruits)