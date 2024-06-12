"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
"""


class Vehiculo:
    def __init__(self, num_serie, color, fabricante):
        """
        Instancia un objeto en la clase vehiculo
        :param num_serie: recibe como parametro el numero de serie del vehículo
        :param color: Recibe el color del vehículo
        :param fabricante: Recibe la marca que ha fabricado el vehículo
        """
        self.__num_serie = num_serie
        self.__color = color
        self.__fabricante = fabricante


class Coche(Vehiculo):

    num_serie = 1;
    cilindrada = 1000;
    fabricante = 'seat';
    color = 'rojo';

    def __init__(self, num_serie, cilindrada, fabricante, color):
        """
        Permite instanciar un objeto en la clase coche
        :param num_serie: Recibe el numero de serie del coche
        :param cilindrada:  REcibe la cilindrada del coche
        :param fabricante: Nombre del fabricante
        :param color: Color del coche
        """
        self.num_serie = num_serie;
        self.cilindrada = cilindrada;
        self.fabricante = fabricante;
        self.color = color;

    @property
    def num_serie(self):
        """
        Funcion utilizada para saber el numero de serie
        :return: self.__num_serie devuelve el numero de serie
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        """
        Asigan el value a numero de serie del coche
        :param value: parametro pasado que deberia ser un numero de serie de un vehiculo
        """
        self.__num_serie = value

    @property
    def color(self):
        """
        Devuelve el color del vehiculo
        :return: self.__color color del vehículo
        """
        return self.__color

    @color.setter
    def color(self, value: int):
        """
        Asiga el valor al atributo self.__color
        :param value:
        """
        self.__color = value

    @property
    def cilindrada(self):
        """
        Devuelve la cilindrada del vehiculo
        :return: self.__cilindrada
        """
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        """
        Asiga el value a la cilindrada
        :param value: self.__cilindrada , cilindrada del vehículo
        """
        self.__cilindrada = value

    @property
    def fabricante(self):
        """
        Devuelve el fabricante del vehiculo
        :return: self.__fabricante , fabricante del vehículo
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        """
        Asigna el value a el fabricante
        :param value: se espera que sea un fabricante del vehiculo
        """
        self.__fabricante = value
