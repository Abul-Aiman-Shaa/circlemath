# Importing Math
import math

# Function for get the area of a circle with radius 
def orarea(radius:int):   # orarea == circle radius area
    area = (math.pi * radius) * radius   # pi x r x 2
    return area

# Function for get the area of a circle with diameter
def odarea(diameter:int):   # odarea == circle diameter area
    radius = (diameter/2)                # D/2
    area = (math.pi * radius) * radius   # pi x r x 2
    return area

# Function for get the circumfrence of a circle with radius
def orcir(radius:int):      # orcir == circle radius circumfrence
    cir = (2 * math.pi * radius)          # 2 x pi x r
    return cir

# Function for get the circumfrence of a circle with radius
def odcir(diameter:int):    # odcir == circle diameter circumfrence
    cir = (math.pi * diameter)            # c = pi x d
    return cir


if __name__ == "__main__":
    # Check for area of circle with radius
    print(orarea(5))
    print()

    # Check for area of circle with diameter
    print(odarea(10))
    print()

    # Check for circumfrence of circle with radius
    print(orcir(32))
    print()

# Check for circumfrence of circle with diameter
print(odcir(24))
