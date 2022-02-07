print('a=')
a = input()
print('b=')
b = input()
print('c=')
c = input()
a = int(a)
b = int(b)
c = int(c)
d = (a**2+b**2)/(3*b-4)
e = 4*c**5/6
print('Целая часть:')
div = d//e
print(div)
print('Остаток от деления:')
mod = d % e
print(mod)
