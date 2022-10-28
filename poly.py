from cmath import sqrt
from re import X

S: list[int] = [-1, -2, -206, -6, -1001, -2002, 10, 36, 19, 120, 17]
a = int(input('enter a: '))

b = int(input('enter b:'))

c = int(input('enter c:'))

p = sqrt ((b*b) - (4*a*c))

x1: complex= (-b-p)/(2*a)
x2: complex= (-b+p)/(2*a)
print(x1)
print(x2)

if x1 and x2 in S:
    print('cheer!you guessed one of our jackpots polynomials >>')
elif x1 or x2 in S:
    print("Congratulations! you guessed one of our polynomials winners >>")
else:
    print("Thanks for participating! you can try again your luck >>")