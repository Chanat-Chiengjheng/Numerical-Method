a = int(input("Enter the lower limit a: "))
b = int(input("Enter the upper limit b: "))
n = int(input("Enter the number of subintervals n: "))

def f(x):
    return x**2

def Trapezoidal_Rule(a,b,n):
    
    integral_solution = 0.5 * (f(a) + f(b))
    h = (b - a) / n
    for i in range(1, n):
        x = a + i*h
        integral_solution += f(x)

    integral_solution *= h

    return integral_solution
    

result = Trapezoidal_Rule(a,b,n)
print(result)