import math

class Vector():
    def __init__(self,mag=0,ang=0,x=0,y=0,mag_input=False):
        if mag_input:
            self.mag = mag
            self.ang = ang
            self.x = mag * math.cos(ang)
            self.y = mag * math.sin(ang)
        else:
            self.x = x
            self.y = y
            self.mag = math.sqrt(x**2 + y**2)
            self.ang = math.atan2(y,x)
    
    def __add__(self,other):
        return Vector(x=self.x+other.x,
                    y=self.y+other.y)
    
    def __str__(self):
        return f"Vector(x={self.x},y={self.y},mag={self.mag},ang={self.ang})"

def main():
    print("""Elige el modo de entrada de los vectores:
            1. Magnitud y ángulo
            2. Coordenadas cartesianas""")
    modo = int(input("Modo: "))
    if modo == 1:
        mag1 = float(input("Magnitud vector 1: "))
        ang1 = float(input("Ángulo vector 1: "))
        mag2 = float(input("Magnitud vector 2: "))
        ang2 = float(input("Ángulo vector 2: "))
        v1 = Vector(mag1,ang1,mag_input=True)
        v2 = Vector(mag2,ang2,mag_input=True)
    elif modo == 2:
        x1 = float(input("x vector 1: "))
        y1 = float(input("y vector 1: "))
        x2 = float(input("x vector 2: "))
        y2 = float(input("y vector 2: "))
        v1 = Vector(x=x1,y=y1)
        v2 = Vector(x=x2,y=y2)
    else:
        print("Modo no válido")
        return
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    v3 = v1 + v2
    print(f"Vector 3: {v3}")


if __name__ == "__main__":
    main()