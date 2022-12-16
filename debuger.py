def integer(n):
    if isinstance(n, int):
        return n
    
    elif isinstance(n, float):
        return int(n)

    elif sinstance(n, list):
        for i, num in enumerate(n):
            if isinstance(num, int):
                continue

            elif num.is_integer():
                n[i] = int(num)
        return n
        
    else:
        None

tall = 2000.2

print(integer(tall))