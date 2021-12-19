from ListaDoble import NodeTemp
class Lista_Circular:
    def __init__(self):
        self.inicio = None 
        self.final = None 
    def listar(self, data):
        nuevoNodo = NodeTemp(data)
        if self.inicio == None:
            self.inicio = nuevoNodo
            self.final = self.inicio 
            self.vincular()
        else:
            aux = self.final 
            aux.siguiente = nuevoNodo
            self.final = aux.siguiente
            self.final.anterior = aux
            self.vincular()

    def vincular(self):
        self.inicio.anterior = self.final
        self.final.siguiente = self.inicio
        
    def mostrar(self):
        actual = self.inicio
        while True:
            yield actual.data
            actual = actual.siguiente
            if actual == self.inicio:
                break

    def mostrarFinal(self):
        actual = self.final
        while True:
            yield actual.data
            actual = actual.anterior
            if actual == self.final:
                break


    
if __name__ == "__main__":
    lista = Lista_Circular()
    for i in range(7):
        lista.insertar(i+1)
    graphviz = ""
    for node in lista.mostrar():
        print(node)
    for node in lista.mostrarFinal():
        print(node.data)
        