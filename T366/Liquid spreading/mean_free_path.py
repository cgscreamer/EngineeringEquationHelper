import math
import set_size

boltzmann_constant = float(input("Set the boltzmann constant: ")) * pow(10, -23)
temperature = float(input("Set the temperature: ")) + 273.15
particle_diameter = float(input("Set the particle diameter: ")) * set_size.get_size()
pressure = float(input("Set the pressure: ")) * set_size.get_size()

mean_free_path = (1/(math.sqrt((2)*math.pi)))*((boltzmann_constant*temperature)/(pow(particle_diameter,2))*pressure)

print(mean_free_path)
