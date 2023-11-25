import math
import cantilever_stiffness

width = cantilever_stiffness.width
length = cantilever_stiffness.length
thickness = cantilever_stiffness.thickness

A_cantilever_stiffness = cantilever_stiffness.cantilever_stiffness
density = float(input("Set the density: "))

microcantilever_volume = (length * width * thickness)

mass = (density * microcantilever_volume)

print("The mass is: "+ str(mass))

wert = 0.15915494309
resonant_frequency = ((wert)*(pow((A_cantilever_stiffness/(0.24/mass)), 0.5)))

print("The Resonant Frequency is: " + str(resonant_frequency))