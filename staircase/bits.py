def change_ads(base10):
    base2 = ''
    while base10 > 0:
        base2 = str(base10 % 2) + base2
        q = base10 // 2
        base10 = q

    print(base2)

    b = ''
    for el in base2:
        if el == '1':
            b += '0'
        elif el == '0':
            b += '1'

    b_int = [int(i) for i in b]
    result = 0
    for index in range(len(b_int)):
        print(f'x: {b_int[index]}')
        result += b_int[index] * 2 ** (len(b_int) - 1 - index)
        print(result)
    print(result)
    return b_int, result


print(change_ads(50))
