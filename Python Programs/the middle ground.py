p = int(input())
r = int(input())

p = p*(1+(r/100))**2
print(0.95*(p*r*2)/100+p)