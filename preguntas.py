"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
        
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ",") for line in data]   
    
    return sum([int(row[2]) for row in data])

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
    from collections import Counter
    
    with open("data.csv", "r") as file:
        data = file.readlines()
        
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ",") for line in data]
    
    return sorted(list(Counter([row[0] for row in data]).items()))







def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
        
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ",") for line in data]  
    
    data_1 = [line.split(",") for line in data]

    data_1 = [[row[0], int(row[1])] for row in data_1]


    from collections import defaultdict


    merged = defaultdict(lambda: [0])

    for user, *values in data_1:               
        merged[user] = [sum(i) for i in zip(values, merged[user])]
        
    
    return sorted([(row[0], row[1][0]) for row in list(merged.items())])




def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ",") for line in data]  

    from collections import Counter

    
    data_2 = [line.split(",") for line in data]


    return sorted(list(Counter([month[1] for month in [row[2].split("-") for row in data_2]]).items()))



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ",") for line in data]  
    
    data_1 = [line.split(",") for line in data]

    data_1 = [[row[0], int(row[1])] for row in data_1]


    grouped = {}

    for name, x in data_1:
        grouped.setdefault(name, []).append((x))
        
    return sorted([(key[0], max(key[1]), min(key[1])) for key in grouped.items()])


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ",") for line in data]  
    
    data_1 = [line.split(",") for line in data]

    filtered_dict_list = [list(filter(lambda x: len(x)> 2, row)) for row in [row[5:] for row in data_1]]

    data_dict = {}

    for row in filtered_dict_list:
        for value in row:
            data_dict.setdefault(value[:3], []).append(int(value[4:]))
    
    return sorted([(key[0], min(key[1]), max(key[1])) for key in data_dict.items()])






def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    
    with open("data.csv", "r") as file:
        data = file.readlines()
    
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ",") for line in data]  
    
    data_1 = [line.split(",") for line in data]    
    data_1 = [[row[0], int(row[1])] for row in data_1]

    grouped = {}

    for name, x in data_1:
        grouped.setdefault(x, []).append((name))
            
        
    return sorted([key for key in grouped.items()])




def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    
    with open("data.csv", "r") as file:
        data = file.readlines()
    
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ",") for line in data]  
    
    data_1 = [line.split(",") for line in data]
    data_1 = [[row[0], int(row[1])] for row in data_1]  

    grouped = {}

    for name, x in data_1:
        grouped.setdefault(x, []).append((name))
    
    
    return sorted([(key[0], sorted(set(key[1]))) for key in grouped.items()])





def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data_1 = [line.split(",") for line in data]

    filtered_dict_list = [list(filter(lambda x: len(x)> 2, row)) for row in [row[5:] for row in data_1]]

    data_dict = {}

    for row in filtered_dict_list:
        for value in row:
            data_dict.setdefault(value[:3], []).append(int(value[4:]))
    
    return dict(sorted({key:len(value) for (key,value) in data_dict.items()}.items()))




def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ",") for line in data]  
    
    data_1 = [line.split(",") for line in data]
    
    
    return [(row[0], len(list(filter(lambda x: len(x) < 2, row[3:]))), len(list(filter(lambda x: len(x) >2, row[3:])))) for row in data_1]





def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ",") for line in data]  
    
    data_1 = [line.split(",") for line in data]
    values_list = [[list(filter(lambda x: len(x) < 2, row[3:])), int(row[1])]for row in data_1]

    from collections import defaultdict


    merged = defaultdict(lambda: [0])

    for key, *values in values_list:
        for i in key:
            merged[i] = [sum(values) for values in zip(values,merged[i])]

    return dict(sorted({key:value[0] for (key,value) in merged.items()}.items()))





def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
    
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ",") for line in data]  
    
    data_1 = [line.split(",") for line in data]
    values_list = [[row[0], list(filter(lambda x: len(x) > 2, row[3:]))] for row in data_1]

    valores = []

    for i in values_list:
        valores.append([i[0], [int(j[4:]) for j in i[1]]])


    data_dict = {}

    for row in valores:
        data_dict.setdefault(row[0], []).append(sum(row[1]))

    return dict(sorted({key:sum(value) for (key,value) in data_dict.items()}.items()))
