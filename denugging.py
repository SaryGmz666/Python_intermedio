def divisors(num):
    divisors =[]
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors    

def run():
    try: 
        num = int(input("Ingresa un numero: "))
        try:
            if num <= 0:
                raise ValueError("No puedes ingresar números negativos o el valor cero")
        except ValueError as ve:
            return print(ve)
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Debes de ingresar un número")


if __name__ == "__main__":
    run()