

class Alumno:
    def __init__(self,nombre,nro_registro):
        self.nombre = nombre
        self.nro_registro = nro_registro
        pass
    
    def display(self):
        print(f'Registrado con nombre de {self.nombre} y número de registro de {self.nro_registro}')
        pass

    def setAge(self,edad):
        self.edad = edad
        print(f'Edad agregado correctamente')
        print(self.edad)
        pass
    
    def setNota(self,nota):
        self.nota = nota
        print(f'Nota agregado correctamente')
        print(self.nota)
        pass

    pass

alumno_1 = Alumno('Juan',12345678)

alumno_1.display()
alumno_1.setAge(26)
alumno_1.setNota(20)
print(alumno_1.edad)
print(alumno_1.nota)
    
    