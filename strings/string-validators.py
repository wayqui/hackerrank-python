if __name__ == '__main__':
    s = input()
    esAlfanum = False
    esLetra = False
    esDigito = False
    esMinusc = False
    esMayusc = False

    for char in s:
        if char.isalnum():
            esAlfanum = True
            break

    for char in s:
        if char.isalpha():
            esLetra = True
            break

    for char in s:
        if char.isdigit():
            esDigito = True
            break

    for char in s:
        if char.islower():
            esMinusc = True
            break

    for char in s:
        if char.isupper():
            esMayusc = True
            break

    print(esAlfanum)
    print(esLetra)
    print(esDigito)
    print(esMinusc)
    print(esMayusc)
