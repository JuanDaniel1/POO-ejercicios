class alumno:
    def __init__(self):
        self.nombre = input("Digite su nombre: ")
        self.nota = float(input("Digite su nota: "))

    def saludo(self):
        print("Hola ",self.nombre)
    
    def exam(self):
        if self.nota >= 3:
            print("Aprobo con la nota: ", self.nota)
        elif self.nota <= 3:
            print("No aprobo con la nota: ", self.nota) 
        
        else:
            print("La nota no es valida")


Alumno = alumno()
Alumno.saludo()
Alumno.exam()


