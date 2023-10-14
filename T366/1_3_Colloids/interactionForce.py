import math
import set_size

R1 = float(input("Radius of the first molecule: "))*float(set_size.get_size())
R2 = float(input("Radius of the second molecule: "))*float(set_size.get_size())
effectiveRadius = (R1*R2)/(R1 + R2)

hamakerConstant = float(input("Set the Hamaker Constant: "))*float(set_size.get_size())

separationDistance = pow(float(input("Set the distance between the spheres: "))*float(set_size.get_size()), 2)


interactionForce = (hamakerConstant*effectiveRadius)/(12*separationDistance)

print(interactionForce)
