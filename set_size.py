ATTO = pow(10, -19)
NANO = pow(10, -9)
MICRO = pow(10, -6)
MILLI = pow(10, -3)
KILO = pow(10, 3)


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
        else:
            return 0
