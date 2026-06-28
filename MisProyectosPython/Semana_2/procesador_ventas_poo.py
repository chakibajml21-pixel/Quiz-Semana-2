# procesador_ventas_poo.py
# Actividad 2 - Refactorización a Programación Orientada a Objetos (POO)

# Clase que representa una venta
class Venta:
    def __init__(self, producto_id, categoria, valor):
        self.producto_id = producto_id
        self.categoria = categoria
        self.valor = int(valor)

    def __str__(self):
        return f"Producto: {self.producto_id}, Categoría: {self.categoria}, Valor: {self.valor}"


# Clase que administra todas las ventas
class ProcesadorVentas:
    def __init__(self):
        self.ventas = []

    # Cargar ventas desde un archivo
    def cargar_ventas(self, nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                venta = Venta(partes[0], partes[1], partes[2])
                self.ventas.append(venta)

    # Calcular el valor total
    def calcular_valor_total(self):
        total = 0
        for venta in self.ventas:
            total += venta.valor
        return total

    # Filtrar ventas por categoría
    def filtrar_por_categoria(self, categoria):
        lista_filtrada = []
        for venta in self.ventas:
            if venta.categoria == categoria:
                lista_filtrada.append(venta)
        return lista_filtrada

    # Ejecutar el sistema
    def ejecutar(self):
        self.cargar_ventas("ventas.txt")

        print("Valor total de las ventas:", self.calcular_valor_total())

        print("\nVentas de ELECTRONICA:")
        electronica = self.filtrar_por_categoria("ELECTRONICA")
        for venta in electronica:
            print(venta)


# Programa principal
sistema = ProcesadorVentas()
sistema.ejecutar()
