resistors = [[10], [5]]

def resistance(r, index=0):
    typ = isinstance(r, list)
    parallel_i = []
    if typ:
        for i, val in enumerate(r):
            if isinstance(val, list):
                if len(val) > 1:
                    resistance(val, i)
                
                else:
                    
                     
            


    
    else:
        return sum(r)

print(resistance(resistors))
        
    