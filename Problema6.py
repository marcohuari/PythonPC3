
class Producto:
    def __init__(self, nom_producto, categoria, anio, descripcion):
        self.nom_producto = nom_producto
        self.categoria = categoria
        self.anio = anio
        self.descripcion = descripcion
    def __str__(self):
        return '({}) ({}) ({}) ({})'.format(self.nom_producto, self.categoria, self.anio, self.descripcion)
    
class Catalogo:
    productos = []

    def __init__(self, p = []): #puede iniciar con una cantidad de productos
        self.productos = p
        pass
    
    def mostrar(self):
        for i in self.productos:
            print(i)
        pass

    def agregar(self, p):
        self.productos.append(p)

    def buscar_producto(self, nom_producto):
        for producto in self.productos:
            if producto.nom_producto == nom_producto:
                break
        return producto

    def eliminar_producto(self, nom_producto):
        a = self.buscar_producto(nom_producto)
        self.productos.remove(a)

p1 = Producto('Coca Cola','Bebidas',2024,'Bebida gasificada y azucarada')


c1 = Catalogo([p1])
p2 = Producto('Frejol','Menestras',2024,'Menestra Peruana')
c1.agregar(p2)
#c1.mostrar()
print(c1.buscar_producto('Coca Cola'))
print('antes de eliminar')
c1.eliminar_producto('Coca Cola')
c1.mostrar()