"""
Clase Perro.

Autor: Jaime Rabasco Ronda.
"""
class Perro:
    def ladrar(self):
        """
        Función que imprime lo que sería la simulación de un ladrido
        """
        self.ladra = 'Guau'
        print(self.ladra);

p = Perro();
p.ladrar();
