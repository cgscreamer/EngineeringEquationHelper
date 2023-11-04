import set_size
import math

volume = float(input("Volume of the water droplet: "))*float(set_size.get_size())

approximate_radius = math.pow((3 * volume)/(4 * math.pi),(1/3))

print(approximate_radius)