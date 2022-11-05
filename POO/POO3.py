class Calculadora:
    def __init__(self):
        self.n1 = int(input("Digite el numero 1: "))
        self.n2 = int(input("Digite el numero 2: "))
        
    def suma(self):
        self.sum = self.n1 + self.n2
        print("Numeros sumados = ", self.sum)
    
    def resta(self):
        self.res = self.n1 - self.n2
        print("Numeros restados = ", self.res)
    
    def multiplicacion(self):
        self.mult = self.n1*self.n2
        print("Numeros multiplicados = ", self.mult)

    def division(self):
        self.div = self.n1/self.n2
        print("Numeros divididos = ", self.div)


resultado = Calculadora()
resultado.suma()
resultado.resta()
resultado.multiplicacion()
resultado.division()