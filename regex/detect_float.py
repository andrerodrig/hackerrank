import re

a_float = re.compile(r"[-+]?([0-9]+)?\.[0-9]+")


def main():
    n_numbers = int(input())
    arr_inputs = []
    for i in range(n_numbers):
        arr_inputs.append(input())

    print(arr_inputs)

    arr_decisive = []
    for el in arr_inputs:
        if a_float.match(el):
            try:
                float(el)
            except ValueError:
                arr_decisive.append(False)
            else:
                arr_decisive.append(True)

        else:
            arr_decisive.append(False)

    print(arr_decisive)


main()
