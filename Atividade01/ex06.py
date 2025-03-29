l = []  
n = 2   
while len(l) < 100:
    divisores = [x for x in range(1, n+1) if n % x == 0]  
    if len(divisores) == 2:  
        l.append(n)
    n += 1  
print(l)
