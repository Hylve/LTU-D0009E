#uppgift1
def bounce (n):
    if n == 0:
        print 0,
    elif n>0: 
        print n,
        bounce(n-1)
        print n,
    else:
        print "Funktionen är Def för >= 0"

#uppgift2
def bounce2(n):
#hjälpvariabel
    N=n
    while (n>0):
        print n,
        n=n-1
    while n<=N:
        print n,
        n=n+1
#uppgift3
def tvarsum(n):
        if n>0:
            n=n%10+tvarsum(n/10)
        return n
#uppgift4
def tvarsum2(n):
    summa = 0
    while(n>0):
        summa += n%10
        n /= 10
    return summa
#uppgift5
#5a
def derivative(f,x,h):
    fd = ((f(x + h/2) - f(x - h/2) ) / h)
    return float(fd)
#5b
#x0 ursprungsgissning, x nuvarande gissning, h noggrannhet
def solve(f, x0, h):
    x = 0
    while True:
        x = x0-(f(x0)/derivative(f, x0, h))
        if abs(x-x0)<h:
            return x
        x0 = x
#-----------------------------------------------
def testfunc1(x):
    gamma = x**2
    return float(gamma)

def testfunc2(x): 
    alfa = (x**2)-1
    return float(alfa)
#-1 och 1

def testfunc3(x):
    beta = ((2**x)-1)
    return float(beta)
#0
def testfunc4(x):
    charlie = ((x**2)-4)
    return float(charlie)
#2
