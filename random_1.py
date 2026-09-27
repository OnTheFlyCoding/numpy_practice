import numpy as np
np.random.seed(seed=1)#will print the same thing every time
rng = np.random.default_rng(seed=1) #rng will print the same thing every time unless seed removed
print(rng.integers(1,9,size=(2,2)))
print(np.random.uniform(size=(2,2))*10)