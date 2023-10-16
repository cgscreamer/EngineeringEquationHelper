import math
import set_size

molecule_one = float(input("Set the density for the 1st molecule: "))*set_size.get_size()
molecule_two = float(input("Set the density for the 2nd molecule: "))*set_size.get_size()

difference_in_density = float(molecule_one - molecule_two)
gravity = 9.81
characteristic_length = pow(float(input("Set the characteristic length: "))*set_size.get_size(), 2)
liquid_surface_tension = float(input("Set the liquid surface tension: "))

eotvos_number = (difference_in_density*gravity*characteristic_length)/liquid_surface_tension

print(eotvos_number)