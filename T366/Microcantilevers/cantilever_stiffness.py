import set_size

width = float(input("Set the width: ")) * set_size.get_size()
length = float(input("Set the length: ")) * set_size.get_size()
thickness = float(input("Set the thickness: ")) * set_size.get_size()
youngs_modulus= float(input("Set the Young's modulus: ")) * set_size.get_size()

cantilever_stiffness = (youngs_modulus*width*pow(thickness,3))/(4*pow(length,3))

print(cantilever_stiffness)