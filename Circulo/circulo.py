import math


class Circulo:
    def __init__(self, r):
        try:
            if r > 0:
                self.radio = r
                print("Enhorabuena! Haz creado un círuculo de radio:", r, "\nPara:"
                      "\nObtener su área con el código: nombredelcirulo.get_area()"
                      "\nObtener su perímetro con el código: 'nombredelcirculo.get_perimetro()'"
                      "\nTambién puedes modificar el valor del radio con el código: "
                      "'nombredelcirculo.set_radio_modificable('nuevoradio') "
                      "\nY puedes agrandar tu círculo n cantidad de veces lo cual creará otro Objeto 'nuevocriculo'"
                      " con el código: 'nombredelnuevocirculo' = 'nombredelcirculoactual'.agrandar_circulo(n)"
                      )
            else:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("___________________________")
            print("Hola! El radio del circulo que deseas crear debe ser mayor que 0 ... Te saluda atentamente 'Tu "
                  "Buen Amigo, 'Spiderman'")

    def get_area(self):
        a = math.pi * (self.radio ** 2)
        return a

    def get_perimetro(self):
        p = 2 * math.pi * self.radio
        return p

    def set_radio_modificable(self, rmodificado):
        try:
            if type(rmodificado) != str:
                if float(rmodificado) > 0:
                    self.radio = rmodificado
                    print("Haz modificado el radio del circulo a el valor:", rmodificado)
                else:
                    raise ""
            else:
                raise ""
        except TypeError:
            print("Lo siento, no es posible modificar el radio. Debes ingresar un radio mayor a 0.\n¡Inténtalo de "
                  "nuevo!")



