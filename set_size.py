ATTO = pow(10, -19)
NANO = pow(10, -9)
MICRO = pow(10, -7)
CUBIC = pow(10, -6)
MILLI = pow(10, -3)
KILO = pow(10, 3)


gravity = 9.81


def get_size():
        size = input("What size: ")
        if size == "NANO":
            return NANO
        elif size == "MICRO":
            return MICRO
        elif size == "ATTO":
            return ATTO
        elif size == "MILLI":
            return MILLI
        elif size == "KILO":
            return KILO
        elif size == "CUBIC":
            return CUBIC
        else:
            return 0
