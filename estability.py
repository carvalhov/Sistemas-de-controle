import numpy as np

# LEVEL 1
A1 = [[-5.2, 2.5],
     [-9.0, -0.8]]
# LEVEL 2
A2 = [[0, 5],
     [-9, -0.9]]
# LEVEL 3
A3 = [[-1.2 , 2],
     [3.6, -0.4]]
# LEVEL 4
A4 = [[1, -0.4],
     [1.8, 0.2]]

"""
Os autovalores de A, são os polos G(s), de forma que o valor dos autovalores podem dizer se o sistema é instável ou estável
Tal que se os polos são negativos, o sistema é estável e se positivos, o sistema é instável. 
"""

auto_v1 = np.linalg.eigvals(A1)

print(f'Autovelores do nível 1: ' + str(auto_v1))

auto_v2 = np.linalg.eigvals(A2)

print(f'Autovelores do nível 2: ' + str(auto_v2))

auto_v3 = np.linalg.eigvals(A3)

print(f'Autovelores do nível 3: ' + str(auto_v3))

auto_v4 = np.linalg.eigvals(A4)

print(f'Autovelores do nível 4: ' + str(auto_v4))

# O código está okay!