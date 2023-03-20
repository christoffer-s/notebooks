def parallel(r):
    rp = 0
    for resistor in r:
        rp += resistor ** -1
    
    return rp ** -1


# 2d arrays
def identifyer(r):
    rp_index = []
    for index, resistor in enumerate(r):
        if isinstance(resistor, list):
            if len(resistor) > 1:
                r[index] = identifyer(resistor)

            else:
                return r

    return sum(r)

print(identifyer([2, 2, [5, 5, [3, 1]]]))