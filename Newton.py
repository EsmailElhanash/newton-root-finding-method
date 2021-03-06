from sympy import *
print('Enter a function of x: ')
f = input()
print('Enter initial guess: ')
iGuess = float(input())
x = Symbol('x')
fd1 = diff(f,x)
fd2 = diff(fd1,x)
f = lambdify(x, f)
fd1 = lambdify(x, fd1)
fd2 = lambdify(x,fd2)
x_1st = (iGuess - fd1(iGuess)/fd2(iGuess))
re1 = (abs(iGuess - x_1st) / abs(x_1st))
x_2nd = (x_1st - fd1(x_1st)/fd2(x_1st))
re2 = (abs(x_1st- x_2nd) / abs(x_2nd))
x_3rd = (x_2nd - fd1(x_2nd)/fd2(x_2nd))
re3 = (abs(x_2nd - x_3rd) / abs(x_3rd))
f_max = (f(x_3rd))

print('x1='+str(x_1st)+',e1='+str(re1))
print('x2='+str(x_2nd)+',e2='+str(re2))
print('x3='+str(x_3rd)+',e3='+str(re3))
print('fmax='+str(f_max))