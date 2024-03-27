def plus (a,b):
    return a + b

def minus (a,b):
    return a - b

def mult (a,b):
    return a * b

def div (a,b):
    return a / b

def mod (a,b):
    return a % b

def pow (a,b):
    return a ** b

a = int(input(" a = "))
b = int(input(" b = "))

tr = input( "( + , - , * , / , % , ** ) AMALNI TALLANG: ")
if tr == "+" :
    print( plus(a,b) )

elif tr == "-" :
    print( minus(a,b) )

elif tr == "*" :
    print( mult(a,b) )

elif tr == "/" :
    print( div(a,b) )

elif tr == "%" :
    print( mod(a,b) )

elif tr == "**":
    print( pow(a,b) )



