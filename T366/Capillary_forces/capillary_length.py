import set_size
import math

liquid_surface_tension = float(input("Set the liquid surface tension: "))
liquid_density = float(input("Set the liquid density: "))

capillary_length = math.pow((liquid_surface_tension / (set_size.GRAVITY * liquid_density)), 0.5)

print(capillary_length)