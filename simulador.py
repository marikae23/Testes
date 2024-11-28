import random
import matplotlib.pyplot as plt

# Entrada do Usuário
num_dados = int(input("Quantos dados você quer lançar? "))
num_lados = 6  

# Cria um histograma para visualizar os resultados dos lançamentos de dados
def exibir_graficamente(resultados, titulo):
    plt.hist(resultados, bins=range(1, num_lados + 2), edgecolor='black', align='left', rwidth=0.8)
    plt.xlabel('Resultado do Dado')  # Rótulo do eixo X
    plt.ylabel('Frequência')  # Rótulo do eixo Y
    plt.title(titulo)  # Título do gráfico
    plt.xticks(range(1, num_lados + 1))  # Define os valores dos ticks no eixo X
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adiciona uma grade no eixo Y
    plt.show()  # Mostra o gráfico

# Paradigma Imperativo
# -------------------
# Função que simula o lançamento de um número especificado de dados
# Usa uma abordagem imperativa, iterando sobre cada lançamento e armazenando os resultados

def simulador_dados_imperativo(num_dados, num_lados):
    resultados = []  
    for _ in range(num_dados):
        
        resultado = random.randint(1, num_lados)
        resultados.append(resultado)  
    print("Resultados (Imperativo):", resultados) 
    exibir_graficamente(resultados, "Resultados (Imperativo)")  
simulador_dados_imperativo(num_dados, num_lados)


# Paradigma Orientado a Objetos
# -----------------------------
# Definindo uma classe para representar um dado
class Dado:
    def __init__(self, lados):
        self.lados = lados  
    
    def rolar(self):
        return random.randint(1, self.lados)

# Classe para simular o lançamento de vários dados
class SimuladorDados:
    def __init__(self, num_dados, lados):
        # Cria uma lista de objetos Dado com o número especificado de lados
        self.dados = [Dado(lados) for _ in range(num_dados)]
    
    def simular(self):
        resultados = [dado.rolar() for dado in self.dados]
        print("Resultados (Orientado a Objetos):", resultados) 
        exibir_graficamente(resultados, "Resultados (Orientado a Objetos)")  
simulador = SimuladorDados(num_dados, num_lados)
simulador.simular()


# Paradigma Funcional
# -------------------
# Função pura que rola um dado de um determinado número de lados
# Não modifica estado e não tem efeitos colaterais

def rolar_dado(lados):
    return random.randint(1, lados)

# Função que simula o lançamento de vários dados usando uma abordagem funcional
# Utiliza map e lambda para gerar os resultados

def simular_dados_funcional(num_dados, lados):
    # Gera uma lista de resultados aplicando a função rolar_dado a cada item do range
    resultados = list(map(lambda _: rolar_dado(lados), range(num_dados)))
    print("Resultados (Funcional):", resultados) 
    exibir_graficamente(resultados, "Resultados (Funcional)") 
simular_dados_funcional(num_dados, num_lados)
