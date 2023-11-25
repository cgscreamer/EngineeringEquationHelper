ATTO = pow(10, -19)
PICO = pow(10, -12)
NANO = pow(10, -9)
MICRO = pow(10, -6)
CUBIC = pow(10, -6)
MILLI = pow(10, -3)
KILO = pow(10, 3)
GIGA = pow(10, 9)
YM = pow(10, 11)


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
        elif size == "PICO":
            return PICO
        elif size == "YM":
            return YM
        elif size == "GIGA":
            return GIGA
        else:
            return 0
