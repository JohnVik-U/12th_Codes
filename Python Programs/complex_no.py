a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(str(a+c),'+', str(b+d)+'j')
print(str(a+c), '-' ,str(b+d)+'j')
print(str(a*c - b*d), '+' ,str(b*c + a*d)+'j')
print(str((a*c + b*d)/(c**2 + d**2)), '+' ,str((b*c - a*d)/(c**2 + d**2)) +'j')
