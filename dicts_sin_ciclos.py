def run():
    """my_dict = {}

    for i in range(1, 101):
        if i%3!=0:    
            my_dict[i] = i**3

    print(my_dict)"""

    my_dict = {i: i**3 for i in range(1,101) if i%3 !=0}
    #print(my_dict)

    sqrt_nat = {j : round(j**.5, 2) for j in range(1,1001)}
    print(sqrt_nat)


if __name__ == '__main__':
    run()