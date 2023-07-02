import dynamics as dy

def BestU(x, y, stateTrans, N, dt, targetX, targetY):
    uStar = 0.0
    dMin = 100000.0
    uMax = 1

    # Aqui se itera os valores ut1, de -Umax até Umax, em intervalos de Umax/10 = 0.1"
    for ut1 in range(-uMax, uMax, uMax // 10):
        for ut2 in range(-uMax, uMax, uMax // 10):
            positions = dy.futurePositions(x, y, [ut1, ut2], stateTrans, N, dt)
            d = dy.Men_dist(targetX, targetY, positions)

            if d < dMin:
                dMin = d
                uStar = ut1

    return uStar

"""
Lembrando que na lista dynamics, nós temos x, y e U como variáveis e 
são baseadosna relação de X`= Ax(t) + Bu(t)

Nós determinamos a menor distância a ser percorrida com a função Men_dist
E determinamos a melhor entrada de U com a função BestU, logo temos as 
informações para controlar o player para atingrir o alvo dele (target)
"""

