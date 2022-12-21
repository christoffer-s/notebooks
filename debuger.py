def integer(n):
    if isinstance(n, list):
        for i, num in enumerate(n):
            try:
                if float(num).is_integer():
                    n[i] = int(float(num))
                
                else:
                    n[i] = float(num)
            
            except:
                continue
        
        return n

    else:
        try:
            if float(n).is_integer():
                return int(float(n))
            
            else:
                return float(n)
        except:
            return n
    
    

tall = ["hello", "4.2", 4.2, 4, 2, 54.0, "54.0"]
    
print(integer(tall))