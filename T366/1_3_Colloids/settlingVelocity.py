import math
import set_size

delta_pho= float(input("Set the difference in Density: "))
gravity = 9.81
particle_radius = float(input("Set the particle radius: "))*set_size.get_size()
liquid_dynamic_viscosity = float(input("Set the liquid dynamic viscosity: "))

settlingVelocity = (2*delta_pho*gravity*particle_radius)/(9*liquid_dynamic_viscosity)

print(settlingVelocity)