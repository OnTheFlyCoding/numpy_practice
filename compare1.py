import numpy as np

scores = np.array([55,78,90,84,100,49,96])
print(scores == 100)
scores[scores<=65] = 0
print(scores)
