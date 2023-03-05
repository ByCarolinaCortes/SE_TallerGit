import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if _name_ == "_main_":
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        print(factorial(n))
    else:
        print("Error: Debe ingresar un número como argumento")