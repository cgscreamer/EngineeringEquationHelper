import set_size
from T366 import Capillary_forces
from T366.Capillary_forces import capillary_length

height = float(input("Set the height: "))
time = float(input("how much time has passed: "))
dynamic_viscosity = float(input("Set the dynamic viscosity: "))
volume = float(input("Set the volume: "))*float(set_size.get_size())
capillary_length = capillary_length.capillary_length
liquid_density = Capillary_forces.capillary_length.liquid_density

liquid_surface_tension = Capillary_forces.capillary_length.liquid_surface_tension

if capillary_length > height:
    radius = (pow(volume, 0.3))*(pow(((liquid_surface_tension*time)/dynamic_viscosity), 0.1))
elif capillary_length < height:
    radius = (pow(volume, 0.375)) * (pow(((liquid_density * set_size.GRAVITY * time) / dynamic_viscosity), 0.125))
else:
    print("incorrect calculation")

print(volume)
print(radius)
