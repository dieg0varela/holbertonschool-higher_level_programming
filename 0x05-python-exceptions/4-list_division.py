#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = 0
    lista = []
    for val in range(list_length):
        try:
            res = my_list_1[val] / my_list_2[val]
            lista.append(res)
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except (TypeError, ValueError):
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            lista.append(res)
    return (lista)
