"""
Recursividad:
1.Programa que calcula el factorial de un numero usando una funcion recursiva,
2.Funcion recursiva que suma los elementos de una lista. 

"""


def factorial(n):
    if n == 1: #caso base
        return 1
    else:
       return n * factorial(n-1)


def suma_lista(n):
    if len(n) == 0: #caso base
        return False
    else:
        return n.pop() + suma_lista(n)
        
        


def main():
    n = 5
    print(f"El factorial de {n} es {factorial(n)}")

    a = [3,2,3,4]
    print(f"La sumatoria de {a} es {suma_lista(a)}")

main()
