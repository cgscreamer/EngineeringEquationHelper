NANOMETERS = pow(10, -9)
MICROMETERS = pow(10, -6)
ATTO = pow(10, -19)


def get_size():
        size = input("What size molecule: ")
        if size == "NANOMETERS":
            return NANOMETERS
        elif size == "MICROMETERS":
            return MICROMETERS
        elif size == "ATTO":
            return ATTO

        else:
            return 0
