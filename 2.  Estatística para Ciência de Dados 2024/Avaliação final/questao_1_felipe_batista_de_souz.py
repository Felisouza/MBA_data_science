import numpy as np
import scipy.stats as st

# Definindo a distribuição de probabilidade
valores = np.array([0, 1, 2])
probabilidades = np.array([0.1, 0.3, 0.6])

# Número de simulações e tamanho da amostra
n_simulacoes = 1000
tamanho_amostra = 100

# Simulando as amostras e calculando as médias amostrais
medias_amostrais = []
for _ in range(n_simulacoes):
    amostra = np.random.choice(valores, size=tamanho_amostra, p=probabilidades)
    media_amostral = np.mean(amostra)
    medias_amostrais.append(media_amostral)

# Calculando a probabilidade de a média amostral ser maior que 1,5
probabilidade = np.mean(np.array(medias_amostrais) > 1.5)

print(f"A probabilidade teórica de a média ser maior que 1,5 é aproximadamente 0 (ou muito próxima, considerando a média teórica de 1,5).")
print(f"A probabilidade simulada de a média amostral ser maior que 1,5 é {probabilidade:.2f}.")


def esperanca(X,P):
    E = 0
    for i in range(0, len(X)):
        E = E + X[i]*P[i]
    return E
    
def variancia(X,P):
    E = 0; E2 = 0
    for i in range(0, len(X)):
        E = E + X[i]*P[i]
        E2 = E2 + (X[i]**2)*P[i]
    V = E2-E**2
    return V
    
X = [0,1,2]
P = [0.1,0.3,0.6]
E = esperanca(X,P)
V = variancia(X,P)
print("Esperança:", E, "Variância:", round(V, 2))

mu = E
sigma = np.sqrt(V)
n = 100
x = 1.5
Z = (x - mu)/(sigma/np.sqrt(n))
pt = 1-st.norm.cdf(Z)
print('Probabilidade:',pt)