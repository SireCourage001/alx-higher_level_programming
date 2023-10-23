#!/usr/bin/python3

"""Function that divides element by element 2 lists."""

def list_division(my_list, my_list_2, list_length):

    updated_list = []
    for list_len_ret in range(list_length):
        try:
            res = 0
            res = my_list[list_len_ret] / my_list_2[list_len_ret]
            except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            updated_list.append(res)
            return updated_list
