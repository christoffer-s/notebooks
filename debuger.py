def serie(r):
    return sum(r)

def parallel(r):
    rp = 0
    for resistor in r:
        rp += resistor ** -1
    
    return rp ** -1

def identifyer(r):
    for resistor in r:
        if not isinstance(resistor, list):
            pass


print(parallel([2, 2]))