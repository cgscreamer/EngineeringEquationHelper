import set_size

width = float(input("Set the width: ")) * set_size.get_size()
length = float(input("Set the length: ")) * set_size.get_size()
thickness = float(input("Set the thickness: ")) * set_size.get_size()

microcantilever_volume = (length * width * thickness)

print(microcantilever_volume)