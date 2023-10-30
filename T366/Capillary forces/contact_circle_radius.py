import set_size
import math
import approximate_radius
import capillary_length

if approximate_radius.approximate_radius >= capillary_length.capillary_length:
    contact_circle_radius = \
        ((pow(approximate_radius.approximate_radius,1.5))/pow(capillary_length.capillary_length, 0.5))
elif approximate_radius.approximate_radius <= capillary_length.capillary_length:
    contact_circle_radius = \
        ((pow(approximate_radius.approximate_radius,2))/capillary_length.capillary_length)

print("The contact circle radius is: \n" )
print(contact_circle_radius)
