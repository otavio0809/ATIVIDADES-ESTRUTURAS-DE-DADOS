# Definindo a classe PersonalArray que será usada para armazenar elementos
class PersonalArray:
    SIZE = 5
    insertPosition = 0
    elements = [None] * SIZE

    # Função que serve para definir se o array está vazio ou não
    def isEmpty(self):
        return self.size() == 0
    
    # Função que serve para retornar o número de elementos já armazenados no array
    def size(self):
        return self.insertPosition
        
    # Função que serve para definir se precisamos de mais memória
    def isMemoryFull(self):
        return self.insertPosition == len(self.elements)
    
    # Função para inserir um novo elemento na lista
    def append(self, newElement):
        if self.isMemoryFull():
            self.updateMemory()
        self.elements[self.insertPosition] = newElement
        self.insertPosition += 1
    
    # Função para aumentar a memória quando necessário
    def updateMemory(self):
        newArray = [None] * (self.size() + self.SIZE)
        for position in range(self.insertPosition):
            newArray[position] = self.elements[position]
        self.elements = newArray
    
    # Função para limpar o array
    def clear(self):
        self.elements = [None] * self.SIZE
        self.insertPosition = 0
    
    # Função para remover o último elemento
    def remove(self):
        if not self.isEmpty():
            self.elements[self.insertPosition - 1] = None
            self.insertPosition -= 1
    
    # Função para remover um elemento em uma posição específica
    def removePosition(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return ""
        removedElement = self.elements[position]
        index = position
        while index < self.insertPosition - 1:
            self.elements[index] = self.elements[index + 1]
            index += 1
        self.insertPosition -= 1
        return removedElement
        
    # Função para inserir um elemento em uma posição específica
    def insertAt(self, position, newElement):
        if position < 0 or position > self.insertPosition:
            print("Posição inválida!")
            return
        if self.isMemoryFull():
            self.updateMemory()
        index = self.insertPosition - 1
        while index >= position:
            self.elements[index + 1] = self.elements[index]
            index -= 1
        self.elements[position] = newElement
        self.insertPosition += 1   
    
    # Função para retornar um elemento em uma posição específica
    def elementAt(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return None
        return self.elements[position]


# Exemplo de Situação Diária: Fila de Atendimento no Supermercado (FIFO)
class PersonalQueue:
    def __init__(self):
        self.list = PersonalArray()  # Agora inicializamos com PersonalArray

    def enqueue(self, newElement):
        self.list.insertAt(0, newElement)  # Adiciona um cliente na fila
    
    def dequeue(self):
        return self.list.removePosition(self.list.size() - 1)  # Atende o próximo cliente (retira o primeiro)

# Exemplo de Situação Diária: Histórico de Navegação (Pilha - LIFO)
class PersonalStack:
    def __init__(self):
        self.list = PersonalArray()  # Agora inicializamos com PersonalArray

    def push(self, newElement):
        self.list.insertAt(0, newElement)  # Empilha uma nova página visitada
    
    def pop(self):
        return self.list.removePosition(0)  # Desempilha a última página visitada (volta para a anterior)


# Simulando a fila de caixa de supermercado:
print("Fila de Caixa do Supermercado (FIFO):")

# Cria a fila
supermercadoFila = PersonalQueue()

# Clientes entram na fila
supermercadoFila.enqueue("Cliente 1")
supermercadoFila.enqueue("Cliente 2")
supermercadoFila.enqueue("Cliente 3")
supermercadoFila.enqueue("Cliente 4")
supermercadoFila.enqueue("Cliente 5")

# Atendendo os clientes e imprimindo quem foi atendido
print(f"Atendimento: {supermercadoFila.dequeue()}")  # Esperado Cliente 1
print(f"Atendimento: {supermercadoFila.dequeue()}")  # Esperado Cliente 2
print(f"Atendimento: {supermercadoFila.dequeue()}")  # Esperado Cliente 3
print(f"Atendimento: {supermercadoFila.dequeue()}")  # Esperado Cliente 4
print(f"Atendimento: {supermercadoFila.dequeue()}")  # Esperado Cliente 5


# Simulando o histórico de navegação (Pilha - LIFO):
print("\nHistórico de Navegação (Pilha - LIFO):")

# Cria o histórico de navegação
historicoNavegacao = PersonalStack()

# Visitando páginas
historicoNavegacao.push("Página 1")
historicoNavegacao.push("Página 2")
historicoNavegacao.push("Página 3")
historicoNavegacao.push("Página 4")
historicoNavegacao.push("Página 5")

# Navegando para as páginas anteriores e imprimindo quem foi "desempilhado"
print(f"Voltando para: {historicoNavegacao.pop()}")  # Esperado "Página 5"
print(f"Voltando para: {historicoNavegacao.pop()}")  # Esperado "Página 4"
print(f"Voltando para: {historicoNavegacao.pop()}")  # Esperado "Página 3"
print(f"Voltando para: {historicoNavegacao.pop()}")  # Esperado "Página 2"
print(f"Voltando para: {historicoNavegacao.pop()}")  # Esperado "Página 1"