chart = {}

def memofibo(n):  
    
    if n in chart:
        
        return chart[n]
        
    elif n <= 2:
        
        return 1
    
    else:

        chart[n] = memofibo(n-1) + memofibo(n-2)
    
    return chart[n]
    
print (memofibo(24))
