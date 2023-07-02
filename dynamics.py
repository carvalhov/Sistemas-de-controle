import numpy as np

"""
Primeiramenta, há uma área no mapa, que vai de -1 para +1 em x e y, 
nosso player quer atingir um determinado alvo, mas começa de uma posição inicial x = 0 e y = 0
"""

def limita(valor):
    #Vamos delimitar um valor entre um valor mínimo e máximo (-1 e 1).
    valor_minimo = -1
    valor_maximo = 1
    return max(valor_minimo, min(valor, valor_maximo))

"""O player estará em uma posição, mas atingir o alvo é seu objetivo
Logo, deve-se considerar sua posição atual (Como irá mudar com o tempo) e sua posição futura (para atingir o alvo)
"""
state = {
    'land': 'Linearland'
}
for level in range(1, 5):
    state['level'] = level

dynamics = [
    [
        lambda x, y, u: [-5.2*x + 2.5*y + 3.2*u, -9*x - 0.8*y + 5.0*u],
        lambda x, y, u: [5.0*y, -0.9*y - 9.0*x + 5*u],
        lambda x, y, u: [2.0*y - 1.2*x, -0.4*y + 3.6*x - 5*u],
        lambda x, y, u: [1.0*x - 0.4*y + 0.6*u, 1.8*x + 0.2*y - 5.0*u],
    ],
]

stateTrans = dynamics[0][state['level']-1]


"""
Para determinar as posições futuras iremos considerar as posições x e y, e a entrada U
Além disso, uma função considerando os estados de transição X = Ax(t) + Bu(t)
dt -- Representa o tempo delta, irá funcionar como um valor de 
atualização das posições do jogo, quanto menor, mais preciso o jogo, 
mas também demorará mais (Mais tempo do computador pensando)
N -- Representará o número de iterações que serão feitas no for, logo, 
quantas posições serão calculadas para o player, quanto mais posições,
 mais precisão, mas também demorará mais, igualmente a dt
"""

def futurePositions(x, y, U, stateTrans, N, dt):
    positions = []
    p = [x, y]

    for i in range(N):
        positions.append([p[0], p[1]])
        uIndex = i % len(U)
        u = U[uIndex]
        xp = stateTrans(p[0], p[1], u)
        p[0] += xp[0] * dt
        p[1] += xp[1] * dt

    return positions

"""Em posse das posições, vamos tentar determinar a menor distância a ser
percorrida da posição atual para o alvo, que iremos chamar de targetX e targetY
representando as posições do alvo em x e y. """

def Men_dist(targetX, targetY, positions):
    dMin = 100000.0 # Estabelece-se um alto valor para poder fazer a comparação
    for p in enumerate(positions):
        d = np.sqrt((targetX - p[0]) ** 2 + (targetY - p[1]) ** 2)
        # Raiz((Delta_x)^2 + (Delta_y)^2) -- Equação clássica

        if d < dMin:
            dMin = d #dMin recebe o novo valor da distância
# retorna a menor distância a ser percorrida pelo player
    return dMin 

