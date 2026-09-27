import numpy as np

alphabet = np.array([
    [
        ['A','B','C'],
        ['D','E','F'],
        ['G','H','I']
    ],
    [
        ['J','K','L'],
        ['M','N','O'],
        ['P','Q','R']
    ],
    [
        ['S','T','U'],
        ['V','W','X'],
        ['Y','Z',' ']
    ]])

word = alphabet[0,2,0] + alphabet[0,2,2] + alphabet[1,1,2]
print(alphabet[::])
print(word)