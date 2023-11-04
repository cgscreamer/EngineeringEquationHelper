from T366 import Capillary_forces
from T366.Capillary_forces import capillary_length
import math

rotation_speed = float(input("set the rotation speed: "))
rpm = (2 * math.pi * rotation_speed)/60
dynamic_viscosity = float(input("Set the dynamic viscosity: "))
liquid_density = Capillary_forces.capillary_length.liquid_density
time = float(input("set the time: "))

spin_coating_thickness = (1/rpm)*(pow(((3*dynamic_viscosity)/(4*liquid_density)),0.5))*(1/(pow(time, 0.5)))

print(spin_coating_thickness)