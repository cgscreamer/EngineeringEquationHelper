import math
import set_size

molecule_one = float(input("Set the density for the 1st molecule: "))*set_size.get_size()
molecule_two = float(input("Set the density for the 2nd molecule: "))*set_size.get_size()

difference_in_density = float(molecule_one - molecule_two)
gravity = 9.81
particle_radius = pow(float(input("Set the particle radius: "))*set_size.get_size(), 2)
liquid_dynamic_viscosity = float(input("Set the liquid dynamic viscosity: "))*set_size.get_size()

settlingVelocity = (2*difference_in_density*gravity*particle_radius)/(9*liquid_dynamic_viscosity)

print(settlingVelocity)
