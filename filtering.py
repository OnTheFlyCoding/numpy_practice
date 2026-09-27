import numpy as np

array = np.array([
    [21,18,19,28,65,22,27,17],
    [16,22,20,80,19,27,21,17]
])
teenagers = array[array<18]
adults = array[(array>18) & (array<65)]
seniors = array[array>=65]
evens = array[array%2 ==0]
adults2 = np.where(array>18, array,0)
print(teenagers)
print(adults)
print(seniors)
print(f'Printing only evens: {evens}')
print(f'This should retain the same size as the original array:\n{adults2}')