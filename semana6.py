class Figura:
    def _init_(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def calcular_area(self):
        print("La figura no tiene un área definida.")


class Rectangulo(Figura):
    def _init_(self, color, base, altura):
        super()._init_(color)
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base

    def set_base(self, base):
        self.__base = base

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def calcular_area(self):
        area = self._base * self._altura
        print(f"El área del rectángulo es: {area}")


# Crear instancias de las clases
figura_generica = Figura("Rojo")
rectangulo = Rectangulo("Azul", 5, 3)

# Probar la funcionalidad de las clases
print(figura_generica.get_color())  # Salida: "Rojo"
figura_generica.calcular_area()  # Salida: "La figura no tiene un área definida."

print(rectangulo.get_color())  # Salida: "Azul"
print(rectangulo.get_base())  # Salida: 5
print(rectangulo.get_altura())  # Salida: 3
rectangulo.calcular_area()  # Salida: "El área del rectángulo es: 15"
