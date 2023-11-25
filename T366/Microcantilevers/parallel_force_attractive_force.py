import set_size

separationDistance = float(input("Set the distance between the plates: ")) * float(set_size.get_size())
vacuum_permitivity = float(8.854 * pow(10, -12))
relative_permitivity = float(input("Set the relative permitivity: "))
plate_width = float(input("Set the plate width: ")) * float(set_size.get_size())
potential_difference = float(input("Set the potential difference: "))

attractive_force = (vacuum_permitivity * relative_permitivity * plate_width * (pow(potential_difference, 2))) \
                   / (2 * separationDistance)

print(attractive_force)
