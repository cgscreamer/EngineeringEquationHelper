import math

wavelength= float(input("what's the wavelength: "))
theta = float(input("what's 2 x theta: "))
braggs_law = (1*wavelength)/(2*(math.sin(math.radians(theta/2))))

print(braggs_law)