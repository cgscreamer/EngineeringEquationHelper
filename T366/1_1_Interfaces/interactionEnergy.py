import math
import set_size


sizeA = pow(10, float(input("Set the number for A: ")))
ConstantA= float(input("Set Constant A: "))*float(sizeA)

sizeB = pow(10, float(input("Set the number for B: ")))
ConstantB= float(input("Set Constant B: "))*float(sizeB)

separationDistance = float(input("Set the distance between the spheres: "))*float(set_size.get_size())


interactionEnergy = ((ConstantB)/math.pow(separationDistance, 12)-((ConstantA)/math.pow(separationDistance, 6)))

print(interactionEnergy)