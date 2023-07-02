import numpy as np
import control.matlab as ct

# LEVEL 1
A1 = [[-5.2, 2.5],
     [-9.0, -0.8]]

B1 = [[3.2],
     [5]]
# LEVEL 2
A2 = [[0, 5],
     [-9, -0.9]]
B2 = [[0],
      [5]]
# LEVEL 3
A3 = [[-1.2 , 2],
     [3.6, -0.4]]
B3 = [[0],
     [-5]]
# LEVEL 4
A4 = [[1, -0.4],
     [1.8, 0.2]]
B4 = [[0.6],
       [-5]]
# MATRIZ DE CONTROLABILIDADE E NUMERO DE ESTADOS INCONTROLÁVEIS
C1 = ct.ctrb(A1, B1)
print(C1)
unco1 = (len(A1)) - np.linalg.matrix_rank(C1)
C2 = ct.ctrb(A2, B2)
unco2 = (len(A2)) - np.linalg.matrix_rank(C2)
C3 = ct.ctrb(A3, B3)
unco3 = (len(A3)) - np.linalg.matrix_rank(C3)
C4 = ct.ctrb(A4, B4)
unco4 = (len(A4)) - np.linalg.matrix_rank(C4)

if unco1 == 0:
    print("O nivel 1 é um sistema controlável!")
else:
    print("Uma pena, o sistema do nível 1 é incontrolável :-( ")
if unco2 == 0:
    print ("O nivel 2 é um sistema controlável!")
else:
    print("Uma pena, o sistema do nível 2 é incontrolável :-( ")
if unco3 == 0:
    print("O nivel 3 é um sistema controlável!")
else:
    print("Uma pena, o sistema do nível 3 é incontrolável :-( ")
if unco4 == 0:
    print ("O nivel 4 é um sistema controlável!")
else:
    print("Uma pena, o sistema do nível 4 é incontrolável :-( ")

# Código Okay!

print(np.linalg.matrix_rank(C1))
print(np.linalg.matrix_rank(C2))
print(np.linalg.matrix_rank(C3))
print(np.linalg.matrix_rank(C4))
