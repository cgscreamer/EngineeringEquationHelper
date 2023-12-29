import math
import set_size

effectiveRadius = float(input("Radius of the first molecule: "))*float(set_size.get_size())

gamma_one = float(input("Surface energy of the first molecule: "))
gamma_two = float(input("Surface energy of the second molecule: "))
geometric_mean_energy = pow((gamma_two * gamma_one), 0.5)

adhesion_force = ((3* math.pi) * geometric_mean_energy * effectiveRadius)/2

print(adhesion_force)