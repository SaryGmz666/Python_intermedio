def divisors(num):
    divisors =[]
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors    

def run():
    num = input("Ingresa un numero: ")
    assert num.isnumeric() and int(num) != 0, "Debes de ingresar un nùmero positivo diferente de cero"
    print(divisors(int(num)))
    print("Termino mi programa")



if __name__ == "__main__":
    run()