def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Sarai', 'lastname': 'Gomez'}

    super_list = [
        {'firstname': 'Sarai', 'lastname': 'Gomez'},
        {'firstname': 'Facundo', 'lastname': 'Garcia'},
        {'firstname': 'Osmar', 'lastname': 'Blanco'},
        {'firstname': 'Sabina', 'lastname': 'Garcia'},
        {'firstname': 'Karen', 'lastname': 'Oviedo'},
    ]

    super_dict ={
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-3,-2,-1,0,1,2,3],
        "reales_nums": [0,.1,.2,.3,.4,.5]
    }

    for key, value in super_dict.items():
        print(key,"-",value)

    for name in super_list:
        print(name)


if __name__ == '__main__':
    run()