def integer(n):
    if isinstance(n, int):
        return n
    
    elif isinstance(n, float):
        if n.is_integer():
            return int(n)
        else:
            return n

    elif isinstance(n, list):
        for i, num in enumerate(n):
            if isinstance(num, int):
                continue

            elif num.is_integer():
                n[i] = int(num)
        return n
        
    else:
        None

tall = [2012.4, 21.0, 21, 123.000, 123.0001]

print(integer(tall))